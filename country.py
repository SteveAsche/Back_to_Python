# create a list of countries
countries = ['united states', 'canada', 'mexico', 'brazil', 'argentina', 'france', 'germany', 'italy', 'spain', 'china', 'japan', 'india', 'australia']
capitals = ['washington, d.c.', 'ottawa', 'mexico city', 'brasilia', 'buenos aires', 'paris', 'berlin', 'rome', 'madrid', 'beijing', 'tokyo', 'new delhi', 'canberra']
#combo = list(zip(countries, capitals))
#print(combo)
allCountry = []
tempDict = {}
index = 0

for country in countries:
    tempDict = dict(country=country.title(), capital=capitals[index].title())
    allCountry.append(tempDict)
    index += 1

message = input("Enter a country name to find its capital: ").lower()
found = False
for country in allCountry:
    if message == country['country'].lower():
        print(f"The capital of {country['country']} is {country['capital']}.")
        found = True
        break

if not found:
    print("Country not found.")
