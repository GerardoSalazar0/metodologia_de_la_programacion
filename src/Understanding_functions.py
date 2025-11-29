# Functions
"""
    Docstring for undestanding_functions

    Las funcione son bloques de codigos diseñadas
    para realizar una tarea especifica.

    Cuando queremos realizar la tarea que se ha definido en una funcion, 
    simplemente lo que hay que hacer es "llamar" elnombredelafuncion 
    que queremos ejecutar.

    "Definicion de funcion" o "Sintaxis general de una funcion"

"""
#Plabra reservada "def" + nombredelafuncion + parentesis
def greatting_paulo():
    """ 
    Docstring for greatting paulo

    Esta funcion saluda al paulo
    """
    print("wasa paulo")

greatting_paulo()

"""
    Vamos a hacer una funcion que pida al usuario first_name, middle_name, last_name
    La funcion debe regresar el nombre completo.
"""
# La funcion tiene 3 parametros
def create_full_name (first_name, middle_name, last_name):
    full_name= f"{first_name} { middle_name} {last_name}"
    return full_name.title()

user_first_name = input("Escribe tu primer nombre: ").strip().lower()
user_middle_name = input("Escribe tu segundo nombre: ").strip().lower()
user_last_name = input("Escribe tu apellido: ").strip().lower()

# Argumentos
# Argumentos posicionales
print(create_full_name(user_first_name, 
user_middle_name, 
user_last_name))

# Argumentos posicionales
generated_full_name = create_full_name(user_first_name, 
user_middle_name, 
user_last_name)
print(generated_full_name)


# Argumentos clave = keyword arguments
full_name_key = create_full_name(
    last_name= user_last_name,
    first_name = user_first_name,
    middle_name = user_middle_name,
)


# Investigar como juntar

#arcs, kwargs en python
# como explorar archivos (DICCIONARIOS, .txt, csv, archivos dr texto plano
#args por consola (sys)
#cli - commando linear interface
# oop - oriented objects profgraming
# testing
