Rain Alert System ☔

A Python script that checks upcoming weather conditions using the OpenWeather API and sends an SMS alert via Twilio if rain is expected in the next few hours.

Features:

1.Fetches weather forecast using latitude and longitude

2.Detects rain based on weather condition codes

3.Sends SMS alert if rain is predicted

4.Simple and lightweight

Tech Used:

1.Python

2.Requests

3.OpenWeather API

4.Twilio API

Setup:

Install dependencies:

pip install requests twilio


Create a .env file:

TWILIO_ACCOUNT_SID=your_sid

TWILIO_AUTH_TOKEN=your_auth_token

OPENWEATHER_API_KEY=your_api_key


Update location coordinates in the script:

MY_LAT = your latitude 

MY_LONG = your longitude

Run

python main.py


If rain is expected, you’ll receive an SMS reminder to carry an umbrella.

Notes

Weather is checked for the next few forecast intervals.

SMS charges may apply (Twilio)!

Intended for educational use!
