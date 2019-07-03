from django.shortcuts import render, HttpResponse


def home(request):
    return HttpResponse('app02 home')
