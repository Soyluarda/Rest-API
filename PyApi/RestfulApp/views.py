from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json

from RestfulApp.models import Motors

def index(request):
    response = json.dumps([{}])
    return HttpResponse(response,content_type="text/json")

def get_moto(request,moto):
    if request.method == 'GET':
        try:
            motor = Motors.objects.get(name=moto)
            response = json.dumps([{'Motorcycle':motor.name, 'Speed':motor.speed}])
        except:
            response = json.dumps([{'Error':'No moto with this name'}])

        return HttpResponse(response,content_type='text/json')
