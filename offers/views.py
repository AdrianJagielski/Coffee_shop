from django.shortcuts import render,redirect
from .models import Offer
import datetime
from .forms import OfferForm
from django.contrib.auth.decorators import login_required
from django.db.models import Q
# Create your views here.

@login_required()
def offers(request):

    Offers = Offer.objects.filter(Offer_Expiration_Date__gt=datetime.datetime.now().date())
    phone = Offer.getphone
    nip = Offer.getnip
    flag=True

    Offers.order_by('-date')
    query = request.GET.get("q")
    if query:
        Offers = Offers.filter(
            Q(provider_name__Provider_name__icontains=query)|
            Q(Offer_Products__icontains=query)|
            Q(Offer_Realization_Time__icontains=query)|
            Q(Offer_Price__icontains=query)|
            Q(provider_name__Provider_Phone__icontains=query)|
            Q(provider_name__Provider_NIP__icontains=query)

            )
    if (request.GET.get('mybtn')):
        Offers = Offer.objects.all()
        flag = True
    if (request.GET.get('mybtn1')):
        Offers = Offer.objects.filter(Offer_Expiration_Date__gt=datetime.datetime.now().date())
        flag = False

    if (flag==True):

        if (request.GET.get('mybtn2')):
            Offers = Offer.objects.filter(Offer_Expiration_Date__gt=datetime.datetime.now().date()).order_by('Offer_Price')
        if (request.GET.get('mybtn3')):
            Offers = Offer.objects.filter(Offer_Expiration_Date__gt=datetime.datetime.now().date()).order_by('-Offer_Price')
        if (request.GET.get('mybtn4')):
            Offers = Offer.objects.filter(Offer_Expiration_Date__gt=datetime.datetime.now().date()).order_by('provider_name')
        if (request.GET.get('mybtn5')):
            Offers = Offer.objects.filter(Offer_Expiration_Date__gt=datetime.datetime.now().date()).order_by('-provider_name')

    elif (flag==False):

        if (request.GET.get('mybtn2')):
            Offers = Offer.objects.order_by('Offer_Price')
        if (request.GET.get('mybtn3')):
            Offers = Offer.objects.order_by('-Offer_Price')
        if (request.GET.get('mybtn4')):
            Offers = Offer.objects.order_by('provider_name')
        if (request.GET.get('mybtn5')):
            Offers = Offer.objects.order_by('-provider_name')

    return render(request, 'offers/offers.html',{'Offers': Offers ,'phone':phone,'nip':nip })
@login_required()
def new_offer(request):
    form = OfferForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('offers')
    else:
        return render(request,'offers/offer_form.html',{'form': form} )