"""ecfr_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
# from django.contrib.auth import views

from django.conf import settings
from django.conf.urls.static import static
from ecfr_admin import views

# admin.autodiscover()

urlpatterns = [
    path('ecfr/admin/', admin.site.urls),
    path('ecfr/', views.index, name='home'),
    path('ecfr/verify/email/', views.verify_email_view, name='verify_email'),
    path('ecfr/dashboard/', include('ecfr_admin.urls')),
    path('ecfr/subject/', include('subjects.urls')),
    path('ecfr/student/', include('students.urls')),
    path('ecfr/hod/', include('hod.urls')),
    # path('result/', include('results.urls')),
    path('ecfr/accounts/', include('django.contrib.auth.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

