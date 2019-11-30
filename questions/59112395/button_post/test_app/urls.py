from django.urls import path

from test_app import views

app_name = 'test_app'

urlpatterns = [
    path('home/', views.HomePageView.as_view(), name='home'),
    path('about/', views.AboutPageView.as_view(), name='about'),
]
