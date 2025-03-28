import requests

# Palvelun osoite ("endpoint")
pyyntö = "https://api.chucknorris.io/jokes/random"

try:

    #Lähetetään pyytö
    vastaus = requests.get(pyyntö)

    #Jos vastaus ok (status-koodi 200), haetaan json:sta
    #Value-kentä arvo (=varsinainen vistin teksti).
    if vastaus.status_code == 200:
        json_vastaus = vastaus.json()
        print(json_vastaus['value'])


# Poikkeuskäsittely (netti pokki tms.)
except requests.exceptions.RequestException as e:
    print ("Hakua ei voitu suoritta.")