from django.urls import path
from . import views

app_name = 'dance'

urlpatterns = [
    path('', views.index, name='index'),
   
]