# MRO (Método de Resolución de Orden) basicamente ahce referencia al orden en que python busca métodos 
# y tributos en las clases 

# Esto es un aspecto crucial de la herencia ya que si tenemos en una herencia, clases que comparten métodos
# llamados igual o atributos iguales, tenemos que saber que es lo que hace python en este caso

# En este caso usamos la funcion super(). Esta contacta al MRO para saber que informacion coger y de donde 


class A:
    def hablar(self):
        print("Hola desde A")
        
        
class B(A):
    def hablar(self):
        print("Hola desde B")


class C(A):
    def hablar(self):
        print("Hola desde C")


class D(B, C):
    def hablar(self):
        print("Hola desde D")
        
        
#       _______
#      |__A___|           level 1
#   __/_      \__
#  |_B_|     |_C_|        Level 2
#   \        /
#    \ ____ /
#     |_D_|               Level 3

# Primeramente usarímaos el método hablar de la clase en la que estamos, en este caso 
# usariamos el de la clase D. Ahora supongamos que en la clase D este método no de encuentra definido

# ------------- ¿ De cuál de las clases que hereda la clase D se usará el método habla ?---------------#

#Teniendo en cuenta lo anterior como D hereda de B y C primeramente se va a utilizar 
# el método hablar de la clase B, si en B no exitiera el método que estamos tratando de utilizar 
# usaríamos entonces el de la clase C y por último, si no existiera este método ni en B ni en C
# entonces directamente usaríamos el de la clase A   

#---------------------------------------------------------------------------------------------------------#
#Imaginemos que tenemos esta otra estructura

"""
class A:
    def hablar(self):
        print("Hola desde A")
        
class F:
    def hablar(self):
        print("Hola desde F")
        
        
class B(A):
    def hablar(self):
        print("Hola desde B")


class C(F):
    def hablar(self):
        print("Hola desde C")


class D(B, C):
    def hablar(self):
        print("Hola desde D")
"""
#     ____    ____
#    |_A_|   |_F_|        level 1
#   __/_      \__
#  |_B_|     |_C_|        Level 2
#   \        /
#    \ ____ /
#     |_D_|               Level 3

#En este caso empezmos a buscar buscar desde la clase D, en el caso que el método "hablar()" no se encuentra en este va a ir 
# automáticamente a la primera clase de donde hereda a buscar el método que queremos, en este caso es la clase B

# Ahora supongamos que en la clase B tampoco se encuentra el método que necesitamos utilizar, en este caso no vamos a 
# buscar en C, que seria la clase que le sigue, en este caso sigue por la rama a buscar en A (que es la clase de la que hereda B)
# a ver si esa clase tiene el método que necesitamos utilizar. Si buscamos en A y en esta no se encuentra el metodo a 
# utilizar entonces en este caso vamos a la clase C y asi sucesivamente hasta llegar a F para encontrar el método que necesitamos 

#----------------------------------------------------------------------------------------------------------------------------------#

# Todo esto podemos verlo a travez de la linea siguiente:
print(D.mro())
#Teniendo en cuenta las primeras combinaciones sin la clase F
#[<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]

#----------------------------------------------------------------------------------------------------------------------------------#

# Imaginemos ahora que queremos desde la instancia del objeto de la clase D utilizar el método "hablar" que se encuentra en la clase B
# esto aun cuando en la clase D esté presente un método "hablar" propio de esta clase. Lo que tenemos que hacer es lo siguiente:

d = D() #instanciamos la clase que necesitamos

B.hablar(d) # Pedimos el método a la clase que necesitamos haciéndolo directamente y pasándole la instancia del objeto de la clase D