from django.db import models


# Create your models here.


class Country(models.Model):
    name = models.TextField()


class Covid(models.Model):
    countryId = models.ForeignKey(Country, on_delete=models.CASCADE)
    cases = models.IntegerField()
    deaths = models.IntegerField()
    recovered = models.IntegerField()
