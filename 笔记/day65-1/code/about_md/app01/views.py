from django.shortcuts import render, HttpResponse
from django.template.response import TemplateResponse


def index(request):
    print('index')

    # print(id(request))
    # ret = HttpResponse('ok')
    # print(id(ret))
    # return ret
    return TemplateResponse(request,'index.html',{'name':'alxe'})