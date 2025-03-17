from django.urls import path
from . import views

urlpatterns = [
    path('',views.students),
    path('entry/',views.student_entry),
    path('success/',views.success),
    path('details/<int:id>/',views.details,name='details')
]