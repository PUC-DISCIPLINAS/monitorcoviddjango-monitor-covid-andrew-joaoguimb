from django.db import models


# Create your models here.


class Country(models.Model):
    name = models.TextField()
    def _str_(self):
        return self.name



class Covid(models.Model):
    countryId = models.ForeignKey(Country, on_delete=models.CASCADE)
    cases = models.IntegerField()
    deaths = models.IntegerField()
    recovered = models.IntegerField()
