from django.urls import path
from .import views 

urlpatterns = [

    path('', views.plantList, name='plant-list'),

]