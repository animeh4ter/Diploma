from django.urls import path
from . import views

urlpatterns = [
    path('profile/', views.profile, name='profile'),
    path('login/', views.login_register, name='login-register'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('edit-acc-info/', views.edit_account_info, name='edit-account'),
]