from django.shortcuts import render
from .models import Dance
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from .forms import CustomLoginForm


def index(request):
    """
    View function for rendering the index page.
    """
    newest_dance = Dance.objects.all() 
    context = {'newest_dance': newest_dance}
    print(context)
    return render(request, 'dance/index.html', context)
    

class CustomLoginView(LoginView):
    template_name = 'dance/login.html'  # Path to your login template
    form_class = CustomLoginForm  # Use the custom login form
    redirect_authenticated_user = True  # Redirect already authenticated users

    def get_success_url(self):
        # Redirect to the admin page after successful login
        return reverse_lazy('admin:index')
        
def login(request):
    """
    View function for rendering the login page.
    """
    newest_event = Dance.objects.all() 
    context = {'newest_event': newest_event}
    print(context)
    return render(request, 'dance/login.html', context)