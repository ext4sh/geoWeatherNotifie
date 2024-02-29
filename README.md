# GeoWeather

## Description
Python program that uses web scraping to retrieve current weather data in real time. It uses powerful Python libraries such as BeautifulSoup for parsing web pages and notifypy for restoring notifications on the Linux desktop.

The main function of this program is to display the current temperature in the user's location. It uses the Geolocation DB API to determine the user's geolocation, and then uses that data to retrieve weather data from Weather.com. The results are then displayed to users as a desktop notification.

## Installation
Before you can use GeoWeather Notifier, you need to install some others. You can install them using pip:

```bash
requests install pip beautifulsoup4 notifypy geocoder
```

## Using
Just run the Python script and you will receive a notification with the current temperature in your location:

```python
python geoweather_notifier.py
```
## License
This project is licensed under the MIT License.
