"""
blog.test_post.py

The file that sets up all tests
for the post class in the blog app.
"""

import datetime as dt

import pytest
from model_bakery import baker
from freezegun import freeze_time

from blog.models import Post


# Mark this test module as requiring the database
pytestmark = pytest.mark.django_db


def test_published_posts_only_returns_those_with_published_status():
    """
    Creating a test to see that the published posts QuerySet
    only returns posts with the published status.
    """
    # Create published Post.
    published = baker.make('blog.Post', status=Post.PUBLISHED)
    # Create a draft Post.
    baker.make('blog.Post', status=Post.DRAFT)

    # We want the returned object to be 'published'.
    expected = [published]

    # Casting the result to a list so that the returned object can be properly compared.
    result = list(Post.objects.published())

    assert result == expected


def test_draft_posts_only_returns_those_with_draft_status():
    """
    A test to check that the draft posts QuerySet
    only returns posts with the draft status.
    """
    # Create a draft Post.
    draft = baker.make('blog.Post', status=Post.DRAFT)
    # Create a published Post.
    baker.make('blog.Post', status=Post.PUBLISHED)

    # We want the returned object to be 'draft'
    expected = [draft]

    # Casting the result to a list so that it can be compared properly
    result = list(Post.objects.draft())

    assert result == expected


def test_publish_sets_status_to_published():
    """
    Checking that when the publish() method is called
    the post status is set to published.
    """
    post = baker.make('blog.Post', status=Post.DRAFT)
    post.publish()

    assert post.status == Post.PUBLISHED


@freeze_time(dt.datetime(2030, 6, 1, 12, tzinfo=dt.timezone.utc))
def test_publish_sets_published_to_current_datetime():
    """
    A test to check that the publish() method
    properly sets the published date & time correctly.
    """
    # Create a new post, ensuring that the datetime isn't set.
    post = baker.make('blog.Post', published=None)
    post.publish()

    # Set the timezone to UTC (to match the tx_offset=0)
    assert post.published == dt.datetime(2030, 6, 1, 12, tzinfo=dt.timezone.utc)
