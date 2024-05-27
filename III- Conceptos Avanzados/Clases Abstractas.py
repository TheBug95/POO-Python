# - Las clases abstractas son como plantillas para crear clases a partir de ellas
# - Estas clases no pueden ser instanciadas
# - Es como una especie de contrato, donde la clase que la herede tiene que implementar de forma 
# obligatoria todos sus métodos definidos
# - Fomenta el polimorfismo

from abc import ABC, abstractmethod

class Persona(ABC):
    @abstractmethod
    def __init__(self, nombre, edad, sexo, dedicacion) -> None:
        self.__nombre = nombre
        self.__edad = edad
        self.__sexo = sexo
        self.__dedicacion = dedicacion
        
    @abstractmethod
    def hacer_actividad(self):
        pass
    
    def presentarse(self):
        return f"Hola mi nombre es {self.__nombre} y tengo {self.__edad} años"
        
    @property
    def dedicacion(self):
        return self.__dedicacion
        
        
        
class Estudiante(Persona):
    def __init__(self, nombre, edad, sexo, dedicacion) -> None:
        super().__init__(nombre, edad, sexo, dedicacion)
    
    def hacer_actividad(self):
        return f"Estoy estudiando: {self.dedicacion}"
    
class Trabajador(Persona):
    def __init__(self, nombre, edad, sexo, dedicacion) -> None:
        super().__init__(nombre, edad, sexo, dedicacion)
        
    def hacer_actividad(self):
        return f"Estoy trabajando en: {self.dedicacion}"
    
    
#persona = Persona() # Esto no se puede ya que la clase es abstracta

estudiante = Estudiante("Miguel", 29, "Masculino", "Programación")

print(estudiante.hacer_actividad())
print(estudiante.presentarse())

estudiante = Trabajador("Lisuan", 29, "Femenino", "Programación")

print(estudiante.hacer_actividad())
print(estudiante.presentarse())