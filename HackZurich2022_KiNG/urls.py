"""HackZurich2022_KiNG URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from HackZurich2022_KiNG.settings import STATIC_URL, STATICFILES_DIRS
from HackZurich2022_KiNG.views import dashboard as king_dashboard
from schindler.urls import urlpatterns as schindler_urlpatterns

urlpatterns = [
    path('', king_dashboard, name='HackZurich2022_KiNG'),

    path('admin/', admin.site.urls),
]

urlpatterns += static(STATIC_URL, document_root=STATICFILES_DIRS[0])
urlpatterns += schindler_urlpatterns
