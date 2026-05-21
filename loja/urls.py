from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('sobre/', views.sobre, name = 'sobre'),
    path('produtos/', views.produtos, name = 'produtos'),
    path('test-upload/', views.test_upload, name='test_upload'),
]