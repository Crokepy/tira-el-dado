from io import *
import time
import random
#from data import *


print('el dado se tirara en 3 segundos')

time.sleep(3)

resultado = random.randint(1, 6)

resultados = open("result.txt", "w")

resultados.close()

def manejo():
    manejo = open("result.txt", "a")
    manejo.write(str(resultado))

manejo()

print(resultado)


correcto = "si"


reciento = input('quieres hacer otro lanzamiento ? ')

while correcto == str(reciento):
        
    print('el dado se tirara en 3 segundos')

    time.sleep(3)

    resultado2 = random.randint(1, 5)

    
    
    def manejo():
        manejo = open("result.txt", "a")
        manejo.write(str(resultado2))

    manejo()

    resultados.close()

   

    print(resultado2)

    break