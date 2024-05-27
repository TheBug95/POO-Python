# Las properties se utilizan principalmente para funciones setters, getters y deletters

class Persona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad
        
    #como tenemos atributos privados no podemos aceder a ellos 
    # directamente. Para ello tenemos que hacer getters y setters
    # para poder modificarlos y acceder a ellos
    @property #Le dice que es un getter y que ademas no va a ser una funcion sino una propiedad, por tal motivo para llamarlo no neceitamos los parentesis
    def nombre(self):
        return self.__nombre
    
    @property
    def edad(self):
        return self.__edad
    
    @nombre.setter
    def nombre(self, new_nombre):
        self.__nombre = new_nombre
    
    @edad.setter
    def edad(self, new_edad):
        self.__edad = new_edad
    
    @nombre.deleter
    def nombre(self):
        del self.__nombre
        
    @edad.deleter
    def edad(self):
        del self.__edad
    
        
# ==================================================================================================================================        
persona = Persona("Pepe", 24)

print(f"Antes me llamaba {persona.nombre} y tenía {persona.edad} años de edad\n")

print("<========================================================>\n")

persona.nombre = "Miguel"
persona.edad = 30

print(f"Pero al pasar el tiempo cambié mi nombre a {persona.nombre} y ahora tengo {persona.edad} años de edad")

del persona.nombre
del persona.edad


    
    