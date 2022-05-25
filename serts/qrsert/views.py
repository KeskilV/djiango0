from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import SertDiamonds1,SertDiamonds

def vkl(request, print):
    diam = SertDiamonds1.objects.filter(print=print)
    slug = []
    for s in diam:
        slug.append(s.nsert)
    context = {'diam': diam,
               'slug': slug}
    return render(request, 'qrsert/vkl.html', context=context)


def test(request):
    return HttpResponse('test -- qrset')

def searchsert(request):
    lensert = len(SertDiamonds.objects.all())
    mainmenu = [{'title': 'тест', 'url_name': 'test2'},
           ]
    context = {'lensert': lensert,
               'mainmenu': mainmenu,
               'title': 'поиск сертификата'}
    return render(request, 'qrsert/searchsert.html', context=context)

def sertifpar(request, sertid):
    diam = get_object_or_404(SertDiamonds, pk=sertid)
    #diam = SertDiamonds1.objects.get(pk=sertid)
    context = {'diam': diam}
    return render(request, 'qrsert/sertif.html', context=context)

def show_sert(request, var_sert_slag):
    print('var_sert_slug_print:', var_sert_slag)
    diam = get_object_or_404(SertDiamonds, slag=var_sert_slag)
    context = {'diam': diam}
    return render(request, 'qrsert/sertif.html', context=context)

