
from django.test import TestCase
from django.urls import reverse



class QuestionIndexViewTests(TestCase):
    def test_no_questions(self):
        """
        If no questions exist, an appropriate message is displayed.
        """
        response = self.client.get(reverse('meals:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No questions are available.")
        self.assertQuerysetEqual(response.context['latest_question_list'], [])


class MealsDetailViewTests(TestCase):
    def test_no_meals(self):
        """
        If no meals exist, an appropriate message is displayed.
        """
        response = self.client.get(reverse('meals:results'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No meals are available.")
        self.assertQuerysetEqual(response.context['meals_list'], [])

