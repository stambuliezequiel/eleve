from django.shortcuts import render
from .models import SobreNosotras

def nosotras_view(request):
    info = SobreNosotras.objects.first() 
    return render(request, 'nosotras.html', {'nosotras': info})
