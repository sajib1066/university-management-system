from django.urls import path
from . import views

urlpatterns = [
    path('add-department/', views.add_department, name='add-department'),
    path('department-list/', views.department_list, name='department-list'),
    path('edit-department/<department_id>', views.edit_department, name='edit-department'),
    path('delete-department/<department_id>', views.delete_department, name='delete-department')
]
