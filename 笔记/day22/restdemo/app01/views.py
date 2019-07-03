from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import BaseAuthentication

class MyAuthentication(object):
    def authenticate(self, request):
        """
        Authenticate the request and return a two-tuple of (user, token).
        """
        return (None,None)

class UserView(APIView):
    authentication_classes = [MyAuthentication]
    def get(self,request,*args,**kwargs):
        return Response({'k1':'v1','k2':'v2'})
