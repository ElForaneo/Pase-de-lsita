#clases urls.py

from django.urls import path
from .views import *

urlpatterns= [
    path('',clases.as_view(), name="clases")
]