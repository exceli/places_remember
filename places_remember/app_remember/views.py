from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView


def home(request, *args, **kwargs):
    return render(request, 'remember/index.html')

