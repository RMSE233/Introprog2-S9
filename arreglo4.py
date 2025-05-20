import os
import random
import time


participantes = list()
while True:
    os.system("cls||clear")
    os.system("color b1")
    nombre = input("Ingrese el nombre del participante (o 'fin' para terminar): ")
    if nombre.lower() == 'fin':
        break
    participantes.append(nombre.upper())
    
os.system("cls||clear")
print("Participantes agregados...")
print(participantes)

os.system(" cls||clear")
print("participantes registrados")
print(participantes)

for cont in range(10, 0, -1):
    os.system("cls||clear")
    print(cont)
    time.sleep(1)


fin = len(participantes) - 1
ganador = random.randint(0, fin)
print("El ganador es:", participantes[ganador])
print("Gracias por participar")
    
    