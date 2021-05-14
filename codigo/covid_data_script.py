from covid.models import Country, Covid
file = open("data.csv", "r")
index = 1
for line in file:
    splittedLine = line.split(';')
    cases = splittedLine[1]
    recovered = splittedLine[2]
    deaths = splittedLine[3]
    covid = Covid(countryId=Country.objects.get(id=index), cases=cases, deaths=deaths, recovered=recovered)
    covid.save()
    index += 1







