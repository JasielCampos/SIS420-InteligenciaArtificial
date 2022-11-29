#Lista de Integrantes:
#
# 1. Santillan Jason
#    Ing. en Ciencias de la Computación
#
# 2. Adriana Jasiel Campos Romero
#    Ing. en Ciencias de la Computación
#
# 3. Rodrigo Walter Andre Basilio
#    Ing. en Ciencias de la Computación
#
# 4. Rosario Cruz Rodrigo 
#    Ing. en Ciencias de la Computación
#
# 5. Choque Cruz Flavio Denylson
#    Ing. de Sistemas
#
# 6. Walter Freddy Canaviri Parraga
#    Ing. de Sistemas

import random
import time
from time import sleep
def time_convert(sec):
  mins = sec // 60
  sec = sec % 60
  hours = mins // 60
  mins = mins % 60
  print("Tiempo total = {0}:{1}:{2}".format(int(hours),int(mins),sec))


def crear_mapa_laberinto(numero_filas, numero_columnas, numero_paredes, numero_espacios, numero_pelotas):
# Se crea un mapa lleno de paredes
    mapa_laberinto = []
    numero_paredes_generadas = 0
    for fila in range(0, numero_filas):
        fila_mapa_laberinto = []
        for columna in range(0, numero_columnas):
    #             if (random.randrange(2) == 1 and numero_paredes_generadas < numero_paredes):
    #                 fila_mapa_laberinto.append('#')
    #                 numero_paredes_generadas += 1
    #             else:
    #                 fila_mapa_laberinto.append(' ')
            fila_mapa_laberinto.append('#')
        mapa_laberinto.append(fila_mapa_laberinto)
            
    #Se ubica aleatoriamente un punto de inicio y a partir de ese punto se llenan espacios
    numero_espacios_generados = 0
    fila_posicion_actual = random.randrange(numero_filas)
    columna_posicion_actual = random.randrange(numero_columnas)
    mapa_laberinto[fila_posicion_actual][columna_posicion_actual] = ' '
    numero_espacios_generados += 1

    while numero_espacios_generados < numero_espacios:
        direccion = random.randrange(4)
        if direccion == 0 and fila_posicion_actual > 0:
            fila_posicion_actual -= 1
        elif direccion == 1 and fila_posicion_actual < numero_filas - 1:
            fila_posicion_actual += 1
        elif direccion == 2 and columna_posicion_actual > 0:
            columna_posicion_actual -= 1
        else:
            if columna_posicion_actual < numero_columnas - 1:
                columna_posicion_actual += 1
            
        if mapa_laberinto[fila_posicion_actual][columna_posicion_actual] == '#':
            mapa_laberinto[fila_posicion_actual][columna_posicion_actual] = ' '
            numero_espacios_generados += 1
    
    numero_pelotas_generadas= 0

    while numero_pelotas_generadas < numero_pelotas:
        direccion = random.randrange(4)
        if direccion == 0 and fila_posicion_actual > 0:
            fila_posicion_actual -= 1
        elif direccion == 1 and fila_posicion_actual < numero_filas - 1:
            fila_posicion_actual += 1
        elif direccion == 2 and columna_posicion_actual > 0:
            columna_posicion_actual -= 1
        else:
            if columna_posicion_actual < numero_columnas - 1:
                columna_posicion_actual += 1
            
        if mapa_laberinto[fila_posicion_actual][columna_posicion_actual] == ' ':
            mapa_laberinto[fila_posicion_actual][columna_posicion_actual] = '0'
            numero_pelotas_generadas += 1

    print(numero_espacios_generados)
    print(numero_paredes_generadas)
    return mapa_laberinto



numero_filas = int(input('Introduzca el número de Filas del laberinto: '))
numero_columnas = int(input('Introduzca el número de Columnas del laberinto: '))
numero_paredes = int(input('Introduzca el número de Paredes del laberinto: '))
numero_espacios = numero_filas * numero_columnas - numero_paredes
numero_pelotas = int(input('Introduzca el número de Pelotas del laberinto: '))

laberinto = crear_mapa_laberinto(numero_filas, numero_columnas, numero_paredes, numero_espacios, numero_pelotas)
start_time = time.time()

# laberinto = [["*", "#", "#", " ", "#"],
#              [" ", "#", " ", " ", " "],
#              [" ", " ", " ", "#", " "],
#              ["#", "#", " ", "#", " "],
#              ["0", "#", " ", "#", " "],
#              [" ", "#", " ", "#", "0"],
#              [" ", " ", "0", "#", " "],]

# laberinto = [[" ", " ", " ", " ", " "],
#              [" ", " ", " ", " ", " "],
#              [" ", " ", " ", " ", " "],
#              [" ", " ", " ", " ", " "],
#              [" ", " ", " ", " ", " "],
#              [" ", " ", " ", " ", " "],
#              [" ", " ", " ", " ", "#"],]


