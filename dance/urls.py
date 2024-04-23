from django.urls import path, include
from . import views
from .views import CustomLoginView

app_name = 'dance'

urlpatterns = [
    path('index', views.index, name='index'),
    #path("home",login),
    path('', views.login_user, name='login'),

    
]