"""Herencias - Ejercicio 2

Ejercicio de herencia y uso de super:

Crear un sistema para una escuela. En este sistema, vamos a tener dos clases principales:
Persona y Estudiante. La clase Persona tendrá los atributos de nombre y edad y un método
que imprima el nombre y la edad de la persona. La clase Estudiante heredará de la clase
Persona y también tendrá un atributo adicional: grado y un método que imprima el grado del
estudiante.

Deberás utilizar super en el método de inicialización (init) para reutilizar el código de la clase padre
(Persona). Luego crea una instancia de la clase Estudiante e imprime sus atributos y utiliza sus
métodos para asegurarte de que todo funciona correctamente."""

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre 
        self.edad = edad
    
    def nombre__edad_persona(self):
        return f"La persona se llama {self.nombre} y tiene una edad de {self.edad} años"


class Estudiante(Persona):
    def __init__(self, nombre, edad, grado):
        super().__init__(nombre, edad)
        self.grado = grado
        
    def grado_estudiante(self):
        return f"El grado del estudiante {self.nombre}, es {self.grado}"
    
    
estudiante = Estudiante(nombre="Alicia", edad=45, grado="Master Sc")

print(f"El grado del estudiante es: \n {estudiante.grado_estudiante()}")

print(f"La edad y el nombre de la persona es: {estudiante.nombre__edad_persona()}")
        
#===================================================================================================#

"""Ejercicio de herencia múltiple y MRO:

Imagina que estás modelando animales en un zoológico. Crear tres clases: "Animal", "Mamifero" y
"Ave". La clase "Animal" debe tener un método llamado "comer". La clase "Mamifero" debe tener
un método llamado "amamantar" y la clase "Ave" un método llamado "volar".

Ahora, crea una clase "Murcielago" que herede de "Mamifero" y "Ave", en ese orden, y por lo tanto
debe ser capaz de "amamantar" y "volar", además de "comer".

Finalmente, juega con el orden de herencia de la clase "Murcielago" y observa cómo cambia el
MRO y el comportamiento de los métodos al usar super()."""


class Animal:
    def __init__(self, especie):
        self.especie = especie
        
    def comer(self):
        return "Estoy comiendo"

class Mamifero(Animal):
    def __init__(self, especie, reproducion):
        Animal.__init__(self, especie)
        self.reproducion = reproducion
    
    def amamantar(self):
        return "Estoy amamantando"

class Ave(Animal):
    def __init__(self, especie, plumaje):
        Animal.__init__(self, especie)
        self.plumaje = plumaje
        
    def volar(self):
        return "Estoy volando"
    
class Murcielago(Mamifero, Ave):
    def __init__(self, especie, reproducion, plumaje, tipo):
        Mamifero.__init__(self, especie, reproducion)
        Ave.__init__(self, especie, plumaje)
        self.tipo = tipo
        
murcielago = Murcielago("Mamífero", "Embarazo_Mamífero", "Sin Plumaje", "Hervíboro")

print(murcielago.amamantar())
print(murcielago.comer())
print(murcielago.volar())


# En esta versión, he reemplazado el uso de super() con llamadas explícitas a Animal.__init__() 
# dentro de los inicializadores de Mamifero y Ave. De esta manera, aseguramos que ambos inicializadores 
# sean llamados correctamente, evitando problemas con la resolución de métodos en la herencia múltiple.