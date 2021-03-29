from django.urls import path
from django.contrib.auth import views as auth_views
from .views import *
urlpatterns = [
    path('',home,name='home'),
    path('signup',signup,name='signup'),
    path('login',user_login,name='login'),
    path('logout',user_logout,name='logout'),

    path('reset_password/',
         auth_views.PasswordResetView.as_view(template_name='reset_password.html'),
         name="reset_password"),

    path('reset_password_sent/',
         auth_views.PasswordResetDoneView.as_view(template_name='reset_password_sent.html'),
         name="password_reset_done"),

    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'),
         name="password_reset_confirm"),

    path('reset_password_complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),
         name="password_reset_complete"),
]
