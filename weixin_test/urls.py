from django.urls import path
from . import views

urlpatterns = [
        path('', views.index, name='index'),
        path('create_menu/', views.create_menu, name='create_menu'),
        path('query_form/', views.query_form, name='query_form'),

]
