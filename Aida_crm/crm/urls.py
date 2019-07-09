from django.conf.urls import url
from crm import views

urlpatterns = [
    url(r'^login/', views.login, name='login'),
    url(r'^reg/', views.reg, name='reg'),
    url(r'^index/', views.index, name='index'),
    url(r'^customer_list/', views.CustomerList.as_view(), name='customer_list'),
    url(r'^my_customer/', views.CustomerList.as_view(), name='my_customer'),

    # url(r'^customer_list/', views.customer_list, name='customer_list'),
    # url(r'^my_customer/', views.customer_list, name='my_customer'),
    # url(r'^add_customer/', views.add_customer, name='add_customer'),
    # url(r'^edit_customer/(\d+)/', views.edit_customer, name='edit_customer'),

    url(r'^add_customer/', views.customer_change, name='add_customer'),
    url(r'^edit_customer/(\d+)/', views.customer_change, name='edit_customer'),

    url(r'^consult_list/$', views.ConsultList.as_view(), name='consult_list'),
    url(r'^consult_list/(\d+)/$', views.ConsultList.as_view(), name='one_consult_list'),

    url(r'^add_consult/$', views.consult_change, name='add_consult'),
    url(r'^edit_consult/(\d+)/$', views.consult_change, name='edit_consult'),

    # url(r'^user_list/', views.user_list, name='user_list'),

]
