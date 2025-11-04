#Numbers
"""
Integers

Los podemos sumar (+), restar (-), multiplicar (*), dividir (/),
elevar a una potencia (**2, **3, ..., etc)
obetener un módulo (%)

"""

""" No debes definir, es python we
"""
number_1 = 35
number_2 = 15

sum = number_1 + number_2
difference = number_1 - number_2
mult = number_1 * number_2
div = number_1 / number_2
power = number_1**2
modulo = number_1 % number_2

print("Sum:", sum, type(sum))
print("difference:", difference, type(difference))
print("Multiplication:", mult, type(mult))
print("Division:", div, type(div))
print("Power (2):", power, type(power))
print("Modulo:", modulo, type(modulo))

"""
Python respeta la jerarquía de las operaciones 

2+3*4 = 14
(2+3)*4 = 20

"""

# Floats - Numeros reales
"""
Floats

Los podemos sumar (+), restar (-), multiplicar (*), dividir (/),
elevar a una potencia (**2, **3, ..., etc)

Python llama float a cualquier número con punto decimal.
"""
print("Floats")
print(0.1 + 0.1) 
print(0.2-+ 0.2)
print(2 * 0.1)
print(0.1 * 2)

"""
 Tomar en cuenta que en ocasiones podemos obtener un numero arbitrario
 de numero decimal en la respuesta. 

 Eso pasa en muchos lenguajes de programación pero no debemos preocuparnos :).
"""
print(0.2 +0.1)
print(3 *0.1)


# Imprimir la edad de alguien

age= 33
message = "Charly tiene " + str(age) + " años "
print(message)


"""
TypeError: Pasa cuando Python no puede reconocer el tipo de informacion
que se esta utilizando

Build-in Method
        usar 
    - str() para convertir un numero a string
"""
message_f = f"Charly tiene {age} años"
#pone la edad en strings de una
print(message_f)

