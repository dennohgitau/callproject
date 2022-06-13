from .views import Registration, UserNameValidation, EmailValidation, Verification, Login, Logout, \
    RequestPasswordResetEmail, CompletePasswordReset
from django.urls import path
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('register', Registration.as_view(), name='register'),
    path('login', Login.as_view(), name='login'),
    path('validate_username', csrf_exempt(UserNameValidation.as_view()), name='validate_username'),
    path('validate_email', csrf_exempt(EmailValidation.as_view()), name='validate_email'),
    path('activate/<uidb64>/<token>', Verification.as_view(), name='activate'),
    path('logout', Logout.as_view(), name='logout'),
    path('set_new_password/<uidb64>/<token>', CompletePasswordReset.as_view(), name='reset_user_password'),
    path('request-reset-link', RequestPasswordResetEmail.as_view(), name='request_password'),

]

