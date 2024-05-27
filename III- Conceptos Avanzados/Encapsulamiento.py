"""En Python el encapsulameinto viene dado por:
    - atributo_publico 
    - _atributo_protegido
    - __atributo_privado"""
    
    
# Para poder acceder a los elementos privados es obligado contruir los métodos getter y setter 
# ya que directamente es imposible por su naturaleza privada     

class MiClase:
    def __init__(self):
        self.__atributo_privado = "Soy un atributo privado"
    
    # Metodo privado
    def __metodo_privado(self):
        print("Soy un método Privado")
        

objeto = MiClase()

print(objeto.__atributo_privado) #==> Esto nos salta un error ya que el atributo es privado y no es posible accederlo de esta manera