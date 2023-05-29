"""
handyman_blog/views.py
"""

from django.http import HttpResponse

def index(request):
    """function to return a message on an HTTP request"""
    return HttpResponse('Hello, world! This is my Handyman blog')
