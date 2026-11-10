import requests
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import time


reader = SimpleMFRC522()


url = "http://[2001:7c0:2321:0:f816:4eff:fe82:1720]:8000/api/load_rfid"

try:
  while True:
    id, password = reader.read()
    print(f"Karte erkannt mit ID: {id}")

    data = {"id": str(id).strip(), "password": password}

    try:
      response = requests.post(url, json=data, timeout=5)
      response.raise_for_status()
      print("Server-Antwort:", response.json())
    except requests.exceptions.RequestException as e:
      print("Verbindungsfehler zum Server:", e)

    time.sleep(2)


finally:
  GPIO.cleanup()
