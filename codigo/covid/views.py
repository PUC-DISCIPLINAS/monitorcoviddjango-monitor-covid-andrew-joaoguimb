from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django import forms
from django.db.models import Sum
from django.views.decorators.csrf import csrf_exempt

from .models import Covid, Country

class CovidForm(forms.ModelForm):
    class Meta:
        model = Covid
        fields = ['deaths', 'cases', 'recovered', 'countryId']


# Create your views here.

def home_view(request, *args, **kwargs):
    return render(request, 'home.html',{})

@csrf_exempt
def create_admin_view(request, *args, **kwargs):
    form = CovidForm(request.POST or None)
    if form.is_valid():
        form.save()
    context = {
        'form': form
    }
    return render(request, 'admin.html', context)

def total_data_view(request, *args, **kwargs):
    context = {
        'totalDeaths': Covid.objects.aggregate(Sum('deaths'))['deaths__sum'],
        'totalRecovered': Covid.objects.aggregate(Sum('recovered'))['recovered__sum'],
        'totalCases': Covid.objects.aggregate(Sum('cases'))['cases__sum']
    }
    return render(request, 'home.html', context)
