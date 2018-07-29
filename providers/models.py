from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
class Provider(models.Model):
    Provider_name = models.CharField(max_length=200,unique=True,primary_key=True)
    Provider_NIP = models.IntegerField(validators=[RegexValidator(regex='^[0-9]{10}$', message='Length has to be 10')],unique=True)
    Provider_Phone = models.IntegerField(validators=[RegexValidator(regex='^[0-9]{7,16}$', message='Atleast 7 and less than 16 digits')],unique=True)
    Provider_UserId = models.IntegerField(null=True)

    def __str__(self):
        return self.Provider_name