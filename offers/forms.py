from django import forms

from .models import Offer

class DateInput(forms.DateInput):
    input_type = 'date'

class OfferForm(forms.ModelForm):

    class Meta:
        model = Offer

        fields=['provider_name','Offer_Price','Offer_Products','Offer_Expiration_Date','Offer_Realization_Time']
        widgets = {'Offer_Expiration_Date':DateInput(),'Offer_Products':forms.Textarea(attrs={'rows':4,'cols':20,'style':'resize:none;'})}
