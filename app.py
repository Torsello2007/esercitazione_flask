#import dellla classe Flask da flask
from flask import Flask, jsonify
from flask_cors import CORS

#inizializziamo flask
#app rappresenta il nostro server
app = Flask(__name__)
CORS(app) #abilita CORS per TUTTE le route

#il decoratore route definisce gli ENDPOINT
#"quando siamo alla route "/" richiama il metodo associato"
@app.route("/")
def index():
    #ora una stringa, dopo un json, prossimamente una select da un db
    data = "ciao mondo"
    return data

@app.route("/profilo")
def profilo():
    profilo_data = {
        "nome": "Matteo",
        "professione": "giocatore professionista di clash royale",
        "status": "swag"
    }
    return jsonify(profilo_data)

if __name__ == "__main__":
app.run(debug=True, port=5000)


