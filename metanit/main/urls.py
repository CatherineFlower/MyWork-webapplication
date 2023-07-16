from django.urls import path
from . import views

urlpatterns = [
    path('', views.reg, name='reg'),
    path('home', views.home, name='home'),
    path('loading', views.load, name='load'),
]



