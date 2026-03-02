from django.shortcuts import render, redirect, get_list_or_404
from .models import Donors 
from django.db.models import Q 
from datetime import date, timedelta 


# Create your views here.
def home(request):
    return render(request, 'blood/index.html')

def register(request):
    
    if request.method == 'POST':
        name = request.POST.get('full_name')
        number = request.POST.get('number')
        gmail = request.POST.get('mail')
        blood = request.POST.get('blood_group')
        location = request.POST.get('location')
        last_date = request.POST.get('donation_date')
        
        Donors.objects.create(
            donor_name = name,
            contact = number,
            email = gmail,
            blood_group = blood,
            address = location,
            donation_date = last_date
        )
        
        return redirect(donors) 
        
    
    return render(request, 'blood/register.html')

def donors(request): 
    donor_list = Donors.objects.all()

    context_dict = {
        'donor': donor_list,   
    }

    return render(request, 'blood/donors.html', context_dict)

