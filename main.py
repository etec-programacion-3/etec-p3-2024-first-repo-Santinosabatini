from flask import Flask, request

app = Flask(__name__)

@app.route("/hola")
def hola():
    return "Hola mundo"

@app.route("/chau")
def chau():  
    return "Chau"

@app.route("/saludo/<nombre>/<apellido>")
def saludo(nombre, apellido):
    return "Hola " + nombre + " " + apellido             


if __name__ == "__main__":
    app.run()
