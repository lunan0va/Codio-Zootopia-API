import requests

API_KEY = "sl5K/ZnEUXPhl1zixQPn3w==atvhb8vzsjU72bw8"
API_URL = "https://api.api-ninjas.com/v1/animals"

def fetch_data(animal_name):
    """
    Holt Tierdaten über das API für das gegebene Tier.
    Gibt eine Liste von Tieren zurück, jeweils als Dictionary.
    """
    url = f"{API_URL}?name={animal_name}"
    headers = {"X-Api-Key": API_KEY}

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"[Fehler] API Rückgabe: {response.status_code}")
        return []