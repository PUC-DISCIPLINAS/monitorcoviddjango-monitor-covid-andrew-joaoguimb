from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django import forms
from django.db.models import Sum
from django.views.decorators.csrf import csrf_exempt

from .models import Covid, Country

# Create your views here.

def home_view(request, *args, **kwargs):
    return render(request, 'dashboard/home.html',{})

def total_data_view(request, *args, **kwargs):
    all_countries = Country.objects.all()
    obj = {}

    for country in all_countries:
        totalDataByCountry = {
            'deaths': Covid.objects.filter(countryId=country.id).aggregate(Sum('deaths'))['deaths__sum'],
            'recovered': Covid.objects.filter(countryId=country.id).aggregate(Sum('recovered'))['recovered__sum'],
            'cases':  Covid.objects.filter(countryId=country.id).aggregate(Sum('cases'))['cases__sum']
        }

        print(totalDataByCountry)
        obj[f'{country.name}'] = totalDataByCountry

    print(obj)
    context = {
        'dataByCountry': obj,
        'totalDeaths': Covid.objects.aggregate(Sum('deaths'))['deaths__sum'],
        'totalRecovered': Covid.objects.aggregate(Sum('recovered'))['recovered__sum'],
        'totalCases': Covid.objects.aggregate(Sum('cases'))['cases__sum']
    }
    return render(request, 'dashboard/total_data.html', context)
