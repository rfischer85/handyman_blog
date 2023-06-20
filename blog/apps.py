"""
blog.apps.py

Listing defined apps.
"""
from django.apps import AppConfig


class BlogConfig(AppConfig):
    """
    Configuring the 'blog' app.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog'
