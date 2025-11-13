from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('students/', views.student_list_view, name='student_list'),  # Student list page
    path('recognition/<int:student_id>/', views.recognition_view, name='recognition'),  # Recognition page
    path('login/', auth_views.LoginView.as_view(template_name='recognition/login.html'), name='login'),  # Login view
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),  # Logout view
]
