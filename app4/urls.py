from django.urls import path
from app4.views import *
app_name='app4'

urlpatterns=[
    path('rohit/',rohit,name='rohit'),
]