"""Crear un juego de fusión.

El juego consiste en crear personajes un juego y que esos personajes se puedan fusionar
para formar personajes más poderosos que tengan más poder ...

Para ello deberemos cambiar el comportamiento del operador "+" para que cuando los personajes
se fusionen, salga un nuevo personaje con habilidades mejoradas.

una posible formula es: el promedio de las habilidades de ambos, al cuadrado!"""


class Personaje:
    def __init__(self, nombre, fuerza, velocidad):
        self.nombre = nombre
        self.velocidad = velocidad
        self.fuerza = fuerza
    
    def __repr__(self) -> str:
        return f"({self.nombre}) => [Fuerza: {self.fuerza}, Velocidad: {self.velocidad}]"
        
    def __add__(self, new_character):
        new_name = self.nombre + "-" + new_character.nombre
        new_velocity = self.velocidad + new_character.velocidad
        new_force = self.fuerza + new_character.fuerza
        return Personaje(new_name, new_force, new_velocity)
    
Captain_America = Personaje("Steve Rogers", 100, 50)
Iron_Man = Personaje("Tony Stark", 80, 150)
Hulk = Personaje("Bruce Banner", 1000, 500)

print(Captain_America)
print(Iron_Man)
print(Hulk)

print("\n=========================\n")

new_character = Captain_America + Hulk
new_character2 = Iron_Man + Captain_America + Hulk

print(new_character)
print(new_character2)