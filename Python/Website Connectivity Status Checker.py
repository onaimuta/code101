# import requests
# resp = requests.get("https://tragela.com")
# html = resp.text
# print(html[1:100])

# import urllib.request

# print(urllib.request.urlopen("https://www.tragela.com").getcode())

from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError
req = Request("https://tragela.com")
try:
    response = urlopen(req)
except HTTPError as e:
    print('The server couldn\'t fulfill the request.')
    print('Error code: ', e.code)
except URLError as e:
    print('Website is Down!')
    print('Reason: ', e.reason)
else:
    print ('Website is Up!')

    