from django.urls import path
from . import views

urlpatterns = [
    path('', views.register_student, name='register'),
    path('success/<int:student_id>/', views.registration_success, name='registration_success'),
    path('students/', views.student_list, name='student_list'),
    path('student/<int:student_id>/', views.student_detail, name='student_detail'),
    path('student/<int:student_id>/edit/', views.edit_student, name='edit_student'),
    path('student/<int:student_id>/delete/', views.delete_student, name='delete_student'),
    path('search/', views.search_students, name='search_students'),
]