import django_tables2 as tables
from .models import Covid


class PersonTable(tables.Table):
    name=tables.Column(accessor='countryId.name')
    cases=tables.Column(accessor='cases')
    deaths=tables.Column(accessor='deaths')
    recovered = tables.Column(accessor='recovered')
    class Meta:
        attrs = {"class": "mytable"}

