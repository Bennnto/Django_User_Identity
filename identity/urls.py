from django.urls import path
from django.contrib.auth.views import PasswordResetCompleteView, PasswordResetView, PasswordResetConfirmView, PasswordResetDoneView
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('reset/', views.reset_password, name='reset'),
    path('reset_password/', PasswordResetView.as_view(template_name='password_reset.html'), name='password_reset'),
    path('reset_password_done/', PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),
    path('reset_password_confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset_password_complete/', PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete')
]