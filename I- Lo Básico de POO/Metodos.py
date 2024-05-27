# Todas las funciones creadas dentro de las clases se llaman métodos 

class Celular:
    def __init__(self, marca, modelo, camara):
        self.marca = marca
        self.modelo = modelo
        self.camara = camara
        
    def tomar_foto(self):
        print(f"Foto tomada con éxito, desde tu teléfono {self.marca} {self.modelo} con una cámara de {self.camara}  ")
        
        
celular = Celular("Samsung", "S23 Ultra", "32MP")

celular.tomar_foto()