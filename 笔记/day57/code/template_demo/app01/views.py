from django.shortcuts import render
import datetime

class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def talk(self):
        return '咱也不知道，咱也不敢问'

    def __str__(self):
        return " < Person obj : {}-{}> ".format(self.name, self.age)


def template_test(request):
    string = 'alexdasb'
    age = 73
    hobby = ['唱', '跳', 'rap', '篮球']
    dic = {
        'name': 'alex',
        'age': age,
        'hobby': hobby,
        'keys': 'xxxxx'
    }
    person_obj = Person('taibai', 84)
    return render(request,
                  'template_test.html',
                  {
                      'string': string,
                      'age': age,
                      'hobby': hobby,
                      'dic': dic,
                      'person_obj': person_obj,
                      'kong': None,
                      'filesize':1*1024*1024*1024*1024*1024*1024,
                      'long_str':"You have 13 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.Run 'python manage.py migrate' to apply them.",
                      'long':'咱也不知道，咱也不敢问',
                      'now':datetime.datetime.now(),
                      'a_html':'<a href="https://www.cnblogs.com/maple-shaw/articles/9333821.html#commentform">点击按钮</a>',
                      'js':"""
                      <script>

                        for (var i = 0; i < 5; i++) {
                        alert('11111')
                        }
                        
                        </script>"""

                  })
