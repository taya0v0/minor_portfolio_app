from django.urls import path
from . import views

app_name = 'portfolio'

urlpatterns = [
    path('', views.home, name='home'),
    path('about-me/', views.about_me, name='about_me'),
    path('educational-program/', views.educational_program, name='educational_program'),
    path('educational-program/<int:pk>/', views.program_detail, name='program_detail'),
    path('management/', views.management, name='management'),
    path('classmates/', views.classmates, name='classmates'),
]
