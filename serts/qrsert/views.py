from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import SertDiamonds

def vkl(request, part, print):
    '''универсальная ЯГЛ'''
    diam = SertDiamonds.objects.filter(part=part).filter(print=print)
    context = {'diam': diam,
               }
    return render(request, 'qrsert/vkl.html', context=context)
    
    
def vklmark(request, part, print):
    '''для Маркова'''
    diam = SertDiamonds.objects.filter(part=part).filter(print=print)
    context = {'diam': diam,
               }
    return render(request, 'qrsert/vklmark.html', context=context)

def vklminih(request, part, print):
    '''универсальная мини горизонтальная'''
    diam = SertDiamonds.objects.filter(part=part).filter(print=print)
    context = {'diam': diam,
               }
    return render(request, 'qrsert/vklminih.html', context=context)

def vkluruu(request, part, print):
    '''уруу 15 ноября 2022'''
    diam = SertDiamonds.objects.filter(part=part).filter(print=print)
    context = {'diam': diam,
               }
    return render(request, 'qrsert/vkluruu.html', context=context)

def vklkdm(request, part, print):
    '''уруу 15 ноября 2022'''
    diam = SertDiamonds.objects.filter(part=part).filter(print=print)
    context = {'diam': diam,
               }
    return render(request, 'qrsert/vklkdm.html', context=context)

def vkl_a(request):#, part, print):
    #diam = SertDiamonds.objects.filter(part=part).filter(print=print)
    #context = {'diam': diam, }
    return render(request, 'qrsert/vkl_a.html')#, context=context)

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


def show_sert(request, var_sert_slug):
    #diam = SertDiamonds.objects.get(slug=var_sert_slug)
    diam = get_object_or_404(SertDiamonds, slug=var_sert_slug)
    context = {'diam': diam}
    return render(request, 'qrsert/sertif.html', context=context)

def show_sert0(request, var_sert_slug):
    #diam = SertDiamonds.objects.get(slug=var_sert_slug)
    diam = get_object_or_404(SertDiamonds, slug=var_sert_slug)
    context = {'diam': diam}
    return render(request, 'qrsert/sertif0.html', context=context)
