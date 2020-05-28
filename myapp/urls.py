from django.urls import path
from . import views

urlpatterns = [
    path('myapp/', views.index),
    path('student/', views.student),
    path('student_update/<int:id>', views.student_update),
    path('update/<int:id>', views.update),
    path('delete/<int:id>', views.delete),
    path('course/', views.course),
    path('course_update/<int:id>', views.course_update),
    path('update_crs/<int:id>', views.update_crs),
    path('delete_crs/<int:id>', views.delete_crs),

]