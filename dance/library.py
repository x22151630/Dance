from django.contrib.auth import authenticate, login, logout
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserCreationForm, CustomUserChangeForm

class CustomLoginView(LoginView):
    template_name = 'login.html'  # Path to your login template
    form_class = AuthenticationForm
    redirect_authenticated_user = True

    def get_success_url(self):
        # Redirect to the admin page after successful login
        return reverse_lazy('admin:index')


class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('home')  # Redirect after logout


@login_required(login_url='login')
def dashboard_view(request):
    # This view is only accessible to logged-in users
    return render(request, 'dashboard.html', {})


def register_user(request):
    # View for user registration
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Automatically log in the user after registration
            login(request, user)
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})


def update_user(request):
    # View for updating user profile
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = CustomUserChangeForm(instance=request.user)
    return render(request, 'profile.html', {'form': form})


def custom_authenticate(username, password):
    # Custom authentication function
    user = authenticate(username=username, password=password)
    return user


def custom_login(request, user):
    # Custom login function
    login(request, user)


def custom_logout(request):
    # Custom logout function
    logout(request)


# Custom utility functions for user authentication can be added here

