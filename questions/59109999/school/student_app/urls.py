from django.urls import path

from student_app import views

app_name = 'student_app'

urlpatterns = [
    path('student/', views.student, name='student'),
]
