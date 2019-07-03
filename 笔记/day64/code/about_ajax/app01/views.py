from django.shortcuts import render, HttpResponse


def index(request):
    if request.method == 'POST':
        i1 = request.POST.get('i1')
        i2 = request.POST.get('i2')
        i3 = int(i1) + int(i2)
        return render(request, 'index.html', {'i1': i1, 'i2': i2, 'i3': i3})

    return render(request, 'index.html')


import time


def calc(request):
    a = request.POST.get('a')
    b = request.POST.get('b')
    c = int(a) + int(b)
    return HttpResponse(c)


def calc2(request):
    a = request.POST.get('a')
    b = request.POST.get('b')
    c = int(a) + int(b)
    return HttpResponse(c)

import json
def test(request):
    print(request.POST)
    ret = request.POST.get('hobby')
    print(ret)
    ret = json.loads(ret)
    print(ret,type(ret))
    return HttpResponse('ok')


def upload(request):
    print(request.FILES)
    print(request.POST)

    return render(request,'upload.html')