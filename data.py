from index import *
from io import *

resultados = open("result.txt", "w")

resultados.close()

def manejo():
    manejo = open("result.txt", "a")
    manejo.write(marcado)
    