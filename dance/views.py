from django.shortcuts import render
from .models import Dance

def index(request):
    """
    View function for rendering the index page.
    """
    newest_dance = Dance.objects.all() 
    context = {'newest_dance': newest_dance}
    print(context)
    return render(request, 'dance/index.html', context)
    

