from django.shortcuts import render
import secrets
import json
from django.http import JsonResponse
from zeep import Client

def home(request):
    return render(request, 'index.html')


def make_request(request):
    client = Client(wsdl="http://www.dneonline.com/calculator.asmx?wsdl")
    resp = client.service.Add(12,13)
    
    context = {
        'request_to': "http://www.dneonline.com/calculator.asmx?wsdl",
        'resp': resp,
        'token': secrets.token_hex(nbytes=16)
    }
    return render(request, 'index.html', context)
