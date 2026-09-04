"""
URL configuration for dj_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
import json

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', include('main.urls')),
]

from django.http import HttpResponse

def handler404(request, exception=None):
    data = json.dumps({"error": "Not Found"}, separators=(",", ":"))
    return HttpResponse(
        data,
        content_type='application/json',
        status=404,
        reason="NOT FOUND"
    )

def handler500(request):
    data = json.dumps({"error": "Internal Server Error"}, separators=(",", ":"))
    return HttpResponse(
        data,
        content_type='application/json',  
        status=500,
        reason="INTERNAL SERVER ERROR"
    )