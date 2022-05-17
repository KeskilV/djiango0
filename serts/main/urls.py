from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about-us', views.about, name='about'),
    path('sertif', views.sertif, name='sert'),
    path('sertif/<int:sertid>/', views.sertifpar, name='sertpar'),
]
