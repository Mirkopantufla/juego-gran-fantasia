import os

class Personaje():

    #Inicializo las variables por defecto
    def __init__(self,nombre):
        self.nombre = nombre
        self.nivel = 1
        self.experiencia = 0

    #Propiedad que imprime las cualidades del jugador
    @property
    def estado(self):
        return f"""NOMBRE: {self.nombre}     NIVEL: {self.nivel}     EXP: {self.experiencia}
"""
    
    #Propiedad setter que maneja el nivel y la experiencia actual de los jugadores
    @estado.setter
    def estado(self, exp):
        temporal_exp = self.experiencia + exp

        #Si la experiencia es mayor o igual a 100
        #Sube un nivel y ajusta experiencia
        while temporal_exp >= 100:
            self.nivel += 1
            temporal_exp -= 100

        #Si la experiencia es menor a 0
        #Baja un nivel y ajusta experiencia
        while temporal_exp < 0 :
            if self.nivel > 1:
                temporal_exp = exp + 100
                self.nivel -= 1
            else:
                temporal_exp = 0

        self.experiencia = temporal_exp

    #Funcion que compara las dos instancias para retornar la probabilidad de ganar
    def get_probabilidad_ganar(self,other):
        if self < other:
            return 0.33
        elif self > other:
            return 0.66
        else:
            return 0.5

    #Funcion para mostrar las cualidades del juego
        #Esta se repetira cada vez que se necesite jugar
    @staticmethod
    def dialogo_opciones(probabilidad_ganar):
        return int(input(
            f"""Con tu nivel actual, tienes {probabilidad_ganar*100}% de probabilidades de ganarle al Orco.
Si ganas, ganaras 50 puntos de experiencia y el orco perdera 30.
Si pierdes, perderas 30 puntos de experiencia y el orco ganara 50.
Que deseas hacer?
1. Atacar
2. Huir
> """
        ))
    
    def __lt__(self, other):
        return self.nivel < other.nivel  #Este metodo se activa cuando yo aplico el menor que "<"

    def __gt__(self, other):
        return self.nivel > other.nivel  #Este metodo se activa cuando yo aplico el mayor que ">"

    def __eq__(self, other):
        return self.nivel == other.nivel #Este metodo se activa cuando yo aplico '=='
    