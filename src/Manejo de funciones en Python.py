# Manejo de Funciones en Python
# Materia: Metodología de la Programación 
# Profesor: Charly Mercury 
# Estudiante: Gerardo Salazar de la Fuente (2530032) 1-1 IM  

# Resumen Ejecutivo:
"""
Las funciones en Python permiten dividir un programa en bloques de código 
reutilizables que realizan tareas específicas. Los parámetros son los nombres 
definidos en la función, mientras que los argumentos son los valores reales 
enviados al llamarla. Separar la lógica en funciones ayuda a mantener un código 
más claro, modular y fácil de probar. Además, devolver resultados con return 
es mejor que solo imprimir, ya que permite reutilizar esos valores en otras 
partes del programa. Este documento presenta varios problemas donde se diseñan 
funciones, se definen entradas, salidas, validaciones y se incluyen pruebas 
básicas para asegurar el correcto funcionamiento del código.
"""

# Buenas practicas:
"""
- Preferir funciones pequeñas que hagan una sola cosa (single responsibility).
- Evitar repetir código; si copias lógica, conviértela en función.
- Mantener funciones “puras” cuando sea posible: mismo input → mismo output.
- Documentar cada función con un comentario breve de su propósito.
- Usar nombres claros y descriptivos (calculate_bmi, not do_it).
"""


# PROBLEMA 1: Rectangle area and perimeter (basic functions)
# Descripción:
"""
Este problema consiste en calcular el área y el perímetro de un rectángulo 
usando dos funciones: una para el área y otra para el perímetro. El programa 
valida los datos proporcionados y, si son correctos, llama a las funciones y 
muestra los resultados al usuario. El objetivo es practicar el uso de funciones 
con parámetros y valores de retorno.

"""

# Inputs:
# - width (float)
# - height (float)

#Outputs:
# - "Area:" <value>
# - "Perimeter:" <value>

#Validations:
# - width > 0
# - height > 0


#Código: 
def calculate_area (width, height):
    return width* height
def calculate_perimeter (width, height):
    return (width+width+height+height)

width = 0
height = 0

try:
    width= float(input("Put width:"))
    height= float(input("Put height:"))
    if width>0 and height >0:
        try:
            area = calculate_area(width, height)
            perimeter = calculate_perimeter(width, height)
            print(f"area: {area}")
            print(f"perimeter: {perimeter}")
        except:
            print("Invalid input")
    else:
        print("0 cant be a data")
except:
    print("Invalid input")


# Test cases:
# 1) Normal:
"""
Put width:12
Put height:33
area: 396.0
perimeter: 90.0
"""

# 2) Border:
"""
Put width:876
Put height:543
area: 475668.0
perimeter: 2838.0
"""

# 3) Error:
"""
Put width:3
Put height:a
Invalid input
"""



# PROBLEMA 2: Grade classifier (function with return string)
# Descripción:
"""
Aquí se define una función que recibe una calificación numérica y devuelve 
una letra de evaluación (A-F). El programa principal verifica que la calificación 
esté dentro del rango válido y luego muestra la categoría obtenida. El propósito es 
aplicar condicionales y retornar cadenas según diferentes rangos.
"""

# Inputs:
#- score (0–100)

#Outputs:
# - "Score:" <score>
# - "Category:" <grade_letter>

#Validations:
# - 0 <= score <= 100


#Código: 
def classify_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

try:
    score = float(input("Enter score (0-100): "))

    if 0 <= score <= 100:
        grade = classify_grade(score)
        print(f"Score: {score}")
        print(f"Category: {grade}")
    else:
        print("Error: invalid input")

except:
    print("Error: invalid input")


# Test cases:
# 1) Normal:
"""
Enter score (0-100): 79
Score: 79.0
Category: C
"""

# 2) Border:
"""
Enter score (0-100): 99
Score: 99.0
Category: A
"""

# 3) Error:
"""
Enter score (0-100):
Error: invalid input
"""


