from django.urls import path
from . import views

urlpatterns = [
    path('properties/', views.property_list, name='property_list'),
    path('properties/<int:property_id>/', views.property_detail, name='property_detail'),
    path('tenants/', views.tenant_list, name='tenant_list'),
    path('tenants/<int:tenant_id>/', views.tenant_detail, name='tenant_detail'),
    path('', views.home, name='home'),
]
