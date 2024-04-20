from django.shortcuts import render, redirect
from dance.models import Dance
from django.contrib.auth.decorators import login_required
from .forms import UserContentForm
from .models import UserContent

def index(request):
    """
    View function for rendering the index page.
    """
    newest_dance = Dance.objects.order_by('title')[:15] #disable no-member
    context = {'newest_dance': newest_dance}
    return render(request, 'dance/index.html', context)
    

def upload(request):
    if request.method == 'POST':
        form = UserContentForm(request.POST, request.FILES)
        if form.is_valid():
            content = form.save(commit=False)
            content.user = request.user
            content.save()
            return redirect('dance/content.html')  # Redirect to content list view
    else:
        form = UserContentForm()
    return render(request, 'dance/upload.html', {'form': form})
    

def content(request):
        content = UserContent.objects.filter(user=request.user)
        return render(request, 'content.html', {'content': content})
