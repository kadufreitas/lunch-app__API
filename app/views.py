from django.shortcuts import render
from django.http import HttpResponse


def view_client(request):
    return HttpResponse('VIEWCLIENT')
