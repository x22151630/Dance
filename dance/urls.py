from django.urls import path
from . import views

app_name = 'dance'

urlpatterns = [
    path('', views.index, name='index'),
    path('upload/', views.upload, name='upload'),
    path('content/', views.content, name='content'),
]