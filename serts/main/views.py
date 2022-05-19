from django.http import HttpResponse #, HttpResponseNotFound, Http404
from django.shortcuts import render
from .models import Diamonds4c


mainmenu = [{'title': 'Главная', 'url_name': 'home'},
            {'title': 'Наша миссия', 'url_name': 'about'},
            {'title': 'Сертификат соответствия', 'url_name': 'searchsert'},
            ]

def test(request):
    return HttpResponse('test')

def index(request):
    context = {'mainmenu': mainmenu,
              'title': 'главная страничка'}
    return render(request, 'main/index.html', context=context)


def about(request):
    context = {'mainmenu': mainmenu,
               'title': 'информация о нас'}
    return render(request, 'main/about.html', context=context)


def searchsert(request):
    lensert = len(Diamonds4c.objects.all())
    mainmenu = [{'title': 'тест', 'url_name': 'test'},
           ]
    context = {'lensert': lensert,
               'mainmenu': mainmenu,
               'title': 'поиск сертификата'}
    return render(request, 'main/searchsert.html', context=context)


def sertifpar(request,sertid):
    diam = Diamonds4c.objects.get(pk=sertid)
    context = {'diam': diam}
    return render(request, 'main/sertif.html', context=context)


def sertifpar0(request,sertid):
    diam = Diamonds4c.objects.get(pk=sertid)

    return render(request, 'main/sertif.html', {'diam':diam})