#Situar al caracter en un espacio libre aleatorio, guardar el valor y posición de lo que habia antes

while True:
    fila_actual = random.randrange(numero_filas)
    columna_actual = random.randrange(numero_columnas)
    if(laberinto[fila_actual][columna_actual] == " "):
        valor_antiguo = " "
        laberinto[fila_actual][columna_actual] = "*"
        break

def mover_abajo(laberinto1, fila1, columna1):
    laberinto1[fila1][columna1] = " "
    fila1 +=1
    laberinto1[fila1][columna1] = "A"

def mover_arriba(laberinto1, fila1, columna1):
    laberinto1[fila1][columna1] = " "
    fila1 -=1
    laberinto1[fila1][columna1] = "A"

def mover_derecha(laberinto1, fila1, columna1):
    laberinto1[fila1][columna1] = " "
    columna1 +=1
    laberinto1[fila1][columna1] = "A"

def mover_izquierda(laberinto1, fila1, columna1):
    laberinto1[fila1][columna1] = " "
    columna1 -=1    
    laberinto1[fila1][columna1] = "A"

#Mover al caracter a espacios libres sin salirnos del laberinto
cantidad_movimientos = 1000
delay = 0.1
pelotas_encontradas = 0

#Mostrar el laberinto para identificar a las posiciones visualmente
for fila_mapa_laberinto in laberinto:
    print(fila_mapa_laberinto)
sleep(5)

while pelotas_encontradas<numero_pelotas:
    direccion = random.randrange(4) #Generamos una dirección aleatoria al cual se movera el caracter
    if direccion == 0:
        if(fila_actual == numero_filas-1): #Nos aseguramos de que no se salga del laberinto
            continue
        # Nos movemos hacia la abajo
        elif laberinto[fila_actual+1][columna_actual] == " " or laberinto[fila_actual+1][columna_actual] == "0":
            if laberinto[fila_actual+1][columna_actual] == "0":
                pelotas_encontradas += 1
            
            laberinto[fila_actual][columna_actual] = " "
            fila_actual += 1
            laberinto[fila_actual][columna_actual] = "*"
            # cantidad_movimientos -= 1
            # print("Movimientos restantes: " + str(cantidad_movimientos))
            for fila_mapa_laberinto in laberinto:
                print(fila_mapa_laberinto)
            print("---------------------------------")
            sleep(delay)
        else:
            continue
    elif direccion == 1:
        if(fila_actual == 0): #Nos aseguramos de que no se salga del laberinto
            continue
        # Nos movemos hacia la arriba
        elif laberinto[fila_actual-1][columna_actual] == " " or laberinto[fila_actual-1][columna_actual] == "0":
            if laberinto[fila_actual-1][columna_actual] == "0":
                pelotas_encontradas += 1
            
            laberinto[fila_actual][columna_actual] = " "
            fila_actual -= 1
            laberinto[fila_actual][columna_actual] = "*"
            # cantidad_movimientos -= 1
            # print("Movimientos restantes: " + str(cantidad_movimientos))
            for fila_mapa_laberinto in laberinto:
                print(fila_mapa_laberinto)
            print("---------------------------------")
            sleep(delay)
        else:
            continue
    elif direccion == 2:
        if(columna_actual == numero_columnas-1): #Nos aseguramos de que no se salga del laberinto
            continue
        # Nos movemos hacia la derecha
        elif laberinto[fila_actual][columna_actual+1] == " " or laberinto[fila_actual][columna_actual+1] == "0":
            if laberinto[fila_actual][columna_actual+1] == "0":
                pelotas_encontradas += 1
            
            laberinto[fila_actual][columna_actual] = " "
            columna_actual += 1
            laberinto[fila_actual][columna_actual] = "*"
            # cantidad_movimientos -= 1
            # print("Movimientos restantes: " + str(cantidad_movimientos))
            for fila_mapa_laberinto in laberinto:
                print(fila_mapa_laberinto)
            print("---------------------------------")
            sleep(delay)
        else:
            continue
    elif direccion == 3:
        if(columna_actual == 0): #Nos aseguramos de que no se salga del laberinto
            continue
        # Nos movemos hacia la izquierda
        elif laberinto[fila_actual][columna_actual-1] == " " or laberinto[fila_actual][columna_actual-1] == "0":
            if laberinto[fila_actual][columna_actual-1] == "0":
                pelotas_encontradas += 1

            laberinto[fila_actual][columna_actual] = " "
            columna_actual -= 1
            laberinto[fila_actual][columna_actual] = "*"
            # cantidad_movimientos -= 1
            # print("Movimientos restantes: " + str(cantidad_movimientos))
            for fila_mapa_laberinto in laberinto:
                print(fila_mapa_laberinto)
            print("---------------------------------")
            sleep(delay)
        else:
            
            continue
            
end_time = time.time()
time_lapsed = end_time - start_time
time_convert(time_lapsed)

