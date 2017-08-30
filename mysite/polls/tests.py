import datetime
from django.utils import timezone
from django.test import TestCase

from .models import Question


class QuestionMethodTests(TestCase):
    def test_was_published_recently_with_future_question(self):

        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertEquals(future_question.was_published_recently(),False)
    def test_was_published_recently_with_recent_question(self):

        time = timezone.now() - datetime.timedelta(hours=1)
        recent_question = Question(pub_date=time)
        self.assertEquals(recent_question.was_published_recently(),True)
