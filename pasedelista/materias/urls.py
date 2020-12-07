#index urls.py

from django.urls import path
from .views import *

urlpatterns= [
    path('',materias.as_view(), name="materias")
]