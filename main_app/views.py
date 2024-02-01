from django.http import HttpResponse, HttpRequest
import os


def index(request: HttpRequest):
    return HttpResponse("Hello, this is a single app Django project.")


def lastest_version(request: HttpRequest):
    return HttpResponse(os.getenv("LASTEST_VERSION"))

def download_exe(request: HttpRequest):
    pass
