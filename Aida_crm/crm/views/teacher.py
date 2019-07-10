from django.views import View
from django.shortcuts import HttpResponse, reverse, redirect, render
from .base import BaseView
from crm import models
from crm.forms import ClassListForm, CourseRecordForm, StudyRecordForm
from utils.pagination import Pagination


class ClassList(BaseView):

    def get(self, request, *args, **kwargs):
        q = self.search(['campuses__name', 'start_date'])

        all_class = models.ClassList.objects.filter(q)
        page = Pagination(request.GET.get('page', 1), all_class.count(), request.GET.copy(), 3)

        return render(request, 'teacher/class_list.html',
                      {'all_class': all_class[page.start:page.end], 'page_html': page.page_html})


def class_change(request, pk=None):
    obj = models.ClassList.objects.filter(pk=pk).first()

    form_obj = ClassListForm(instance=obj)
    title = '编辑班级' if pk else '新增班级'
    if request.method == 'POST':
        form_obj = ClassListForm(request.POST, instance=obj)
        if form_obj.is_valid():
            form_obj.save()
            next = request.GET.get('next')
            if next:
                return redirect(next)

            return redirect(reverse('class_list'))

    return render(request, 'form.html', {'form_obj': form_obj, 'title': title})


class CourseRecordList(BaseView):

    def get(self, request, *args, class_id, **kwargs):
        # q = self.search(['campuses__name', 'start_date'])

        all_course_record = models.CourseRecord.objects.filter(re_class_id=class_id)
        page = Pagination(request.GET.get('page', 1), all_course_record.count(), request.GET.copy(), 3)

        return render(request, 'teacher/course_record_list.html',
                      {'all_course_record': all_course_record[page.start:page.end], 'page_html': page.page_html,
                       'class_id': class_id})

    def multi_init(self):
        # 批量创建学习记录
        course_record_ids = self.request.POST.getlist('pk')
        print(course_record_ids)
        # ['1', '2'] 课程记录的ID
        course_records = models.CourseRecord.objects.filter(pk__in=course_record_ids)
        for course_record in course_records:
            # 查找学生
            students = course_record.re_class.customer_set.all().filter(status='studying')
            # for student in students:
            #     models.StudyRecord.objects.create(course_record=course_record,student=student)

            study_record_list = []
            for student in students:
                study_record_list.append(models.StudyRecord(course_record=course_record, student=student))
            models.StudyRecord.objects.bulk_create(study_record_list)


def course_record_change(request, pk=None, class_id=None):
    obj = models.CourseRecord(re_class_id=class_id,
                              recorder=request.user_obj) if class_id else models.CourseRecord.objects.filter(
        pk=pk).first()

    form_obj = CourseRecordForm(instance=obj)
    title = '编辑课程记录' if pk else '新增课程记录'
    if request.method == 'POST':
        form_obj = CourseRecordForm(request.POST, instance=obj)
        if form_obj.is_valid():
            form_obj.save()
            next = request.GET.get('next')
            if next:
                return redirect(next)

            return redirect(reverse('course_record_list', args=(class_id,)))

    return render(request, 'form.html', {'form_obj': form_obj, 'title': title})


from django.forms import modelformset_factory


def study_record_list(request, course_record_id):
    ModelFormSet = modelformset_factory(models.StudyRecord, StudyRecordForm, extra=0)
    form_set_obj = ModelFormSet(queryset=models.StudyRecord.objects.filter(course_record_id=course_record_id))
    if request.method == 'POST':
        form_set_obj = ModelFormSet(queryset=models.StudyRecord.objects.filter(course_record_id=course_record_id),
                                    data=request.POST)
        if form_set_obj.is_valid():
            form_set_obj.save()
            # next = request.GET.get('next')
            # if next:
            #     return redirect(next)
            # return redirect(reverse('study_record', args=(course_record_id,)))
            return HttpResponse('保存成功')

    return render(request, 'teacher/study_record_list.html', {'form_set_obj': form_set_obj})
