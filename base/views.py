from django.shortcuts import render
from django.http import HttpResponse

def plantList(request):
    return HttpResponse('Plant Tracker!')

