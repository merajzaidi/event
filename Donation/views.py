from django.shortcuts import render , redirect
from django.contrib.auth.decorators import login_required
from .models import Donation
# Create your views here.
@login_required
def donate(request):
    if request.method == "POST":
        name = request.POST.get('name','')
        phone_no = request.POST.get('phone','')
        desc = request.POST.get('description','')
        amount = request.POST.get('amount','')
        obj = Donation(name=name,phone=phone_no, purpose=desc, amount=amount)
        obj.save()
        redirect('home')
    return render(request, 'Donation/donate.html')