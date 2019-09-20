from django.conf.urls import url,include
from . import views

urlpatterns = [
    # url(r'^admin/', admin.site.urls),

    url(r'^index/$', views.index,name='index'),


]

#  /app01/xxxx/index/