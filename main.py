from flask import Flask

app = Flask(__name__)

@app.route("/hola")
def hola():
    return "Hola mundo"

@app.route("/chau")
def chau():  # Changed the function name to 'chau'
    return "Chau"

if __name__ == "__main__":
    app.run()
