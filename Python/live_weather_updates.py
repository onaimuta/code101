from wsgiref import headers
from bs4 import BeautifulSoup
import requests
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)\AppleEbkit/537.36 KHTML, like Gecko) \Chrome/58.0.3029.110 Safari/537.3"}
def weather (city):
    city = city.replace(" ","+")
    