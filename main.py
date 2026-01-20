import requests
import os
from twilio.rest import Client
from dotenv import load_dotenv
load_dotenv()

account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token =os.getenv("TWILIO_AUTH_TOKEN")
MY_LAT = #latitude
MY_LONG = #longitude

api="64781f609c2b6f09796ab3f3999cdc30"

parameters = {
        "lat": MY_LAT,
        "lon": MY_LONG,
        "appid":api,
        "cnt":4,
}
response = requests.get("https://api.openweathermap.org/data/2.5/forecast", params=parameters)
data = response.json()
print(data)
rain=False
ids=[i["weather"][0]["id"] for i in data["list"]]
for i in ids:
        if i < 800:
                rain=True
if rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="Its going to rain in your area,Bring Umbrella ☂️ ",
        from_=os.getenv("TWILIO_NUM"),
        to=os.getenv("MY_NUM"),
    )
    print(message.status)