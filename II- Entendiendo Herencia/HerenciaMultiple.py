#clase Padre
class Persona:
    def __init__(self, nombre, edad, nacionalidad, color_de_piel):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad
        self.color_de_piel = color_de_piel
        
    def hablar(self):
        print(f"Hola me llamo {self.nombre} y estoy hablando")
        
        
        
class Artista:
    def __init__(self, habilidad):
        self.habilidad = habilidad
        
    def mostrar_habilidad(self):
       return f"Esta es mi habilidad: {self.habilidad}"
        

class EmpleadoArtista(Persona, Artista):
    def __init__(self, nombre, edad, nacionalidad, color_de_piel, habilidad, salario, empresa):
        Persona.__init__(self, nombre, edad, nacionalidad, color_de_piel)
        Artista.__init__(self, habilidad)
        self.salario = salario
        self.empresa = empresa
        
    # COn este accedemos al método mostrar habilidad de una de las clases padre (Artista en este caso)
    def presentarse_artista(self):
        return super().mostrar_habilidad()
    
    # En este caso se accede al metodo de mostrar habilidad perteneciente a la clase hija, o sea esta misma clase
    def presentarse_empleado(self):
        return self.mostrar_habilidad()
    
    def mostrar_habilidad(self):
        return "No tengo ninguna habilidad"
        
        
        
empleado_artista = EmpleadoArtista(nombre="Miguel", edad=29, nacionalidad="cubano", color_de_piel="blanco", habilidad="Bailar", empresa="TEC", salario=800)

print(
    f"""
      Datos del Empleado-Artista: \n\n
      - Nombre: {empleado_artista.nombre} \n
      - Edad: {empleado_artista.edad} \n
      - Nacionalidad: {empleado_artista.nacionalidad} \n
      - Color de piel: {empleado_artista.color_de_piel} \n
      - Habilidad: {empleado_artista.habilidad} \n
      - Salario: {empleado_artista.salario} \n
      - Empresa: {empleado_artista.empresa}
      
      """
)

print(f"Como artista: {empleado_artista.presentarse_artista()} \n")
print("------------------------\n")
print(f"Como empleado: {empleado_artista.presentarse_empleado()} \n")


#Suponiendo que las clases de arriba estan empaquetadas y no podemos ver su implementacion
# y necesitamos saber si una clase hereda de otra, lo podemos hacer con el método -issubclass()- 

herencia = issubclass(EmpleadoArtista, Artista)
if herencia:
    print("Si hay herencia entre las clases")
else: 
    print("No existe herencia entre las clases")
    
    
# Supongamos ahora queremos saber que instancia correcponde a cual objeto, podemos hacerlo con el 
# método -isinstance()-

instancia = isinstance(empleado_artista, EmpleadoArtista)
instancia1 = isinstance(empleado_artista, Artista)
instancia2 = isinstance(empleado_artista, Persona)

response = "El objeto es una instancia de "

if instancia:
    response += "la clase EmpleadoArtista, "
else: 
    print("El objeto NO es una instancia de la clase EmpleadoArtista")
    
if instancia1:
    response += "la clase Artista, "
else: 
    print("El objeto NO es una instancia de la clase Artista")

if instancia2:
    response += "y la clase Persona"
else: 
    print("El objeto NO es una instancia de la clase Persona")
    
print(response)


