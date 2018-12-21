from django.db import models
from django.utils.text import slugify
from django.core.urlresolvers import reverse

class Project(models.Model):
    name =  models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, blank=True, unique=True)
    budget = models.IntegerField()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Project, self).save(*args, **kwargs)
    def __str__(self):
        return self.name
    # def get_absolute_url(self):
    #     return redirect("slug_field",kwargs={"slug":self.slug})

class Category(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)


class Expense(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="expenses")
    title = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
