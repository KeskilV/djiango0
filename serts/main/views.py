from django.shortcuts import render
from .models import Diamonds4c


def index(request):
    return render(request, 'main/index.html')


def about(request):
    return render(request, 'main/about.html')


def sertifpar(request,sertid):
    diam = Diamonds4c.objects.order_by('id')[:sertid]
    return render(request, 'main/sertif.html', {'diam':diam})


def sertif(request):
    diam = Diamonds4c.objects.order_by('-id')
    return render(request, 'main/sertif.html', {'diam':diam})

