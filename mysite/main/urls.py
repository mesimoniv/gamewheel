from django.contrib import admin
from django.urls import path
from django.urls import include
from . import views

app_name = "main"

urlpatterns = [
    path('',views.homepage, name="homepage"),
    path('wheels/',views.wheel_list, name="wheel_list"),
    path('wheelcreate/',views.wheelcreate, name="wheelcreate"),
    path('wheel/<int:pk>/',views.wheeldetail, name="wheeldetail"),
    path('wheel/<int:pk>/edit',views.wheeledit, name="wheeledit"),
    path('wheelfortune/',views.wheelfortune, name="wheelfortune"),
    path('admin/', admin.site.urls),
]
