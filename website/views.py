from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
def index_view(request):
    return HttpResponse('<h1>index</h1>')


def about_view(request):
    return HttpResponse('<h1>about</h1>')


def contact_view(request):
    return HttpResponse('<h1>contact</h1>')
