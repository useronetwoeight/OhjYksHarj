import requests


def hae_saatiedot(paikkakunta, api):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={paikkakunta}&appid={api}"
    vastaus = requests.get(url)
    data = vastaus.json()
    if vastaus.status_code == 200:
        sailytieto = data["main"]
        kelvin = sailytieto["temp"]
        celsius = kelvin - 273.15
        kuvaus = data["weather"][0]["description"]
        return kuvaus, celsius
    else:
        return None, None


paikkakunta = input("Paikkakunta: ")
api = input("OpenWeatherMap API key: ")

kuvaus, lampo = hae_saatiedot(paikkakunta, api)
if kuvaus is not None and lampo is not None:
    print(f"Sää paikkakunnalla {paikkakunta}:")
    print(f"Säätila: {kuvaus}")
    print(f"Lämpötila: {lampo:.1f} C")