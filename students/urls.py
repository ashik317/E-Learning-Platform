from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.StudentRegistrationView.as_view(), name='student_registration'),
    path('enroll-course/', views.StudentEnrollCourseView.as_view(), name='student_enroll_course'),
    path('courses/', views.StudentCourseListView.as_view(), name='student_course_list'),
    path('course/<int:pk>/', views.StudentCourseDetailView.as_view(), name='student_course_detail'),
    path('course/<int:pk>/<module_id>/', views.StudentCourseDetailView.as_view(), name='student_course_module_detail'),
]