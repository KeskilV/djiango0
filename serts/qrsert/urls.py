from django.urls import path
from . import views


urlpatterns = [
    path('test', views.test, name='test2'),
    path('searhcsert', views.searchsert, name='searchsert'),
    path('sertif/<int:sertid>/', views.sertifpar, name='sertpar'),
    path('s/<slug:var_sert_slug>/', views.show_sert, name='pathsertslug'),
    path('vkl/<int:part>/<int:print>/', views.vkl, name='pathvkl'),
]
