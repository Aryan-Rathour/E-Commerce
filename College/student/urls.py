from django.urls import path
from . import views
from .views import student_list,student_form,save_student,delete_record,Update_record

urlpatterns=[
    path('', views.student_list ,name='student-list'),
    path('student-form/',views.student_form,name='student-form'),
    path('save-student/',views.save_student,name='save-student'),
    path('delete-record/',views.delete_record,name='delete-record'),
    path('Update-record/<int:id>/',views.Update_record,name='Update-record'),
]