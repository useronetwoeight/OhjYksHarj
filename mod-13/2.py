from flask import Flask, jsonify
app = Flask(__name__)
lentopeli = {}


@app.route('/kenttä/<string:icao>', methods=['GET'])
def inffo(icao):
    if icao in lentopeli:
        returni = {
            "ICAO": icao,
            "Nimi": lentopeli[icao]["Nimi"],
            "Kaupunki": lentopeli[icao]["Sijainti"]
        }
        return jsonify(returni)
    else:
        return jsonify({"error": "Error not found"}), 404

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)
