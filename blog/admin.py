"""
blog.admin.py

Django Admin for the 'blog' app.
Exposing models to admin.
"""
from django.contrib import admin
from . import models


class CommentInline(admin.StackedInline):
    """
    Configuring the inline post comments.
    """
    model = models.Comment
    extra = 0


class PostAdmin(admin.ModelAdmin):
    """
    Configuring the Post class.
    """
    list_display = (
        'title',
        'author',
        'created',
        'updated',
    )

    list_filter = (
        'status',
        'topics',
    )

    search_fields = (
        'title',
        'author__username',
        'author__first_name',
        'author__last_name',
    )

    inlines = [
        CommentInline,
    ]

    prepopulated_fields = {'slug': ('title',)}


@admin.register(models.Topic)
class TopicAdmin(admin.ModelAdmin):
    """
    Configuring the Topics class.
    """
    list_display = (
        'name',
        'slug',
    )
    prepopulated_fields = {'slug': ('name',)}


@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin):
    """
    Configuring the Comments class.
    """
    list_display = (
        'name',
        'post',
        'updated',
        'created',
    )

    list_filter = (
        'approved',
    )

    search_fields = (
        'name',
        'email',
        'post',
    )


admin.site.register(models.Post, PostAdmin)
