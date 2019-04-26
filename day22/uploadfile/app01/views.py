from django.shortcuts import render,HttpResponse

def index(request):
    if request.method == 'GET':
        return render(request,'index.html')
    from django.core.files.uploadedfile import TemporaryUploadedFile
    file_object = request.FILES.get('avatar')
    with open(file_object.name,mode='wb') as f:
        for chunk in file_object:
            f.write(chunk)
    return HttpResponse('测试中')