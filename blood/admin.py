from django.contrib import admin 
from . models import Donors

# Register your models here.
@admin.register(Donors)
class DonorsAdmin(admin.ModelAdmin):
    list_display = ('id','donor_name', 'blood_group', 'donation_date', 'address')
    list_filter = ('blood_group',)
    search_fields = ('blood_group', 'address')
    ordering = ('donation_date',)
    