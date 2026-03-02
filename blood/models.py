from django.db import models

# Create your models here.
class Donors(models.Model):
    donor_name = models.CharField(max_length=100)
    contact = models.CharField(max_length=14)
    email = models.EmailField()
    blood_group = models.CharField(max_length=3)
    address = models.TextField()
    donation_date = models.DateField(null=True, blank=True)
