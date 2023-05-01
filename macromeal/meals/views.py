from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render  #Remove 404?
from django.urls import reverse
from django.views import generic
import random
from django.template import loader



from .models import Choice, Question, Meal, Nutrition

class IndexView(generic.ListView):
    template_name = 'meals/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Question.objects.filter()


class DetailView(generic.DetailView):
    model = Question
    template_name = 'meals/detail.html'


    def get_queryset(self):
        return Question.objects.filter()


class Controller:
    def generate_meals(self, type):
        menu = list(Meal.objects.filter(meal_type = type))
        daily_menu = random.sample(menu, 7)
        n = []
        for m in daily_menu:
            nutrition = list(Nutrition.objects.filter(meal_name = m.id))[0]
            print(nutrition)
            n.append(nutrition)


        print(MealPlan(daily_menu, n))
        return MealPlan(daily_menu, n)

class MealPlan:
    def __init__(self, meals, nutrition):
        self.meals = []
        self.meals.append(MealInfo(meals[0], "Monday", nutrition[0]))
        self.meals.append(MealInfo(meals[1], "Tuesday", nutrition[1]))
        self.meals.append(MealInfo(meals[2], "Wednesday", nutrition[2]))
        self.meals.append(MealInfo(meals[3], "Thursday", nutrition[3]))
        self.meals.append(MealInfo(meals[4], "Friday", nutrition[4]))
        self.meals.append(MealInfo(meals[5], "Saturday", nutrition[5]))
        self.meals.append(MealInfo(meals[6], "Sunday", nutrition[6]))

class MealInfo:
    def __init__(self, meal, dayofweek, nutrition):
        self.meal = meal
        self.dayofweek = dayofweek
        self.nutrition = nutrition

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'meals/results.html'


def search(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'meals/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        print("selected_choice is" + selected_choice.choice_text)
        controller = Controller()
        if(selected_choice.choice_text == "Breakfast"):
            my_meals = controller.generate_meals("B")
        elif selected_choice.choice_text == "Lunch":
            my_meals = controller.generate_meals("L")
        else:
            my_meals = controller.generate_meals("D")
        print("----------------------------------------------------")
        print(my_meals.meals[0].nutrition)
        print(my_meals.meals[0].nutrition.total_calories)
        template_name = loader.get_template('meals/results.html')
        context = {'meals_list':my_meals }

        return HttpResponse(template_name.render(context, request))






# from py2puml.py2puml import py2puml
#
# # outputs the PlantUML content in the terminal
# print(''.join(py2puml('py2puml/domain', 'py2puml.domain')))
#
# # writes the PlantUML content in a file
# with open('py2puml/domain.puml', 'w') as puml_file:
#     puml_file.writelines(py2puml('py2puml/domain', 'py2puml.domain'))









