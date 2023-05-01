from django.contrib import admin

from .models import Question
from .models import Choice
from .models import Meal
from .models import Nutrition


admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Meal)
admin.site.register(Nutrition)

