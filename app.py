from flask import Flask
import sys
import random

app = Flask(__name__)


# python decorator
@app.route("/")
def update_posiciones():
    puntos = []
    for i in range(10):
        puntos.append({"id": i, "x": i, "y": i, "z": i})

    # como hacer impresión 
    print("UN MENSAJITO A IMPRIMIR", file=sys.stdout)

    # random en un rango de valores flotantes
    random.uniform(0, 10)
    
    return {"carros": puntos}