from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
#from .models import SertDiamonds

def vkl(request, part, print):
    diam = SertDiamonds.objects.filter(part=part).filter(print=print)
    context = {'diam': diam,
               }
    return render(request, 'qrsert/vkl.html', context=context)

def vkl_a(request):#, part, print):
    #diam = SertDiamonds.objects.filter(part=part).filter(print=print)
    #context = {'diam': diam, }
    return render(request, 'qrsert/vkl_a.html')#, context=context)

def test(request):
    return HttpResponse('test -- qrset')
    
def home(request):
    return HttpResponse('welcome to YGL Якутский гемцентр')
    

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

