import requests
import json
import re

from bs4 import BeautifulSoup
from notifypy import Notify

def getdata(url):
    r = requests.get(url)
    return r.text

geo_request = requests.get("https://geolocation-db.com/jsonp")
geo_data = re.findall(r"\((.*?)\)", geo_request.text)[0]
geo_json = json.loads(geo_data)

lat, lon = geo_json["latitude"], geo_json["longitude"]
url = f"https://weather.com/en-IN/weather/today/l/{lat},{lon}"

htmldata = getdata(url) 
soup = BeautifulSoup(htmldata, 'html.parser')
print(soup.prettify())

current_temperature = soup.find("span",
                                class_="CurrentConditions--tempValue--MHmYY")

if current_temperature:
    temp = current_temperature.text
else:
    temp = "Error"

result = f"Current temperature {temp} in {geo_json['city']}"

notification = Notify()
notification.title = "Weather"
notification.message = result
notification.icon = "live_weather/cloud.png"

notification.send()
