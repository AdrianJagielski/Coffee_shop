from django.db import models
from providers import models as provider
from django.core.validators import RegexValidator
# Create your models here.
class Offer(models.Model):

    provider_name = models.ForeignKey(provider.Provider,on_delete=models.CASCADE,db_column='Provider_name')
    Offer_Date_Published = models.DateTimeField(auto_now_add=True)

    Offer_Price = models.DecimalField(max_digits=9,decimal_places=2)
    Offer_Products = models.TextField(max_length=200)
    Offer_Realization_Time = models.IntegerField(validators=[RegexValidator(regex='^[0-9]{1,3}$', message='Atleast 1 and less than 3 digits')])
    Offer_Expiration_Date = models.DateField()

    def __str__(self):
        return self.provider_name.Provider_name
    def getnip(self):
        return self.provider_name.Provider_NIP
    def getphone(self):
        return self.provider_name.Provider_Phone