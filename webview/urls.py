from django.conf.urls import include, url
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^all/', views.all, name='all'),
    url(r'^upload/', views.uploadCSV, name='upload'),
    # url(r'^download/', views.downloadCSV, name='download'),
]