# PROBLEMA 3: List statistics function (min, max, average)
# Descripción:
"""
En este problema se procesa una lista de números para obtener el mínimo, máximo y promedio. 
La función summarize_numbers calcula y regresa estos valores dentro de un diccionario. 
El programa convierte texto en una lista de números, valida que todos sean válidos y muestra 
los resultados. Sirve para practicar listas, conversiones y cálculos básicos.
"""

# Inputs:
# - numbers_text (string, e.g., "10,20,30")

#Outputs:
# - "Min:"
# - "Max:"
# - "Average:"

#Validations:
# - Input not empty
# - All values must be numeric
# - List must not be empty


#Código: 
def summarize_numbers(numbers_list):
    stats = {
        "min": min(numbers_list),
        "max": max(numbers_list),
        "average": sum(numbers_list) / len(numbers_list)
    }
    return stats


numbers_text = input("Enter numbers separated by commas: ")

if numbers_text.strip() == "":
    print("Error: invalid input")
else:
    try:
        parts = numbers_text.split(",")
        numbers_list = []

        for p in parts:
            number = float(p.strip())
            numbers_list.append(number)

        if len(numbers_list) == 0:
            print("Error: invalid input")
        else:
            stats = summarize_numbers(numbers_list)
            print(f"Min: {stats['min']}")
            print(f"Max: {stats['max']}")
            print(f"Average: {stats['average']}")

    except:
        print("Error: invalid input")



# Test cases:
# 1) Normal:
"""
3,5,7,9,8
Min: 3.0
Max: 9.0
Average: 6.4
"""

# 2) Border:
"""
Enter numbers separated by commas: 3,3,3,3
Min: 3.0
Max: 3.0
Average: 3.0
"""

# 3) Error:
"""
Enter numbers separated by commas: a
Error: invalid input
"""


# PROBLEMA 4: Apply discount list (pure function)
# Descripción:
"""
Se crea una función que aplica un descuento a cada precio dentro de una lista 
y devuelve una nueva lista sin modificar la original. El programa principal 
construye la lista desde texto, valida el porcentaje de descuento y muestra tanto 
los precios originales como los descontados. El objetivo es trabajar con funciones puras 
y manipulación de listas.
"""

# Inputs:
# - prices_text (string, e.g., "100,200,300")
# - discount_rate (0 to 1)

#Outputs:
# - "Original prices:"
# - "Discounted prices:"

#Validations:
# - List not empty
# - All prices > 0
# - 0 <= discount_rate <= 1


#Código: 
def apply_discount(prices_list, discount_rate):
    discounted = []
    for price in prices_list:
        new_price = price * (1 - discount_rate)
        discounted.append(new_price)
    return discounted

prices_text = input("Enter prices separated by commas: ")
discount_text = input("Enter discount rate (0 to 1): ")

if prices_text.strip() == "":
    print("Error: invalid input")
else:
    try:
        discount_rate = float(discount_text)

        if discount_rate < 0 or discount_rate > 1:
            print("Error: invalid input")
        else:
            parts = prices_text.split(",")
            prices_list = []

            for p in parts:
                price = float(p.strip())
                if price <= 0:
                    raise ValueError
                prices_list.append(price)

            if len(prices_list) == 0:
                print("Error: invalid input")
            else:
                discounted = apply_discount(prices_list, discount_rate)

                print(f"Original prices: {prices_list}")
                print(f"Discounted prices: {discounted}")

    except:
        print("Error: invalid input")


# Test cases:
# 1) Normal:
"""
Enter prices separated by commas: 22, 44, 67, 89
Enter discount rate (0 to 1): 0
Original prices: [22.0, 44.0, 67.0, 89.0]
Discounted prices: [22.0, 44.0, 67.0, 89.0]
"""

# 2) Border:
"""
Enter prices separated by commas: 65,78,90,25
Enter discount rate (0 to 1): 1
Original prices: [65.0, 78.0, 90.0, 25.0]
Discounted prices: [0.0, 0.0, 0.0, 0.0]
"""

# 3) Error:
"""
Enter prices separated by commas: two
Enter discount rate (0 to 1): 0
Error: invalid input
"""


