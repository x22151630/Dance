from django.shortcuts import render
from dance.models import Dance

def index(request):
    """
    View function for rendering the index page.
    """
    newest_dance = Dance.objects.order_by('title')[:15] #disable no-member
    context = {'newest_dance': newest_dance}
    return render(request, 'dance/index.html', context)