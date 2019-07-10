from django.conf.urls import url
from crm.views import auth,consultant,teacher

urlpatterns = [
    url(r'^login/', auth.login, name='login'),
    url(r'^reg/', auth.reg, name='reg'),
    url(r'^index/', consultant.index, name='index'),
    url(r'^customer_list/', consultant.CustomerList.as_view(), name='customer_list'),
    url(r'^my_customer/', consultant.CustomerList.as_view(), name='my_customer'),

    # url(r'^customer_list/', consultant.customer_list, name='customer_list'),
    # url(r'^my_customer/', consultant.customer_list, name='my_customer'),
    # url(r'^add_customer/', consultant.add_customer, name='add_customer'),
    # url(r'^edit_customer/(\d+)/', consultant.edit_customer, name='edit_customer'),

    url(r'^add_customer/', consultant.customer_change, name='add_customer'),
    url(r'^edit_customer/(\d+)/', consultant.customer_change, name='edit_customer'),

    url(r'^consult_list/$', consultant.ConsultList.as_view(), name='consult_list'),
    url(r'^consult_list/(\d+)/$', consultant.ConsultList.as_view(), name='one_consult_list'),

    url(r'^add_consult/(?P<customer_id>\d+)/$', consultant.consult_change, name='add_consult'),
    url(r'^edit_consult/(\d+)/$', consultant.consult_change, name='edit_consult'),

    # url(r'^user_list/', consultant.user_list, name='user_list'),

    # 展示一个销售填写报名记录
    url(r'^enrollment_list/$', consultant.EnrollmentList.as_view(), name='enrollment_list'),
    # 展示一个客户报名记录
    url(r'^enrollment_list/(?P<customer_id>\d+)/$', consultant.EnrollmentList.as_view(), name='one_enrollment_list'),

    # 添加报名表
    url(r'^add_enrollment/(?P<customer_id>\d+)$', consultant.enrollment_change, name='add_enrollment'),
    # 编辑报名表
    url(r'^edit_enrollment/(\d+)/$', consultant.enrollment_change, name='edit_enrollment'),


    # 展示班级
    url(r'^class_list/$', teacher.ClassList.as_view(), name='class_list'),
    # 添加班级
    url(r'^add_class/$', teacher.class_change, name='add_class'),
    # 编辑班级
    url(r'^edit_class/(\d+)$', teacher.class_change, name='edit_class'),
    # 展示课程记录
    url(r'^course_record_list/(?P<class_id>\d+)$', teacher.CourseRecordList.as_view(), name='course_record_list'),

    # 添加课程记录
    url(r'^add_course_record/(?P<class_id>\d+)$', teacher.course_record_change, name='add_course_record'),
    # 编辑课程记录
    url(r'^edit_course_record/(?P<pk>\d+)$', teacher.course_record_change, name='edit_course_record'),
    # 展示学习记录
    url(r'^study_record/(?P<course_record_id>\d+)$', teacher.study_record_list, name='study_record'),

]
