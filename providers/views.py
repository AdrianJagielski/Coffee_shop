from .models import Provider
from .forms import ProviderForm
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Q
# Create your views here.


@login_required
def providers(request):

    providers_list = Provider.objects.all()
    print(providers_list)
    query = request.GET.get("q")
    if query:
        providers_list = providers_list.filter(
            Q(Provider_name__icontains=query) |
            Q(Provider_NIP__icontains=query)|
            Q(Provider_Phone__icontains=query)

        )
    return render(request, 'providers/providers.html',{'Providers': providers_list})

@login_required
def new_provider(request):
    form = ProviderForm( request.POST or None )
    userid = request.user.id

    if form.is_valid():
        obj = form.save(commit=False)
        obj.Provider_UserId = userid
        form.save()
        return redirect('providers')
    else:

        return render(request, "providers/providers_form.html",
                          {
                              'form': form,

                          }
                          )

@login_required
def delete_provider(request, Provider_name):
    provider_list = Provider.objects.get(Provider_name=Provider_name)
    if request.method == 'POST':
        provider_list.delete()
        return redirect('providers')
    return render(request, 'providers/confrim.html', {'Providers': provider_list})

