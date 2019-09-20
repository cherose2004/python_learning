from django.shortcuts import render, HttpResponse
from app01 import models
import time
# Create your views here.
from django.views.decorators.cache import cache_page
from sg import pizza_done


# @cache_page(5)
def student_list(request, *args, **kwargs):
    students = models.Student.objects.all()
    pizza_done.send(sender='xxxxx', k1='xxxx')
    now = time.time()

    # 信号测试
    obj = models.Student.objects.get(id=1)
    obj.name = 'xxxxxxxx'
    obj.save()
    return render(request, 'student_list.html', {'students': students, 'now': now})


def index(request):
    # ret = models.Student.objects.all().defer('name')
    # for i in ret:
    #     print(i.classes_id)

    # ret = models.Student.objects.using('db2').all()
    #
    # models.Student.objects.using('db2').create(name='star', classes_id=1)

    # obj = models.Student.objects.using('db2').get(name='zhazha')
    # obj.name = 'star'
    # obj.save(using='default')

    # ret = models.Student.objects.all()
    # print(ret)
    #
    # obj = models.Student.objects.get(id=1)
    # obj.name = 'star'
    # obj.save()


    request.session['k1']= 'v1'

    from django.contrib.sessions.backends.db import SessionStore
    from django.contrib.sessions.models import Session
    ret = Session.objects.filter(session_key='ld5w252hf6b6pe72y2b0cmc9yh6kdyen').first()
    print(ret.session_data)

    ret = request.session.decode(ret.session_data)
    print(ret,type(ret))
    ret = request.session.encode(ret)
    print(ret,type(ret))


    return render(request, 'index.html')
