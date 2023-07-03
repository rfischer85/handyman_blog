from django.shortcuts import render
from django.db.models import Count

from . import models


def home(request):
    """
    The blog's homepage.
    """
    latest_posts = models.Post.objects.published().order_by('-published')[:3]
    topics = models.Topic.objects.annotate(post_count=Count('blog_posts')).order_by('-post_count')[:10]

    context = {
        'topics': topics,
        'latest_posts': latest_posts,
    }

    return render(request, 'blog/home.html', context)
