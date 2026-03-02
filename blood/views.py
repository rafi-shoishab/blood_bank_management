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
    # query
    query = request.GET.get('q')
    if query:
        donor_list = Donors.objects.filter(
            blood_group = query
            )
    else:
        donor_list = Donors.objects.all()

    # eligible calculation
    today = date.today()
    
    for donor in donor_list:
        if donor.donation_date:
            donor.available_date = donor.donation_date + timedelta(days=90)
            donor.available = today >= donor.available_date
        else:
            donor.available = True
            donor.available_date = None 
        
    context_dict = {
        'donors': donor_list,
        'query' : query,
        }
    return render(request, 'blood/donors.html', context_dict) 