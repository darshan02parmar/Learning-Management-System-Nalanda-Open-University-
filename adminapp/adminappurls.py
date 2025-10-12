# adminapp/urls.py - Fixed version

from django.urls import path
from . import views, analytics_views
# from analytics_views import debug_analytics
app_name = "adminapp"

urlpatterns = [
    # Existing admin URLs
    path('adminhome/', views.adminhome, name='adminhome'),
    path('adminlogout/', views.adminlogout, name='adminlogout'),
    path('viewstudent/', views.viewstudent, name='viewstudent'),
    path('viewfeedback/', views.viewfeedback, name='viewfeedback'),
    path('viewenquiry/', views.viewenquiry, name='viewenquiry'),
    path('viewcomplain/', views.viewcomplain, name='viewcomplain'),
    path('studymaterial/', views.studymaterial, name='studymaterial'),
    path('move/', views.move, name='move'),
    path('viewmaterial/', views.viewmaterial, name='viewmaterial'),
    path('news/', views.news, name='news'),
    
    # Analytics URLs - FIXED
    path('dashboard/', analytics_views.admin_dashboard, name='admin_dashboard'),
    path('analytics-data/', analytics_views.analytics_data, name='analytics_data'),  # Fixed function name
    path('enrollment-analytics/', analytics_views.enrollment_analytics_view, name='enrollment_analytics'),
    path('course-analytics/', analytics_views.course_analytics_view, name='course_analytics'),
    path('performance-analytics/', analytics_views.performance_analytics_view, name='performance_analytics'),
    path('real-time-analytics/', analytics_views.real_time_analytics, name='real_time_analytics'),
    
    # File management system URLs - FIXED path syntax
    path('materials/', views.material_list, name='material_list'),
    path('course/<int:course_id>/materials/', views.material_list, name='course_materials'),
    path('materials/<int:material_id>/', views.material_detail, name='material_detail'),
    path('materials/<int:material_id>/preview/', views.material_preview, name='material_preview'),
    path('materials/<int:material_id>/download/', views.material_download, name='material_download'),
    path('materials/<int:material_id>/delete/', views.delete_material, name='delete_material'),
    
    # Material Creation URLs
    path('course/<int:course_id>/materials/create/', views.create_material, name='create_material'),
    path('materials/<int:material_id>/version/', views.create_material_version, name='create_material_version'),
    
    # Category Management URLs
    path('materials/categories/', views.material_categories, name='material_categories'),
    path('debug-analytics/', analytics_views.debug_analytics, name='debug_analytics'),

    # Assignment Management URLs
    path('assignments/', views.list_assignments, name='list_assignments'),
    path('assignments/create/', views.create_assignment, name='create_assignment'),
    path('assignments/<int:assignment_id>/submissions/', views.view_submissions, name='view_submissions'),
    path('submissions/<int:submission_id>/grade/', views.grade_submission, name='grade_submission'),
]