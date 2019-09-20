from django.shortcuts import render, HttpResponse
from django.views import View
from app01 import models
import json


class BookListView(View):

    def get(self, request, *args, **kwargs):
        """ 获取所有的数据  返回所有的书籍数据 json格式"""
        # 1. 从数据库获取所有数据
        all_books = models.Book.objects.all().values('id', 'title', 'pub_date')  # [ {} ]
        # 2. 返回数据  json序列化
        return HttpResponse(json.dumps(list(all_books), ensure_ascii=False))

    def post(self, request, *args, **kwargs):
        """ 新增数据 返回新建的书籍数据 json格式"""
        pass

    def put(self, request, *args, **kwargs):
        """ 更新数据 返回更新后的书籍数据 json格式"""
        pass

    def delete(self, request, *args, **kwargs):
        """ 删除数据 返回空白  删除成功"""
        pass


from django.http.response import JsonResponse


class BookListView(View):

    def get(self, request, *args, **kwargs):
        """ 获取所有的数据  返回所有的书籍数据 json格式"""
        # 1. 从数据库获取所有数据
        all_books = models.Book.objects.all().values('id', 'title', 'pub_date')  # [ {} ]
        # 2. 返回数据  json序列化
        return JsonResponse(list(all_books), safe=False, json_dumps_params={'ensure_ascii': False})


from django.core import serializers


class BookListView(View):

    def get(self, request, *args, **kwargs):
        """ 获取所有的数据  返回所有的书籍数据 json格式"""
        # 1. 从数据库获取所有数据
        all_books = models.Book.objects.all()

        data = serializers.serialize('json', all_books)
        return HttpResponse(data)


from rest_framework.views import APIView
from rest_framework.response import Response


class BookListView(APIView):
    def get(self, request, *args, **kwargs):
        all_books = models.Book.objects.all().values('title', 'authors__name')
        print(all_books)
        return Response(all_books)


from app01.serializer import BookSerializer


class BookListView(APIView):
    def get(self, request, *args, **kwargs):
        all_books = models.Book.objects.all()
        ser_obj = BookSerializer(all_books, many=True)

        return Response(ser_obj.data)

    def post(self, request, *args, **kwargs):
        ser_obj = BookSerializer(data=request.data)
        if ser_obj.is_valid():
            ser_obj.save()
            return Response(ser_obj.data)
        return Response(ser_obj.errors)


class BookView(APIView):
    def get(self, request, pk, *args, **kwargs):
        book_obj = models.Book.objects.filter(pk=pk).first()
        ser_obj = BookSerializer(book_obj)

        return Response(ser_obj.data)

    def put(self, request, pk, *args, **kwargs):
        book_obj = models.Book.objects.filter(pk=pk).first()
        ser_obj = BookSerializer(book_obj, data=request.data, partial=True)
        if ser_obj.is_valid():
            ser_obj.save()
            return Response(ser_obj.data)
        return Response(ser_obj.errors)

    def delete(self, request, pk, *args, **kwargs):
        obj = models.Book.objects.filter(pk=pk).first()
        if obj:
            obj.delete()
            return Response({'msg': '删除成功'})
        return Response({'error': '数据不存在'})
