from django.urls import path
from . import views


urlpatterns = [
    path('test', views.test, name='qr sert - test'),
    path('searhcsert', views.searchsert, name='searchsert'),
    path('sertif/<int:sertid>/', views.sertifpar, name='sertpar'),
]
