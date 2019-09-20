from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView,ListAPIView,CreateAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from app01 import models
# class UserView(View):
#
#     def get(self,request,*args,**kwargs):
#         return JsonResponse({'k1':123})

# class UserView(APIView): # 10个功能
#     def get(self,request,*args,**kwargs):
#         data = models.User.objects.all()
#         # return JsonResponse({'k1':123})
#         return Response({'k1':123})

#
# class UserView(GenericAPIView): # 5个功能(鸡肋）
#     queryset = models.User.objects
#     # queryset = None
#     def get(self,request,*args,**kwargs):
#         # return JsonResponse({'k1':123})
#         data = self.get_queryset()
#         return Response({'k1':123})


from rest_framework.serializers import ModelSerializer
class UserModelSerializer(ModelSerializer):
    class Meta:
        model = models.User
        fields = "__all__"

# class UserView(CreateAPIView):
#     queryset = models.User.objects
#     serializer_class = UserModelSerializer


class UserView(ModelViewSet):
    queryset = models.User.objects
    serializer_class = UserModelSerializer