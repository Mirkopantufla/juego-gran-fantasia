from personaje import Personaje
import random
import os

print("************** Bienvenido a Gran Fantasía **************")
# Seteo del nombre del jugador
nombre = input("Por favor indique su nombre: \n")
p = Personaje(nombre)

os.system("cls") #Limpio pantalla
print(p.estado) #Imprimo jugador creado
print("Oh no, Ha aparecido un Orco!") #Aviso como en el ejemplo
o = Personaje('Orco') #Creo el jugador orco

probabilidad_ganar = p.get_probabilidad_ganar(o) #Defino las probabilidades de ganar del jugador frente al enemigo


opcion_orco = Personaje.dialogo_opciones(probabilidad_ganar)
# Guardo la opcion ingresada por el usuario
# 1. Atacar
# 2. Huir

while opcion_orco == 1: #Mientras sea 1, seguira preguntando y ejecutandose
    numero = random.uniform(0,1) #Numero random entre 0 y 1
    resultado = 'Gane' if numero < probabilidad_ganar else 'Pierdo' 

    if resultado == 'Gane':
        os.system("cls")
        print(f"""Le has ganado al orco, Felicidades!
Recibiras 50 puntos de experiencia!
              """)
        p.estado = 50
        o.estado = -30
    elif resultado == 'Pierdo':
        os.system("cls")
        print(f"""Oh No! El Orco te ha ganado!
Has perdido 30 puntos de experiencia!
              """)
        p.estado = -30
        o.estado = 50

    #Imprimo la informacion nuevamente
    print(p.estado)
    print(o.estado)
    probabilidad_ganar = p.get_probabilidad_ganar(o)
    opcion_orco = Personaje.dialogo_opciones(probabilidad_ganar)

os.system("cls")
print('¡Has huido! El orco ha quedado atrás.')