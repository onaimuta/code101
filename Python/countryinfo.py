'''
I am from Zimbabwe but have lived in Uganda for a long time
'''
from countryinfo import CountryInfo
count = input("Enter Country Name")
country = CountryInfo
print ("Country aliases: ", country.alt_spellings())
print ("Capital is: ", country.capital())
print ("Currency is: ", country.currencies())
print ("Language is: ", country.languages())
print ("Borders are: ", country.borders())
