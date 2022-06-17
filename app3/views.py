from email.policy import HTTP
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def hardhik(request):
    return HttpResponse('he is a great player')