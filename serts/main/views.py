from django.shortcuts import render
from .models import Diamonds4c


def index(request):
    return render(request, 'main/index.html')


def about(request):
    return render(request, 'main/about.html')


def sertifpar(request,sertid):
    diam = Diamonds4c.objects.get(pk=sertid)

    return render(request, 'main/sertif.html', {'diam':diam})


def sertif(request):
    lensert = len(Diamonds4c.objects.all())
    return render(request, 'main/sertif0.html', {'lensert': lensert})

