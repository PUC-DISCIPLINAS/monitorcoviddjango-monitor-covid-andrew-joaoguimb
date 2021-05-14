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
    countriesName = []
    for country in all_countries:
        covid = Covid.objects.get(countryId=country.id)
        totalDataByCountry = {
            'deaths': covid.deaths,
            'recovered': covid.recovered,
            'cases': covid.cases
        }
        obj[f'{country.name}'] = totalDataByCountry
        countriesName.append(country.name)

    context = {
        'countries': countriesName,
        'dataByCountry': obj,
        'totalDeaths': Covid.objects.aggregate(Sum('deaths'))['deaths__sum'],
        'totalRecovered': Covid.objects.aggregate(Sum('recovered'))['recovered__sum'],
        'totalCases': Covid.objects.aggregate(Sum('cases'))['cases__sum']
    }
    return render(request, 'dashboard/total_data.html', context)
