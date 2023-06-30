import pytest
from model_bakery import baker

from blog.models import Topic


# Mark this test module as requiring the database
pytestmark = pytest.mark.django_db


def test_that_the_list_of_topics_is_pulled_from_the_models():
    # Create a topic
    first_topic = baker.make('blog.Topic', name='test 1', slug='test-1')
    second_topic = baker.make('blog.Topic', name='test 2', slug='test-2')

    expected = [first_topic, second_topic]

    assert list(Topic.objects.get_topics()) == expected
