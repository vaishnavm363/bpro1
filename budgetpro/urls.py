
from django.conf.urls import url,include
from django.contrib import admin
from budget import views
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.project_list, name="list"),
    url(r'^add', views.ProjectCreateView.as_view(), name="add"),
    url(r'^(?P<slug>[-\w]+)/$', views.project_detail, name="slug_field"),

]
