from django.contrib import admin
from django.urls import path
from django.urls import include
from . import views

app_name = "main"

urlpatterns = [
    path('',views.homepage, name="homepage"),
    path('wheels/',views.wheel_list, name="wheel_list"),
    path('wheelcreate/',views.wheelcreate, name="wheelcreate"),
    path('wheel/view/<int:pk>/',views.wheeldetail, name="wheeldetail"),
    path('wheel/edit/<int:pk>/',views.wheeledit, name="wheeledit"),
    path('wheel/edit-segment/<int:pk>/',views.edit_segment, name="edit_segment"),
    path('wheelfortune/',views.wheelfortune, name="wheelfortune"),
    path('admin/', admin.site.urls),
]
