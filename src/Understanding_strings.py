"""
Un string es de manera sencilla una serie de caracteres

    En python todo lo que se ENCUENTRE DENTRO DE COMILLAS SIMPLES ' '
    O DOBLES COMILLAS " " 
    es considerado un STRING

    por ejemplo:

    "Esto es un string"
    'Esto tambien es un string'

    'Le dije a mi amigo python, "¡Python es mi lenguaje favorito!"'
    " El lenguaje 'PYTHON' lleva el nombre en honor a Monty Python, no por la serpiente. "

"""

# STRINGS

name = "clase de programación"
print(name)
print()
print(name.title()) # Convierte la primera letra de cada palabra en mayúscula
print()
print(name)
print()


"""

    Un método es una acción que python puede realizar en un fragmento
    de datos o sobre una variable.

    El punto (.) después de una variable string seguido del método title() dice que
    se tiene que ejecutar el método title() en la variable name.

    Todos los métodos van seguidos de paréntesis porque en ocasiones necesitan información
    adicional para funcionar, lo cual iría dentro de los paréntesis.

    En esta ocasión el método .title() no requiere información adicional para ejecutarse.

"""

# OTROS MÉTODOS

print("Para mayúsculas: ", name.upper())
print("Para minúsculas: ", name.lower())


# CONCATENACIÓN DE STRINGS

first_name = "Charly"
last_name = "Mercury"
full_name = first_name + " " + last_name
print(full_name)

print("Hola", "!" + full_name.title() + "!")   

message = "Hola", "!" + full_name.title() + "!"
print(message)

# Whitespaces

"""
    Los whitespace se refiere a cualquier caracter que no se imprime,
    es decir, un espacio en blanco, un tabulador o un salto de línes. Los whitespaces
    se utilizan comunmente para organizar las salidad en pantalla de tal manera que sea
     mas amigable de ver pasra los usuarios.
"""


print("Python")
print ("\tPython") #Tabulador antes de Python
print ("\t\tPython") #Doble tabulador antes de Python
print("Lenguages: \nPython\nC\nJavaScript")
# \n es un salto de linea
# \t es el tabulador

# Eliminación de Espacios en Blanco
print("\n\nEliminación de espacios en blanco")
favorite_lenguage = " python "
print(favorite_lenguage)
print(favorite_lenguage.rstrip()) #Elimina espacios a la derecha
print(favorite_lenguage.lstrip()) #Elimina espacios a la izquierda
print(favorite_lenguage.strip()) #Elimina todos los espacios 

# Syntx Error con Strings
message = "Una fortaleza de python es su comunidad activa"
print(message)

message_ = "Una fortaleza de 'python' es su comunidad activa" 
print(message_)


#f-strings
full_name1 = "charly"
last_name1 = "mercury"
full_name1= f"[first_name1. title() (last_name1)]"
print(full_name)






#Ejercicio de f-strings
full_name2 = "El Pirata de Culiacan"
frase_famosa = "'Así nomas uedó'"
nombreyfrase = f"{full_name2} una vez dijo {frase_famosa}"
print(nombreyfrase)


