from django.urls import path
from . import views

urlpatterns = [
    path('add-faculty/', views.add_faculty, name='add-faculty'),
    path('faculty-list/', views.faculty_list, name='faculty-list')
]