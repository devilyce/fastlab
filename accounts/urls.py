from django.contrib.auth import views as auth_views
from django.urls import path

from .views import *

urlpatterns = [
    path('register/', registerPage, name='register'),
    path('activate/<slug:uidb64>/<slug:token>/', activate, name='activate'),
    path('login/', loginPage, name='login'),
    path('logout/', logoutUser, name='logout'),
    path('user_profile/', user_profile.as_view(), name='user_profile'),

    path('password/', change_password.as_view(), name="change_password"),

    path('reset_password/', auth_views.PasswordResetView.as_view(template_name="accounts/reset_password.html"),
         name="reset_password"),

    path('reset_password_sent/',
         auth_views.PasswordResetDoneView.as_view(template_name="accounts/password_reset_sent.html"),
         name="password_reset_done"),

    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name="accounts/password_reset_form.html"),
         name="password_reset_confirm"),

    path('password_reset_complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name="accounts/password_reset_done.html"),
         name="password_reset_complete"),
]
