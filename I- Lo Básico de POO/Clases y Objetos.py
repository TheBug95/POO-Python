### Esto es FATAL ####

celular1_marca = "samsung"
celular2_marca = "apple"
celular3_marca = "huawei"

celular1_modelo = "S23"
celular2_modelo = "iPhone 15 pro"
celular3_modelo = "P20 pro"

celular1_camaraT = "48MP"
celular2_camaraT = "48MP"
celular3_camaraT = "12MP"

celular1_camaraF = "24MP"
celular2_camaraF = "24MP"
celular3_camaraF = "8MP"

print(celular2_camaraF)

##------------- Sintaxis-----------##

class NombreClase():
    propiedad1 = "valor1"
    propiedad2 = "valor2"
    propiedad3 = "valor3"
    
    
#---------------------------------#

class Celular():
    marca = "Samsung"
    modelo = "S23"
    camara = "48MP"
    
celular_mio = Celular()

print("La capacidad de la cámara de mi celular es de: ", celular_mio.camara)
print("La marca de mi celular es: ", celular_mio.marca)
print(f"El modelo de mi celular marca - {celular_mio.marca} es {celular_mio.modelo}")

# Los atributos de la clase anterior son estáticos por lo que siempre cada vez que cree el objetos
# se va a crear por defecto con los valores definidos anteriormente, por lo que necesitamos una forma 
# donde se pueda crear varios celulares con diferentes especificaciones

# Creamos constructores y con ello nos quitamos ese problema de encima

class Celular:
    #Constructor de la clase
    def __init__(self, marca, modelo, camara):
        self.marca = marca
        self.modelo = modelo
        self.camara = camara
        
celular_mio2 = Celular("Samsung", "S23", "48MP")
celular_mio3 = Celular("Apple", "15 Pro Max", "12MP")

print("La marca de mi celular 2 es: ", celular_mio2.marca)
print("La marca de mi celular 3 es: ", celular_mio3.marca)