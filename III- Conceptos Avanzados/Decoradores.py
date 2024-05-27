# Un decorador es una funcion que agarra una funcion, le agraga funcionalidades, antes de ejecutarla o 
# despues de ejecutarla, o ambas y devuelve la nueva función ya modificada

def decorator(funcion):
    def funcion_modificada():
        print("Antes de llamar a la función")
        
        funcion()
        
        print("Despues de llamar a la función")
        
    return funcion_modificada


# def saludo():
#     print("Hola Mundo!!!!")
    
# hello = decorator(saludo) #Con esto llamamos al decorador pero no es lanorma para esto
# hello()

@decorator #LLamada al decorador
def saludo():
    print("Hola Mundo!!!!")
    
saludo()



