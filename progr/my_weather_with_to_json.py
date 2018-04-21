import pprint
import requests
import json
import functools

def to_json(func):
    @functools.wraps(func)
    def wrapped(*args, **kwargs):
        return json.dumps(func(*args, **kwargs))
    return wrapped

class MyWeather:
    def __init__(self):
        self._city_cache = {}

    @to_json
    def get(self, city):
        if city in self._city_cache:
            return self._city_cache[city]
        url = f"http://api.wunderground.com/api/3f99b63e6e335951/forecast10day/lang:RU/q/Russia/{city}.json"
        print("Sending Http request...")
        data = requests.get(url).json()
        forecast_data = data["forecast"]["simpleforecast"]["forecastday"]
        # forecast = []
        forecast = {}
        for day_data in forecast_data:
            forecast.update({
                str(day_data["date"]["day"])+" "+str(day_data["date"]["monthname"]): str(day_data["low"]["celsius"]) + "-" +str(day_data["high"]["celsius"])
            })
        self._city_cache[city] = forecast
        return forecast

class CityInfo:
    def __init__(self, city, weather_forecast = None):
        self.city = city
        self._weather_forecast = weather_forecast

    def weather_forecast(self):
        return self._weather_forecast.get(self.city)

def _main():
    weather_forecast = MyWeather()
    city = input("Введите город ")
    city_info = CityInfo(city, weather_forecast = weather_forecast)
    forecast = city_info.weather_forecast()
    #метод .loads() необходим, тк .dumps() возвращает строку
    new = json.loads(forecast)
    pprint.pprint(new)
    with open("/Users/utah/hw_univer/progr2/weather.json", "w") as f:
        json.dump(new, f)

if __name__ == "__main__":
    _main()