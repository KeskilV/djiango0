from django.shortcuts import render
from .models import Diamonds4c


def index(request):
    return render(request, 'main/index.html')


def about(request):
    return render(request, 'main/about.html')


def sertif(request):
    diam = Diamonds4c.objects.order_by('-id')[:1]
    return render(request, 'main/sertif.html', {'diam':diam})
