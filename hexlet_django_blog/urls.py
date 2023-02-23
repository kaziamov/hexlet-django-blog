from django.contrib import admin
from django.urls import path, include
from hexlet_django_blog import views


urlpatterns = [
    path('', views.index),
    path('about/', views.about),
    path('article/', include('hexlet_django_blog.article.urls')),
    path('admin/', admin.site.urls),
]
