from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about-us', views.about, name='about'),
    path('searhcsert', views.searchsert, name='searchsert'),
    path('main/sertif/<int:sertid>/', views.sertifpar, name='sertpar'),
    path('main/test', views.test, name='test')
]
