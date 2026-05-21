"""
URL configuration for loja_essente project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from django.http import JsonResponse
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
import os

def test_cloudinary(request):
    return JsonResponse({
        'CLOUD_NAME': os.environ.get('CLOUDINARY_CLOUD_NAME', 'NÃO DEFINIDO'),
        'API_KEY': os.environ.get('CLOUDINARY_API_KEY', 'NÃO DEFINIDO')[:5] + '...',
        'API_SECRET': '***' if os.environ.get('CLOUDINARY_API_SECRET') else 'NÃO DEFINIDO',
    })


urlpatterns = [
    path('test-cloud/', test_cloudinary, name='test_cloudinary'),
    path('admin/', admin.site.urls),
    path('', include('loja.urls')),
    path('carrinho/', include('carrinho.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)