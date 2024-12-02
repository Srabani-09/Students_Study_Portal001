
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from dashboard import views as dash_view
from django.contrib.auth.views import LoginView,PasswordResetView,PasswordResetDoneView,PasswordResetConfirmView,PasswordResetCompleteView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('dashboard.urls')),
    path('register/',dash_view.register,name="register"),
    path('login/',LoginView.as_view(template_name="dashboard/login.html"),name="login"),
    path('logout/',dash_view.custom_logout, name="logout"),
    path('profile/',dash_view.profile,name="profile"),
    
    path('password_reset/',PasswordResetView.as_view(template_name='dashboard/password_reset.html'),name="password_reset"),
    path('password_reset_done/',PasswordResetDoneView.as_view(template_name='dashboard/password_reset_done.html'),name="password_reset_done"),
    path('password_reset_confirm/<uidb64>/<token>/',PasswordResetConfirmView.as_view(template_name='dashboard/password_reset_confirm.html'),name="password_reset_confirm"),
    path('reset/done/',PasswordResetCompleteView.as_view(template_name='dashboard/password_reset_complete.html'),name="password_reset_complete")
]