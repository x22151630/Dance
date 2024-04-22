from django.urls import path
from . import views
from .views import CustomLoginView

app_name = 'dance'

urlpatterns = [
    path('', views.index, name='index'),
    path('login', CustomLoginView.as_view(), name='login'),
    
]