from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import CreateView
from .models import Project,Category, Expense
from django.http import HttpResponseRedirect, HttpResponse
from django.utils.text import slugify
from .forms import ExpenseForm

def project_list(request):
    return render(request,"budget/project-list.html")

def project_detail(request, slug):
    project = get_object_or_404(Project, slug=slug)
    category_list = None
    if request.method == "GET":
        category_list = Category.objects.filter(project=project)
        print("Okkk")
        return render(request,"budget/project-detail.html",{"project": project,"expense_list": project.expenses.all(), "category_list":category_list })

    elif request.method == "POST":
        form = ExpenseForm(request.POST)
        if form.is_valid():
            title = forms.cleaned_data['title']
            amount = forms.cleaned_data['amount']
            category_name = forms.cleaned_data['category']
            category = get_object_or_404(Category, project=project, name=category_name)
            Expense.objects.create(
                project = project,
                title = title,
                amount = amount,
                category = category
            ).save()


    return redirect(slug)


class ProjectCreateView(CreateView):
    model = Project
    template_name = "budget/add-project.html"
    fields = ("name", "budget")

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()
        categories = self.request.POST['categoriesString'].split(',')
        for category in categories:
            Category.objects.create(
            project = Project.objects.get(id=self.object.id),
            name=category
            ).save()

            # return HttpResponseRedirect(self.get_success_url())
        # print("************* "+self.get_success_url())
        return redirect("/"+self.get_success_url())
    def get_success_url(self):
        return slugify(self.request.POST['name'])
