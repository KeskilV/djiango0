from django.http import HttpResponse #, HttpResponseNotFound, Http404
from django.shortcuts import render
from .models import Diamonds4c

#1111
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






