from django.contrib.auth import views as auth_views
from django.contrib import admin
from django.urls import path, include, reverse_lazy
from . import views

app_name = "main"

urlpatterns = [
    path('update_server/', views.update, name="update"),
    path('',views.homepage, name="homepage"),
    path('wheels/',views.wheel_list, name="wheel_list"),
    path('wheelcreate/',views.wheelcreate, name="wheelcreate"),
    path('wheel/view/<int:pk>/',views.wheeldetail, name="wheeldetail"),
    path('game/view/<int:pk>/',views.wheel_public_view, name="wheel_public_view"),
    path('wheel/edit/<int:pk>/',views.wheeledit, name="wheeledit"),
    path('wheel/edit-segment/<int:pk>/',views.edit_segment, name="edit_segment"),
    path('wheelfortune/',views.wheelfortune, name="wheelfortune"),
    path('register/',views.register, name="register"),
    path('login/',views.login_user, name="login"),
    path('logout/',views.logout_user, name="logout"),
    path('reset-password/', auth_views.PasswordResetView.as_view(
        template_name="main/registration/password_reset_form.html", 
        email_template_name="main/registration/password_reset_email.html",
        success_url=reverse_lazy('main:password_reset_done')), 
        name="password_reset"),
    path('reset-password-done/', auth_views.PasswordResetDoneView.as_view(
        template_name="main/registration/password_reset_done.html"), 
        name="password_reset_done"),
    path('reset-password/confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name="main/registration/password_reset_confirm.html", 
        success_url=reverse_lazy('main:password_reset_complete')), 
        name="password_reset_confirm"),
    path('reset-password/complete/', auth_views.PasswordResetCompleteView.as_view(
        template_name="main/registration/password_reset_complete.html"), 
        name="password_reset_complete"),
    path('admin/', admin.site.urls),
]

