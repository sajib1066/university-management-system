from django.urls import path
from . import views

urlpatterns = [
    path('add-department/', views.add_department, name='add-department'),
    path('department-list/', views.department_list, name='department-list')
]