# PROBLEMA 5: Greeting function with default parameters
# Descripción:
"""
Este problema define una función de saludo que combina un nombre y, un título como “Dr.” o “Eng.”. 
El programa prueba la función con argumentos posicionales y nombrados. 
El propósito es practicar parámetros con valores por defecto y construcción dinámica de textos.
"""

# Inputs:
# - name (string)
# - title (optional string)

#Outputs:
# - "Greeting:" <message>

#Validations:
# - name not empty


#Código: 
def greet(name, title=""):
    name = name.strip()
    title = title.strip()

    if title == "":
        full_name = name
    else:
        full_name = f"{title} {name}"

    return f"Hello, {full_name}!"

name_input = input("Enter name: ").strip()
title_input = input("Enter title (optional): ").strip()

if name_input == "":
    print("Error: invalid input")
else:
    greeting_message = greet(name_input, title_input)

    print(f"Greeting: {greeting_message}")


# Test cases:
# 1) Normal:
"""
Enter name: Jesus
Enter title (optional): Doc
Greeting: Hello, Doc Jesus!
"""

# 2) Border:
"""
Enter name: Jhon
Enter title (optional):
Greeting: Hello, Jhon!
"""

# 3) Error:
"""
Enter name:
Enter title (optional): Doc
Error: invalid input
"""


# PROBLEMA 6: Factorial function
# Descripción:
"""
El objetivo es calcular el factorial de un número usando una función que puede 
implementarse de forma iterativa o recursiva. El programa principal valida que el número 
sea correcto y muestra el resultado. Este ejercicio permite comprender los ciclos, llamadas 
recursivas y el manejo de casos base.
"""

# Inputs:
# - n (int)

#Outputs:
# - "n:" <n>
# - "Factorial:" <value>

#Validations:
# - n >= 0
# - Optional: n <= 20


#Código: 
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

value_text = input("Enter n: ")

try:
    n = int(value_text)

    if n < 0 or n > 20:
        print("Error: invalid input")
    else:
        result = factorial(n)
        print(f"n: {n}")
        print(f"Factorial: {result}")

except:
    print("Error: invalid input")



# Test cases:
# 1) Normal:
"""
Enter n: 8
n: 8
Factorial: 40320
"""

# 2) Border:
"""
Enter n: 2
n: 2
Factorial: 2
"""

# 3) Error:
"""
Enter n:
Error: invalid input
"""



# ======================================================================
# CONCLUSIONES 
# ======================================================================

"""
Las funciones permiten mantener el código organizado, modular y fácil de leer.
Además, devolver valores con return hace que los resultados puedan reutilizarse
en otros cálculos y evita depender solo de impresiones en pantalla. El uso de 
parámetros y valores por defecto vuelve las funciones más flexibles y fáciles 
de adaptar. Encapsular la lógica en funciones fue especialmente útil en tareas 
repetitivas como validaciones o cálculos. Finalmente, quedó clara la diferencia 
entre la lógica principal y las funciones de apoyo, mejorando la estructura del 
programa completo.
"""



# ======================================================================
# REFERENCIAS 
# ======================================================================

# https://www.freecodecamp.org/espanol/news/guia-de-funciones-de-python-con-ejemplos/ 
# https://funtech-co-uk.translate.goog/latest/what-does-def-mean-in-python?_x_tr_sl=en&_x_tr_tl=es&_x_tr_hl=es&_x_tr_pto=tc
# https://ellibrodepython.com/funciones-en-python 
# https://stackoverflow.com/questions/27009247/find-min-max-and-average-of-a-list 
# https://linuxhint.com/use-python-numpy-mean-min-max-functions/ 
# https://discuss.python.org/t/how-to-change-my-function-to-pure-function-in-python/15134 
# https://www.geeksforgeeks.org/python/factorial-in-python/ 
# https://www.youtube.com/watch?v=g78juF9pB_w 
# https://aulavirtual.espol.edu.ec/courses/4558/pages/funciones-en-python 
# https://www.youtube.com/watch?v=9k91jETchkI 



# ======================================================================
# REPOSITORIO DE GITHUB
# ======================================================================

# https://github.com/GerardoSalazar0/metodologia_de_la_programacion/blob/main/src/Manejo%20de%20funciones%20en%20Python.py