from django.urls import path
from .views import *

urlpatterns = [
    path('licences/', get_lincenc)
]
