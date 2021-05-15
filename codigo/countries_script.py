from covid.models import Country, Covid
file = open("data.csv", "r")
for line in file:
    splittedLine = line.split(';')
    country = Country(name=splittedLine[0])
    country.save()




