import requests
import os
import sys
import json

c = requests.get("https://api.covid19api.com/summary")
data = json.loads(c.text)
covid = data['Global']['TotalDeaths']
print(f'Covid-19 has taken {covid} lives around globally.')