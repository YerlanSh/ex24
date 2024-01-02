from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import ClientsInfo

@login_required
def client_detail(request):
    client = ClientsInfo.objects.get(user=request.user)
    return render(request, 'clients/client_detail.html', {'client': client})
