from django.shortcuts import render
from django.http import HttpResponse
from .models import SertDiamonds1

def test(request):
    return HttpResponse('test -- qrset')

def searchsert(request):
    lensert = len(SertDiamonds1.objects.all())
    mainmenu = [{'title': 'тест', 'url_name': 'test'},
           ]
    context = {'lensert': lensert,
               'mainmenu': mainmenu,
               'title': 'поиск сертификата'}
    return render(request, 'qrsert/searchsert.html', context=context)

def sertifpar(request, sertid):
    diam = SertDiamonds1.objects.get(pk=sertid)
    context = {'diam': diam}
    return render(request, 'qrsert/sertif.html', context=context)

def nsert(request, nsert):
    sert = SertDiamonds1.objects.get(nsert=nsert)
    context = {'diam': diam}
    return render(request, 'qrsert/nsert.html', context=context)

