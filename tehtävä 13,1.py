from flask import Flask, Response
import json

app = Flask(__name__)

@app.route('/alkukuku/<luku>')
def alkukuku(luku):
    try:

        luku = int(luku)

        onko_alkuluku = True
        jakaja = 2
        while jakaja < luku:
            if luku % jakaja == 0:

                onko_alkuluku = False
                break
            jakaja += 1

        tilakoodi = 200
        vastaus = {
            "Number": 31,
            "isPrime": onko_alkuluku,
        }

    except:
        tilakoodi = 400
        vastaus = {
            "status": tilakoodi,
            "teksti": "Virheellinen parametri"
        }

    jsonvast = json.dumps(vastaus)

    return Response(response=jsonvast, status=tilakoodi,  mimetype="application/json")

@app.errorhandler(404)
def page_not_found(virhekoodi):
    vastaus = {
        "status": "404",
        "teksti": "Virheellinen päätepiste"
    }

    jsonvast = json.dumps(vastaus)
    return Response(response=jsonvast, status=tilakoodi, mimetype="application/json")