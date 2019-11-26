from django.urls import path

from workbook_app import views

app_name = 'workbook_app'

urlpatterns = [
    path('books/', views.BookListView.as_view(), name='books'),
    path('keep_or_delete/<int:pk>/', views.KeepOrDeleteView.as_view(), name='keep_or_delete'),
]
