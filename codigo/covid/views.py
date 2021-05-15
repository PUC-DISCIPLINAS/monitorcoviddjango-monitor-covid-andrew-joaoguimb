from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django import forms
from django.db.models import Sum
from django.views.decorators.csrf import csrf_exempt

from .models import Covid, Country

# Create your views here.
all_countries = Country.objects.all()
obj = {}
countriesData = []
for country in all_countries:
    covid = Covid.objects.get(countryId=country.id)
    totalDataByCountry = {
        'deaths': covid.deaths,
        'recovered': covid.recovered,
        'cases': covid.cases
    }
    obj[f'{country.name}'] = totalDataByCountry
    countriesData.append({
        'name': country.name,
        'id': country.id
    })


def home_view(request, *args, **kwargs):
    return render(request, 'dashboard/home.html', {})


def country_view(request, *args, **kwargs):
    context = {
        'totalDeaths': Covid.objects.aggregate(Sum('deaths'))['deaths__sum'],
        'totalRecovered': Covid.objects.aggregate(Sum('recovered'))['recovered__sum'],
        'totalCases': Covid.objects.aggregate(Sum('cases'))['cases__sum']
    }
    if (request.method == 'POST'):
        country_id = request.POST['select']
        country_covid_data = Covid.objects.get(id=country_id)
        context['countryName'] = Country.objects.get(id=country_id).name
        context['data'] = country_covid_data
    return render(request, 'dashboard/country_page.html', context)


def total_data_view(request, *args, **kwargs):
    context = {
        'countriesData': countriesData,
        'dataByCountry': obj,
        'totalDeaths': Covid.objects.aggregate(Sum('deaths'))['deaths__sum'],
        'totalRecovered': Covid.objects.aggregate(Sum('recovered'))['recovered__sum'],
        'totalCases': Covid.objects.aggregate(Sum('cases'))['cases__sum']
    }
    return render(request, 'dashboard/total_data.html', context)
