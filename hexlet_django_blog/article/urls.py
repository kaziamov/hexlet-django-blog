from django.urls import path
from django.views.generic.base import TemplateView


from hexlet_django_blog.article import views


urlpatterns = [
    path('', views.RootView.as_view()),
    path('example', TemplateView.as_view(template_name='base.html')),
    path('template', views.RootView.as_view()),
]
