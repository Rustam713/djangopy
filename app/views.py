from django.shortcuts import render
from .models import New
# Create your views here.
def index(request):
    new = New.objects.all()
    return render(request, 'index.html', {'muchacha' : new})