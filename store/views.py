from django.shortcuts import render
from django.http import HttpResponse
from .models import Specifications


def home(request):
    obj = Specifications.objects.all()
    print(obj)
    return render(request, "home.html", {'obj': obj})


def add(request):
    global checked_instances
    if request.method == 'POST':
        checked_data = request.POST.getlist('list_check')
        checked_instances = Specifications.objects.filter(id__in=checked_data)

    return render(request, "cart.html", {'checked_instances': checked_instances})


