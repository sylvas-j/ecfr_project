from django.urls import path
from subjects import views
from .views import (
    SubjectCreateView, SubjectListView, SubjectUpdateView, SubjectDeleteView,
    SubjectRegisteredCreateView, SubjectRegisteredUpdateView, SubjectRegisteredDeleteView
)

app_name = 'subjects'

urlpatterns = [
    path('', SubjectListView.as_view(), name='subject_list'),
    path('courses/list/', views.SubjectList.subject_list, name='subject_user_list'),
    path('courses/list/<int:pk>/', views.SubjectList.subject_student_list, name='subject_student_list'),
    path('create/', SubjectCreateView.as_view(), name='create_subject'),
    path('update/<int:pk>/', SubjectUpdateView.as_view(), name='update_subject'),
    path('delete/<int:pk>/', SubjectDeleteView.as_view(), name='delete_subject'),

    # SubjectConbinations
    path('combination/create/', SubjectRegisteredCreateView.as_view(), name='create_subject_registered' ),
    path('registered/list/checker/', views.SubjectReg.subject_reg_status_checker, name='subject_reg_status_checker' ),
    path('registered/list/', views.SubjectReg.subject_reg_status, name='subject_registered_list' ),
    path('combination/update/<int:pk>', SubjectRegisteredUpdateView.as_view(), name='subject_registered_update' ),
    path('combination/delete/<int:pk>', SubjectRegisteredDeleteView.as_view(), name='subject_registered_delete' ),
    path('register/course/', views.subject_reg, name='subject_reg' ),
    path('registered/course/status/', views.subject_status_update, name='subject_status' ),
    

]