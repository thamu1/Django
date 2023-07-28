from django.contrib import admin
from django.urls import path , include
from . import views
from django.views.generic import TemplateView


urlpatterns = [
    path('', views.home),
    path('insert',views.insert,name='insert'),
    path('insert/tables',views.tables,name='tables'),
    path("insert/insert/metainsert", views.metainsert, name='metainsert'),
]