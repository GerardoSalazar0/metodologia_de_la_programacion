message = "This is my first variable!"
another_message = "Variables are used to store information"

print(message)
print(another_message)

print(message, another_message)
print(another_message, message)

"""
    Los nombres de las variables deben nombrarse solo con:
    - letras, numeros y guión bajos
    - deben comenzar con unas letras o guión bajo pero no con números:
    (correcto) message1, (incorrect) 1_message
    - no utilizar espacios para separar palabras en variables
    - no utilizar palabras reservadas por python para nombrar variables
    - los nombres deben ser cortos, pero descriptivos
    - letras minúsculas


"""

#
python_message = "Hola amiko Python"
print(python_message, "Charly")
print(python_message, "Mercury")
print(python_message, "Paulo Coelho")



"""
print(python_mesage)

Traceback: Es un registro de donde el intérprete tuvo problemas para ejecutar el código.

Ejemplo:

Traceback (most recent call last):
  File "C:/Users/gerar/Documents/python_proyects/test_project/src/Understanding_variables.py", line 29, in <module>
    print(python_mesage)
          ^^^^^^^^^^^^^
NameError: name 'python_mesage' is not defined. Did you mean: 'python_message'?

NameError: Significa que olvidamos establecer el valor de una variable antes de utilizar
o cometimos un error al ingresar el nombre de la variable.

"""
