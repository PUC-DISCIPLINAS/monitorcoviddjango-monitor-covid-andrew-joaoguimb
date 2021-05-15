from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django import forms
from django.db.models import Sum
from django.views.decorators.csrf import csrf_exempt
from django_tables2 import SingleTableView
from .models import Covid, Country
import django_tables2 as tables

# Create your views here.

from django_tables2 import SingleTableView
from .tables import PersonTable


class PersonListView(SingleTableView):
    model = Covid
    table_class = PersonTable
    template_name = 'dashboard/test.html'

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

    table = PersonTable(Covid.objects.all())


def home_view(request, *args, **kwargs):
    return render(request, 'dashboard/home.html', {})


def country_view(request, *args, **kwargs):
    table.paginate(page=request.GET.get("page", 1), per_page=10)
    context = {
        'countriesData': countriesData,
        'dataByCountry': obj,
        'totalDeaths': Covid.objects.aggregate(Sum('deaths'))['deaths__sum'],
        'totalRecovered': Covid.objects.aggregate(Sum('recovered'))['recovered__sum'],
        'totalCases': Covid.objects.aggregate(Sum('cases'))['cases__sum'],
        'table': table
    }
    print(request)
    if (request.method == 'POST'):
        country_id = request.POST['select']
        if(country_id != "Global"):
            country_covid_data = Covid.objects.get(id=country_id)
            context['countryName'] = Country.objects.get(id=country_id).name
            context['data'] = country_covid_data
            return render(request, 'dashboard/country_page.html', context)
    return render(request, 'dashboard/total_data.html', context)



def total_data_view(request, *args, **kwargs):
    table.paginate(page=request.GET.get("page", 1), per_page=10)
    context = {
        'countriesData': countriesData,
        'dataByCountry': obj,
        'totalDeaths': Covid.objects.aggregate(Sum('deaths'))['deaths__sum'],
        'totalRecovered': Covid.objects.aggregate(Sum('recovered'))['recovered__sum'],
        'totalCases': Covid.objects.aggregate(Sum('cases'))['cases__sum'],
        'table': table
    }
    return render(request, 'dashboard/total_data.html', context)
