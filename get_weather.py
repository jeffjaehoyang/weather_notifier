import pyowm, os, json
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv('OWM_API_KEY')
owm = pyowm.OWM(api_key)
CITY = 'Evanston'
COUNTRY = 'US'

def get_weather():
	weather = owm.weather_at_place(f'{CITY}, {COUNTRY}')
	weather_report = json.loads(weather.to_JSON())
	current_weather = weather_report["Weather"]["detailed_status"]
	current_temp = weather.get_weather().get_temperature('fahrenheit')['temp']
	weather_dump = [current_weather, current_temp]
	print(weather_dump)
	return weather_dump

get_weather()
