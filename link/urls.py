from django.urls import path
from .views import *

urlpatterns = [
    path('calendar/<str:slug>', calendar, name="calendar"),
    path('<str:slug>/<str:date>', home, name="home"),
    
]