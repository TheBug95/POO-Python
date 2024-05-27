# El polimorfismo basicamente es hacer cuando nosotros le demos un metodo a un objeto este se comporte de diferente 
# manera en concordancia con sus propiedades 

# Envío el mismo mensaje solo que el resultado es diferente

class Animal():
    def sonido(self):
        pass
    
class Gato(Animal):
    def sonido(self):
        return "Miau"
    
class Perro(Animal):
    def sonido(self):
        return "Guau"
    
# ahora si yo defino los diferentes objetos (Perro y Gato) y llamamos a la funcion sonido vamos a tener diferentes respuestas 
# dependiendo del objeto

perro = Perro()
gato = Gato()

print(perro.sonido())
print(gato.sonido())

# Como vemos arriba la llamada es al mismo método (sonido()) pero la respuesta es diferente

# Ahora veamos un ejemplo con polimorfismo de funciones

def hacer_sonido(animal):
    print(animal.sonido())
    
print("=========================================")    

hacer_sonido(perro)
hacer_sonido(gato)

# Como podemos ver se usó la misma función pero los resultados se diferencian teniendo en cuenta el objeto utilizado