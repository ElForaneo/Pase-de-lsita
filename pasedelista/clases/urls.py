#clases urls.py

from django.urls import path
from .views import *

urlpatterns= [
    path('',home.as_view(), name="clases")
]