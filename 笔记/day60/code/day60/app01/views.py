from django.shortcuts import render, HttpResponse, reverse


def index(request):
    url = reverse('app01:blogs',args=('2019','12'))
    print(url,type(url))

    url = reverse('app01:blogs', kwargs={'year':'2018','month':'10'})
    print(url, type(url))

    return render(request, 'index.html')


def blog(request, ):

    return HttpResponse('ok')


def blogs(request, year, month):
    print(year)
    print(month)
    return HttpResponse('o98k')


def home(request):
    return HttpResponse('app01 home')