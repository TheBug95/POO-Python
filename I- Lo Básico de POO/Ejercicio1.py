class Estudiante:
    def __init__(self, nombre, edad, grado):
        self.nombre = nombre
        self.edad = edad
        self.grado = grado
        
    def estudiar(self):
        print(f"El estudiante {self.nombre} está estudiando")
        
nombre = str(input("Proporcione nombre del estudiante: "))
edad = int(input("Proporcione la edad del estudiante: "))
grado = str(input("Proporcione el grado del estudiante: "))
         
estudiante = Estudiante(nombre, edad, grado)

print(f"""
      Datos del Estudiante: \n\n
      Nombre: {estudiante.nombre} \n
      Edad: {estudiante.edad} \n
      Grado: {estudiante.grado} \n
      """)

estudioso = True

while estudioso:
    estudiar = input(f"Para mandar al estudiante {estudiante.nombre} a estudiar, escriba la palabra -estudiar-: ")
    if estudiar.lower() == "estudiar":
        estudiante.estudiar()
        estudioso = False
    else:
        print(f"El estudiante {estudiante.nombre} se esta tocando las pelotas")
        