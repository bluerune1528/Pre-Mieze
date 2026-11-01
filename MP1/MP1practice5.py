import requests
try:
    response = requests.get("https://api.open-meteo.com/v1/forecast", params={"latitude": 18.52, "longitude": 73.86,
"current": "temperature_2m,wind_speed_10m"}, timeout=5)
except requests.exceptions.Timeout:
    print("timed out")
else:
    if response.status_code >=400:
        print("failed:", response.status_code)
    else:
        data = response.json()
        # print(type(data))     dict
        # print(data)
        print(f"Pune: {data["current"]["temperature_2m"]} {data["current_units"]["temperature_2m"]}, wind: {data['current']['wind_speed_10m']} {data['current_units']['wind_speed_10m']}")