from django.urls import path
from . import views

urlpatterns = [
    path('mine/', views.ManageCourseListView.as_view(), name='manage-course-list'),
    path('create/', views.CourseCreateView.as_view(), name='create'),
    path('edit/<int:pk>/', views.CourseUpdateView.as_view(), name='course_edit'),
    path('delete/<int:pk>/', views.CourseDeleteView.as_view(), name='course_delete'),
    path('module/<int:pk>/', views.CourseModuleUpdateView.as_view(), name='course_module_update'),
    path('module/<int:module_id>/content/<model_name>/<int:id>/', views.ContentCreateUpdateView.as_view(), name='module_content_update'),
    path('module/<int:module_id>/content/<model_name>/create/', views.ContentCreateUpdateView.as_view(), name='module_content_create'),
    path('content/<int:id>/delete/', views.ContentDeleteView.as_view(), name='module_content_delete'),
    path('module/<int:module_id>/contents/',views.ModuleContentListView.as_view(),name='module_content_list'),
    path('module/order/', views.ModuleOrderViews.as_view(), name='module_order'),
    path('content/order/', views.ContentOrderViews.as_view(), name='content_order'),
    path('subject/<slug:subject>/',views.CourseListViews.as_view(), name='course_list_subject'),
    path('<slug:slug>/', views.CourseDetailViews.as_view(), name='course_detail'),
]

