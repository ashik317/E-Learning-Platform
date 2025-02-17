from django.urls import path
from . import views

app_name = 'courses'

urlpatterns = [
    path('mine/', views.ManageCourseListView.as_view(), name='manage-course-list'),
    path('create/', views.CourseCreateView.as_view(), name='create'),
    path('edit/<int:pk>/', views.CourseUpdateView.as_view(), name='course_edit'),
    path('delete/<int:pk>/', views.CourseDeleteView.as_view(), name='course_delete'),
]