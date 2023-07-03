"""
The test module for the Topic class.
"""
import pytest
from model_bakery import baker

from django.test import TestCase

from blog.models import Topic


# Mark this test module as requiring the database
pytestmark = pytest.mark.django_db


# def test_that_the_list_of_topics_is_pulled_from_the_models():
#     # Create topics
#     first_topic = baker.make('blog.Topic', name='test 1', slug='test-1')
#     second_topic = baker.make('blog.Topic', name='test 2', slug='test-2')
#
#     expected = [first_topic, second_topic]
#
#     assert list(Topic.objects.get_topics()) == expected
#
#
# def test_that_the_number_of_posts_per_topic_is_pulled(django_user_model):
#     # Create topics
#     first_topic = baker.make('blog.Topic', name='test 1', slug='test-1')
#     second_topic = baker.make('blog.Topic', name='test 2', slug='test-2')
#
#     # Create a User
#     user = baker.make(django_user_model)
#
#     # Create a post with first topic
#     first_post = baker.make('blog.Post', author=user)
#     first_post.topics.add(first_topic)
#
#     # Create two posts with the second topic
#     second_post = baker.make('blog.Post', author=user)
#     second_post.topics.add(second_topic)
#     third_post = baker.make('blog.Post', author=user)
#     third_post.topics.add(second_topic)
#
#     expected = [1, 2]
#
#     assert list(Topic.objects.get_topics()) == expected


class TopicTestCase(TestCase):
    # def setUpTestData(cls):
    #     # Creating an author for tests
    #     Post.objects.create(
    #         title='test',
    #         slug='test',
    #         author='rfisc',
    #     )
    def test_topic_post_count(self):
        # Create topics.
        first_topic = baker.make('blog.Topic', name='test 1', slug='test-1')
        second_topic = baker.make('blog.Topic', name='test 2', slug='test-2')

        # Create posts for the first topic
        for _ in range(7):
            first_topic.blog_posts.create()

        # Create posts for the second topic.
        for _ in range(3):
            second_topic.blog_posts.create(author='rfisc')

        # Get the topics including post counts
        topics = Topic.objects.annotate(post_count=Count('blog_posts')).order_by('-post_count')

        # Asserting the expected results
        self.assertEqual(topics[0].name, 'test 1')
        self.assertEqual(topics[0].post_count, 7)
        self.assertEqual(topics[1].name, 'test 2')
        self.assertEqual(topics[1].post_count, 3)