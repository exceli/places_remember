from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView


def home(request):
    return HttpResponse('Привет! Это стартовая страница с описанием сервиса!\n'
                        'Тут есть кнопки зарегистрироваться, и войти')


# class RememberView(ListView):
#     model = Model
#     template_name = 'remember/index.html'
#     context_object_name = 'remembers'
