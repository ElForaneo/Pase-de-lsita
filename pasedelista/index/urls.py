#index urls.py

from django.urls import path
from .views import *

urlpatterns= [
    path('',home.as_view(), name="home"),
    path('clasesadd/Add', clasesadd.as_view(), name="clasesadd"),
    path('clasesadd/<int:id>/', clasesUpdate.as_view(), name="clasesupdate")
]