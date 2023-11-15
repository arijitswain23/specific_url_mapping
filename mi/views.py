from django.shortcuts import render
from django.http import HttpResponse


def rohit(request):
    return render(request,'rohit.html')

def bumrha(request):
    return HttpResponse('<center><h1>Boom Boom Bumrha</h1></center>')


