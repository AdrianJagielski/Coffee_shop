from django.contrib import admin
from .models import Offer
from django.forms import TextInput, Textarea
from django.db import models
# Register your models here.

admin.site.register(Offer)