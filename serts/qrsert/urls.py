from django.urls import path
from . import views


urlpatterns = [
    path('test', views.test, name='test2'),
    path('searhcsert', views.searchsert, name='searchsert'),
    path('sertif/<int:sertid>/', views.sertifpar, name='sertpar'),
    path('show_sert/<slug:var_sert_slag>/', views.show_sert, name='pathsertslug'),
    path('vkl/<int:print>/', views.vkl, name='pathvkl'),
]
