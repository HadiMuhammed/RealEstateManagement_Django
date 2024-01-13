from django.db import models

class Property(models.Model):
    class Meta:
        verbose_name_plural = "Properties"
    name = models.CharField(max_length=255)
    address = models.TextField()
    location = models.CharField(max_length=255)
    features = models.TextField()

class Unit(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    rent_cost = models.DecimalField(max_digits=10, decimal_places=2)
    bedroom_type = models.CharField(max_length=10, choices=[('1BHK', '1BHK'), ('2BHK', '2BHK'), ('3BHK', '3BHK'), ('4BHK', '4BHK')])

class Tenant(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()
    document_proofs = models.TextField()

class Lease(models.Model):
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    agreement_end_date = models.DateField()
    monthly_rent_date = models.IntegerField()
