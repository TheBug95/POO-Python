# Permite acceder a la clase hija a todos los metodos y tener las propiedades de la clase padre 

#clase Padre
class Persona:
    def __init__(self, nombre, edad, nacionalidad, color_de_piel):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad
        self.color_de_piel = color_de_piel
        
    def hablar(self):
        print(f"Hola me llamo {self.nombre} y estoy hablando")

# pass -> lo pongo cuando no deseo implementar algo para que este no de error por si en algun momento se llama 

#clase Hija
class Empleado(Persona):
    def __init__(self, nombre, edad, nacionalidad, color_de_piel, trabajo, salario, puesto_laboral):
        super().__init__(nombre, edad, nacionalidad, color_de_piel)
        self.trabajo = trabajo
        self.salario = salario
        self.puesto_laboral = puesto_laboral

    #redefinimos el método hablar
    def hablar(self):
        print(f"Hola me llamo {self.nombre} y no quiero hablar ahora mismo")
        
        

empleado = Empleado(nombre = "Miguel", nacionalidad = "cubano", color_de_piel = "blanco", edad = 29, trabajo = "Estudiante de Maestría", puesto_laboral = "Investigador", salario = 800  )

persona = Persona(nombre = "Lisuan", nacionalidad = "cubana", color_de_piel = "blanca", edad = 30) 


print(f"""
      Datos de la Persona: \n\n
      - Nombre: {persona.nombre} \n
      - Edad: {persona.edad} \n
      - Nacionalidad: {persona.nacionalidad} \n
      - Color de piel: {persona.color_de_piel} \n\n
      
      Por ser la clase padre solamente podemos acceder a sus atributos

      """)

print("<========================================================================>")


print(f"""
      Datos del Empleado: \n\n
      - Nombre: {empleado.nombre} \n
      - Edad: {empleado.edad} \n
      - Nacionalidad: {empleado.nacionalidad} \n
      - Color de piel: {empleado.color_de_piel} \n
      - Trabajo: {empleado.trabajo} \n
      - Puesto Laboral: {empleado.puesto_laboral} \n\n
      
      Por ser la clase hija tiene acceso a los atributos de si misma y los de la clase padre
      
      """)

print("<========================================================================>")

empleado.hablar()

persona.hablar()
