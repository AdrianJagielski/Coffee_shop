from django.urls import path

from .views import providers
from .views import new_provider

from .views import delete_provider

urlpatterns = [

    path('',providers, name = "providers"),
    path('add_provider/',new_provider, name = "new_provider"),

    path('delete/<str:Provider_name>/', delete_provider,name="delete_provider"),


]