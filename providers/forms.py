from django import forms
from .models import Provider

class ProviderForm(forms.ModelForm):
    Provider_UserId = forms.IntegerField(required=False,)

    class Meta:
        model = Provider
        fields = ['Provider_name','Provider_NIP','Provider_Phone']
        error_messages={

            'Provider_name':{
              'required':  "must be unique",
               'invalid': 'Name already in database'
            },
            'Provider_NIP':{
                'required': "must be unique",
                'invalid': 'Enter a valid NIP number(10 digits)'
            },
            'Provider_Phone': {
                'required': "must be unique",
                'invalid': 'Enter a valid phone number(7 to 16 digits)'
            }

        }