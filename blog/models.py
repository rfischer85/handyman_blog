"""
blog.models.py

The file defining the data models for the blog app.
"""
from django.conf import settings
from django.db import models
from django.utils import timezone
from django.db.models import Count


class TopicQuerySet(models.QuerySet):
    """
    Modifying the QuerySet class for Topic.
    """
    def get_topics(self):
        """
        Finding all topics with number of posts
        """
        return Topic.objects.annotate(Count('blog_posts')).values('name', 'blog_posts__count')


class Topic(models.Model):
    """
    The representation of a topic.
    """
    objects = TopicQuerySet.as_manager()
    name = models.CharField(
        max_length=50,
        unique=True,  # No duplicates
        null=False,
    )
    slug = models.SlugField(
        unique=True,
        null=False,
    )

    def __str__(self):
        """
        Customizing the str() for the Topic class.
        """
        return self.name

    class Meta:
        """A class to sort topics"""
        ordering = ['name']


class PostQuerySet(models.QuerySet):
    """
    Modified QuerySet class for Post.
    """
    def published(self):
        """
        Filtering a Post QuerySet by published status.
        """
        return self.filter(status=self.model.PUBLISHED)

    def draft(self):
        """
        Filtering a Post QuerySet by draft status.
        """
        return self.filter(status=self.model.DRAFT)


class Post(models.Model):
    """
    The representation of a blog post.
    """
    DRAFT = 'draft'
    PUBLISHED = 'published'
    STATUS_CHOICES = [
        (DRAFT, 'Draft'),
        (PUBLISHED, 'Published'),
    ]

    objects = PostQuerySet.as_manager()

    title = models.CharField(
        max_length=255,
        null=False,
    )
    slug = models.SlugField(
        null=False,
        help_text='The date & time this article was published',
        unique_for_date='published',  # Slug is unique for publication date
    )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,  # The Django auth user model
        on_delete=models.PROTECT,  # Prevents posts from being deleted
        related_name='blog_posts',
        null=False,
    )

    content = models.TextField()

    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default=DRAFT,
        help_text='Set to "published" to make this post publicly visible.',
        null=False,
    )

    published = models.DateTimeField(
        null=True,
        blank=True,
        help_text="The date & time this article was published",
    )

    created = models.DateTimeField(auto_now_add=True)  # Sets on create.
    updated = models.DateTimeField(auto_now=True)  # Updated on each save.

    topics = models.ManyToManyField(
        Topic,
        related_name='blog_posts'
    )

    comment = models.OneToOneField(
        'Comment',
        related_name='comments',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )

    class Meta:
        """
        A class to sort posts.
        """
        ordering = ['-created']

    def __str__(self):
        """
        Customizing the str() for the Post class.
        """
        return self.title

    def publish(self):
        """
        A method that sets a Posts status info to published.
        """
        self.status = self.PUBLISHED
        self.published = timezone.now()


class Comment(models.Model):
    """
    The representation of a post comment.
    """
    post = models.ForeignKey(
        Post,
        max_length=50,
        on_delete=models.CASCADE,
        related_name='comments',
        null=False,
        default=''
    )
    name = models.CharField(
        max_length=50,
        null=False,
        default=''
    )
    email = models.CharField(
        max_length=50,
        null=False,
        default=''
    )
    text = models.TextField(
        max_length=600,
        null=False,
        default=''
    )
    approved = models.BooleanField()  # Binary selection for approving comments
    created = models.DateTimeField(auto_now_add=True)  # Sets on create.
    updated = models.DateTimeField(auto_now=True)  # Updated on each save.

    class Meta:
        """
        A class to sort comments.
        """
        ordering = ['-created']

    def __str__(self):
        """
        Customizing the str() for the Comment class.
        """
        return self.text[:60]
