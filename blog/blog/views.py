from django.http import HttpResponse
from django.shortcuts import render


def test(request):
    return HttpResponse('tset页面')


def about(request):
    return render(request, 'about.html')


def index(request):
    return render(request, 'index.html')


def listpic(request):
    return render(request, 'listpic.html')


def newslistpic(request):
    return render(request, 'newslistpic.html')
