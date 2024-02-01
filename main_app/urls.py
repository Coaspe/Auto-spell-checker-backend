from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("download_exe/", views.download_exe, name="download_exe"),
    path("lastest_version/", views.lastest_version, name="lastest_version"),
]
