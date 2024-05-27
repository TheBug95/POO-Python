# Estos métodos se utilizan para acceder a estos atributos privados que tienen las clases y 
# además poder modificar estos elementos

class Persona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad
        
    #como tenemos atributos privados no podemos aceder a ellos 
    # directamente. Para ello tenemos que hacer getters y setters
    # para poder modificarlos y acceder a ellos
    
    def set_nombre(self, new_nombre):
        self.__nombre = new_nombre
    
    def set_edad(self, new_edad):
        self.__edad = new_edad
        
    def get_nombre(self):
        return self.__nombre
    
    def get_edad(self):
        return self.__edad
        
# ==================================================================================================================================        
persona = Persona("Pepe", 24)

print(f"Antes me llamaba {persona.get_nombre()} y tenía {persona.get_edad()} años de edad\n")

print("<========================================================>\n")

persona.set_nombre("Miguel")
persona.set_edad(30)

print(f"Pero al pasar el tiempo cambié mi nombre a {persona.get_nombre()} y ahora tengo {persona.get_edad()} años de edad")


    
    