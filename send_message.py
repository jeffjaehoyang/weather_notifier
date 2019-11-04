from twilio.rest import Client
from dotenv import load_dotenv
from get_weather import get_weather
import os

load_dotenv()

account_sid = os.getenv('TWILIO_ACCOUNT_SID')
auth_token = os.getenv('TWILIO_AUTH_TOKEN')
client = Client(account_sid, auth_token)
my_number = os.getenv('MY_NUMBER')
pg_number = os.getenv('PG_NUMBER')
twilio_number = os.getenv('TW_NUMBER')

def send_message(twilio_number, dest_number):
    weather_dump = get_weather()
    current_status = None
    current_temp = None
    recepient = None
    body = None

    current_temp = weather_dump[1]

    if dest_number == pg_number:
        recepient = "Paige"
    else:
        recepient = "Jeff"

    if 'rain' in weather_dump[0]:
        current_status = 'raining'
        body = f"Hi, {recepient}. It's currently {current_status} outside. Remember to bring your umbrella! Oh, just one more thing. It's {current_temp}(°F) outside, so please dress accordingly."
    elif 'cloud' in weather_dump[0]: 
        current_status = 'cloudy'
        body = f"Hi, {recepient}. It's currently {current_status} outside. No need for an umbrella! Oh, just one more thing. It's {current_temp}(°F) outside, so please dress accordingly."
    elif 'clear' in weather_dump[0]:
        current_status = 'clear'
        body = f"Hi, {recepient}. It's currently {current_status} outside. No need for an umbrella! Oh, just one more thing. It's {current_temp}(°F) outside, so please dress accordingly."

    message = client.messages \
                .create(
                     body=body,
                     from_=twilio_number,
                     to=dest_number
                 )
    print(message.sid)
    return message.sid

send_message(twilio_number, pg_number)
send_message(twilio_number, my_number)