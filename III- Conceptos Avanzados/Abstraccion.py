 # Ocultar la complejidad interna de un sistema
 
class Auto:
    def __init__(self) -> None:
        self.__estado = "apagado"
        
    def encender(self):
        self.__estado = "encendido"
        print(f"El auto está {self.__estado}")
        
    def conducir(self):
        if self.__estado == "apagado":
            self.encender()
        print("Conduciendo el auto")
        
mi_auto = Auto()

mi_auto.conducir()
            
# Podemos darnos cuenta que en la funcion conducir aplicamos lo que es la abstraccion ya que con esta 
# ocultamos al usuario las diferentes funcionalidades que hay que procesar antes de conducir el auto

# Por ejemplo: Para conducir un auto, nosotros no necesitamos saber su funcionamiento interno del motor, 
# ni como está distribuido la instalación electrica del mismo simplemente que hay una llave para arrancarlo
# y los pedales de freno, acelerador y el selector de velicidades nada mas
 