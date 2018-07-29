"""Coffee_Shop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView
from signup import views as signup_views
from providers import views as providers_views
from offers import views as offers_views

urlpatterns = [
    path('login/', auth_views.login, name="login"),
    path('logout/', auth_views.logout, {'template_name': 'registration/logout.html'}, name='logout'),
    path('admin/', admin.site.urls),
    #path('home/', TemplateView.as_view(template_name='signup/home.html'), name='home'),
    path('signup/', signup_views.signup, name='signup'),
    path('',TemplateView.as_view(template_name='signup/home.html'), name='home'),
    path('new_offer/',offers_views.new_offer,name="new_offer"),
    path('providers/',include('providers.urls')),


    path('offers/',offers_views.offers,name="offers"),

]
