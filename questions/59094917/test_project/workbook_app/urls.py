from django.urls import path

from workbook_app import views

app_name = 'workbook_app'

urlpatterns = [
    path('employees/', views.Employees.as_view(), name='employees'),    
]
