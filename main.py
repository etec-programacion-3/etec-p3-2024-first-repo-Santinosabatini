from flask import Flask, request

app = Flask(__name__)

@app.route("/hola")
def hola():
    return "Hola mundo"

@app.route("/chau")
def chau():  
    return "Chau"

@app.route("/saludo/<nombre>")
def saludo(nombre):
    return "Hola " + nombre


if __name__ == "__main__":
    app.run()
