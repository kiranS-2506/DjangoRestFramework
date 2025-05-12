from django.urls import path
from .views import *
urlpatterns = [
    path('students/',students),
    path('getstudent/<int:pk>',student_data),
]