from django.shortcuts import render
from django.http import HttpResponse
from todo.models import Item


def home(request):
    response = HttpResponse("Text only, please.", content_type="text/plain")
    return response
