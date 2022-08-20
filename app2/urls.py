from .views import *
from django.urls import path

urlpatterns = [
    path('', app2index, name='app2index')
]