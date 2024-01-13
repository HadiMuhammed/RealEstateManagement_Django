from django.shortcuts import render
from .models import Property, Unit, Tenant, Lease

def property_list(request):
    properties = Property.objects.all()
    return render(request, 'property_list.html', {'properties': properties})

def property_detail(request, property_id):
    property = Property.objects.get(id=property_id)
    units = Unit.objects.filter(property=property)
    return render(request, 'property_detail.html', {'property': property, 'units': units})

def tenant_list(request):
    tenants = Tenant.objects.all()
    return render(request, 'tenant_list.html', {'tenants': tenants})

def tenant_detail(request, tenant_id):
    tenant = Tenant.objects.get(id=tenant_id)
    leases = Lease.objects.filter(tenant=tenant)
    return render(request, 'tenant_detail.html', {'tenant': tenant, 'leases': leases})

def home(request):
    return render(request, 'home.html')