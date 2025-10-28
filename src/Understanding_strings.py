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