from django.urls import path
from . import views


urlpatterns = [
    path('test', views.test, name='test2'),
    path('searchsert', views.searchsert, name='searchsert'),
    path('sertif/<int:sertid>/', views.sertifpar, name='sertpar'),
    path('s/<slug:var_sert_slug>/', views.show_sert, name='pathsertslug'),
    path('s0/<slug:var_sert_slug>/', views.show_sert0, name='pathsertslug0'),
    path('vkl/<int:part>/<int:print>/', views.vkl, name='pathvkl'),
    path('vkl_a', views.vkl_a, name='pathvkl_a'),
    path('vklmark/<int:part>/<int:print>/', views.vklmark, name='pathvklmark'),
    path('vklminih/<int:part>/<int:print>/', views.vklminih, name='pathvklminih'),
    path('vkluruu/<int:part>/<int:print>/', views.vkluruu, name='pathvkluruu'),
    path('vklkdm/<int:part>/<int:print>/', views.vklkdm, name='pathvklkdm'),
    ]
