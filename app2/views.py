from django.shortcuts import render
from django.http import HttpResponse
from .models import Simple
# Create your views here.

def app2index(request):
    simple = Simple.objects.all()
    context = {
        'ss' : simple
    }
    return render(request, 'app2/index2.html', context)