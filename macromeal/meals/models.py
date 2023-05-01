import datetime

from django.db import models
from django.utils.translation import gettext_lazy as _

class Question(models.Model):
    question_text = models.CharField(max_length=200)

    def __str__(self):
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    searches = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text


class Meal(models.Model):
    meal_name = models.CharField(max_length=200)
    prep_time = models.FloatField()
    servings = models.IntegerField()
    ingredients = models.TextField(default='None')
    directions = models.TextField()
    image = models.TextField(default='None')

    class Meal_Type(models.TextChoices):
        BREAKFAST = 'B', _('Breakfast')
        LUNCH = 'L', _('Lunch')
        DINNER = 'D', _('Dinner')

    meal_type = models.CharField(
        max_length=2,
        choices=Meal_Type.choices,
        default=Meal_Type.DINNER,
    )

    def __str__(self):
        return self.meal_name

class Nutrition(models.Model):
    meal_name = models.ForeignKey(Meal, on_delete=models.CASCADE)
    nut_text = models.CharField(max_length=200)
    total_calories = models.IntegerField()
    fat_grams = models.IntegerField()
    carb_grams = models.IntegerField()
    protein_grams = models.IntegerField()


    def __str__(self):
        return f"text: {self.nut_text} calories: {self.total_calories}"




