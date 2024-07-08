from django.urls import path
from .views import upload_file, success, filter_data

urlpatterns = [
    path('upload/', upload_file, name='upload'),
    path('success/', success, name='success'),
    path('filter/', filter_data, name='filter'),
]