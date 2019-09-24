from django.contrib import admin
from django.urls import path
from django.urls import include
from . import views

app_name = "main"

urlpatterns = [
    path('',views.homepage, name="homepage"),
    path('wheelfortune/',views.wheelfortune, name="wheelfortune"),
    path('admin/', admin.site.urls),
]
