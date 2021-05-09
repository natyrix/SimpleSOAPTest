from django.shortcuts import render
from rest_framework import viewsets, views, status
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import AllowAny, IsAuthenticated
from zeep import Client

class Home(views.APIView):
    permission_classes = (AllowAny,)
    def get(self, request):
        client = Client(wsdl="http://www.dneonline.com/calculator.asmx?wsdl")
        resp = client.service.Add(12,13)
        user = User.objects.get(username='hp')
        tok = Token.objects.get(user=user)

        return Response({
            "request":{
                "Requested URL":"http://www.dneonline.com/calculator.asmx?wsdl",
                "Requested Method": "Requested Method: Add(intA: xsd:int, intB: xsd:int) -> AddResult: xsd:int",
                "Requested Method With Passed Arguments": "Requested Method: Add(12: xsd:int, 13: xsd:int) -> 25: xsd:int"
            },
            "response": {
                "Response": resp 
            },
        }, headers={
            "authentication": "Token {}".format(tok)
        })


