from django.shortcuts import render
from . import models


def home(request):
    """
    The blog's homepage.
    """
    latest_posts = models.Post.objects.published().order_by('-published')[:3]
    context = {'latest_posts': latest_posts}
    return render(request, 'blog/home.html', context)
