import os 
import requests

API_KEY = os.getenv("API_KEY_PROYECTO")

if not API_KEY:
    print("error: api key no encontrada")
    exit(1)

city = "santiago"
url =  f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

try:
    response = requests.get(url, timeout=10)

    if response.status_code == 404:
        print("error 404")
        exit()
    elif response.status_code ==401:
     print("API KEY INVALIDA")
     exit()

    response.raise_for_status()

    data = response.json()

    temperatura = data["main"]["temp"]
    humedad = data["main"]["humidity"]
    clima = data["weather"][0]["description"]

    print("=== CLIMA EN SANTIAGO ===")
    print(f"temperatura:{temperatura}°c")
    print(f"humedad:{humedad}%")
    print(f"condición:{clima}")

except requests.Timeout:
    print("timeout")

except requests.ConnectionError:
    print("error de conexion")

except Exception as e:
    print("error:", e)