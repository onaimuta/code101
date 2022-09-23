my_list = ["uno",
        "dos"
        "tres",
        "quatro"
        "cinco"]
print(len(my_list))
# Observe the commas, the len() function in Pythoon is used to find the length of an object. 
# Just a missed or added ",", can change everything
word = "Mutambashora";
print (len(word))

from unicodedata import name
from countryinfo import CountryInfo #Country info module
name = "UK"
country = CountryInfo(name)
data1 = country.capital()
data2 = country.alt_spellings()
data3 = country.info
print (data1)
print (data2)
print (data3)
print(len(name))


