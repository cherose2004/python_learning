from django.conf.urls import url, include
from . import views

urlpatterns = [
    # url(r'^admin/', admin.site.urls),

    url(r'^index/$', views.index, name='index'),
    url(r'^home/$', views.home, name='home'),
    url(r'^blog/$', views.blog, name='blog'),
    url(r'^blog/(?P<year>[0-9]{4})/(?P<month>\d{2})$', views.blogs, name='blogs'),
    url(r'^xxxx/', include('app01.xx', namespace='xxx')),

]
