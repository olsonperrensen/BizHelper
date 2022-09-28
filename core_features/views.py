from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def homepage(req):
    return HttpResponse("<pre>You've landed on the homepage!</pre>")
