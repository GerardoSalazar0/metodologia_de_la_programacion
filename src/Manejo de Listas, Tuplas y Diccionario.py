# Manejo de Listas, Tuplas y Diccionarios en Python
# Materia: Metodología de la Programación 
# Profesor: Charly Mercury 
# Estudiante: Gerardo Salazar de la Fuente (2530032) 1-1 IM  

# Resumen Ejecutivo:
"""
En Python, las listas, las tuplas y los diccionarios son estructuras esenciales
para organizar y manejar información. Las listas permiten almacenar elementos
ordenados y mutables, ideales cuando se necesita agregar, eliminar o modificar
datos con frecuencia. Las tuplas también son ordenadas, pero son inmutables, lo
que las hace útiles para datos fijos como coordenadas, fechas o configuraciones
que no deben cambiar. Los diccionarios relacionan claves con valores y permiten
búsquedas rápidas y directas sin recorrer toda una estructura.

Este documento explica cada problema usando un diseño claro de entradas, salidas
y validaciones, mostrando cómo aplicar estas estructuras en contextos prácticos
como catálogos, registros de estudiantes, análisis de palabras y operaciones
básicas de contactos. También se resalta la importancia de validar datos antes
de procesarlos, comprender la mutabilidad, y elegir la estructura adecuada según
la necesidad. Con estos ejemplos, el estudiante aprende cuándo usar listas,
tuplas o diccionarios y cómo estos apoyan programas confiables y organizados.
"""


# Buenas practicas:
"""
En el trabajo con estructuras de datos es importante aplicar buenas prácticas
que hagan el código más claro, seguro y fácil de mantener. Las listas deben
usarse cuando se necesite agregar, eliminar o modificar elementos con
frecuencia, aprovechando su naturaleza mutable. Las tuplas resultan ideales
para datos que deben permanecer fijos, evitando cambios accidentales y
garantizando estabilidad en la información.

Los diccionarios permiten acceder rápidamente a valores usando claves
descriptivas, por lo que conviene emplearlos cuando se manejen registros,
catálogos o cualquier dato que deba localizarse por nombre o identificador.
Es importante evitar modificar una lista mientras se recorre en un for, ya que
esto puede producir errores o comportamientos inesperados. También es clave
mantener nombres de variables y claves claros y significativos, así como mostrar
mensajes comprensibles para el usuario. Estas prácticas fomentan programas más
organizados, legibles y fáciles de depurar.
"""


# PROBLEMA 1: Shopping list basics (list operations)
# Descripción:
"""
Este programa trabaja con una lista de productos. A partir de un texto inicial
con productos separados por comas, crea una lista, agrega un nuevo producto
al final y verifica si un producto específico está dentro de la lista. También
muestra el total de elementos.
"""

# Inputs:
#- initial_items_text: string con productos separados por comas.
#- new_item: string, producto a agregar.
#- search_item: string, producto a buscar.

#Outputs:
#- "Items list:" <items_list>
#- "Total items:" <len_list>
#- "Found item:" true|false

#Validations:
#- initial_items_text no debe estar vacío después de strip().
#- Cada producto debe limpiarse con strip().
#- new_item y search_item no deben estar vacíos.
#- Si initial_items_text es solo espacios, es un error.

#Código: 
initial_items_text = input("Enter initial items (separed by a comma): ").strip()
new_item = input("Enter new item: ").strip()
search_item = input("Enter item to search: ").strip()

# Validation for initial text
if initial_items_text == "":
    print("Error: invalid input")
else:
    # Convert text to list
    items_list = initial_items_text.split(",")
    
    # Del spaces
    cleaned_list = []
    for item in items_list:
        cleaned_item = item.strip()
        if cleaned_item != "":
            cleaned_list.append(cleaned_item)
    
    # Validate new and search items
    if new_item == "" or search_item == "":
        print("Error: invalid input")
    else:
        # Append new item
        cleaned_list.append(new_item)
        
        # Total items
        total_items = len(cleaned_list)
        
        # Check if search item exists
        is_in_list = search_item in cleaned_list
        
        # Output
        print("Items list:", cleaned_list)
        print("Total items:", total_items)
        print("Found item:", str(is_in_list).lower())


# Test cases:
# 1) Normal:
"""
Enter initial items (separed by a comma): banana, apple, orange
Enter new item: pear
Enter item to search: apple
Items list: ['banana', 'apple', 'orange', 'pear']
Total items: 4
Found item: true """

# 2) Border:
"""Enter initial items (separed by a comma): apple
Enter new item: apple
Enter item to search: apple
Items list: ['apple', 'apple']
Total items: 2
Found item: true"""

# 3) Error:
"""
Enter initial items (separed by a comma): pear, pineapple, bread
Enter new item:
Enter item to search: bread
Error: invalid input"""

# PROBLEMA 2: Points and distances with tuples
#Descripción:
"""Usa tuplas para representar dos puntos en un plano 2D: (x1, y1) y (x2, y2).
El programa debe:
1) Crear dos tuplas point_a y point_b a partir de entradas numéricas.
2) Calcular la distancia euclidiana entre ambos puntos.
3) Crear una nueva tupla midpoint con el punto medio entre ellos."""

# Inputs:
#- x1, y1, x2, y2 (float; coordenadas de los puntos).

#Outputs:
#- "Point A:" (x1, y1)
#- "Point B:" (x2, y2)
#- "Distance:" <distance>
#- "Midpoint:" (mx, my)

#Validations:
#- Verificar que las 4 entradas se puedan convertir a float.
#- No se requieren restricciones adicionales en el rango.

#Código: 
try:
    x1 = float(input("Enter x1: "))
    y1 = float(input("Enter y1: "))
    x2 = float(input("Enter x2: "))
    y2 = float(input("Enter y2: "))

    point_a = (x1, y1)
    point_b = (x2, y2)

    distance = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
    midpoint = ((x1 + x2)/2, (y1 + y2)/2)

    print("Point A:", point_a)
    print("Point B:", point_b)
    print("Distance:", distance)
    print("Midpoint:", midpoint)

except ValueError:
    print("Error: Invalid numeric input.")


# Test cases:
# 1) Normal:
"""
Enter x1: 2
Enter y1: 5
Enter x2: 7
Enter y2: 9
Point A: (2.0, 5.0)
Point B: (7.0, 9.0)
Distance: 6.4031242374328485
Midpoint: (4.5, 7.0)"""

# 2) Border:
""" Enter x1: 23
Enter y1: 3
Enter x2: 0
Enter y2: 0
Point A: (23.0, 3.0)
Point B: (0.0, 0.0)
Distance: 23.194827009486403
Midpoint: (11.5, 1.5)"""


# 3) Error:
""" 
Found item: true
Enter x1: 4
Enter y1: 7
Enter x2: 2
Enter y2:
Error: Invalid numeric input."""

# PROBLEMA 3: Product catalog with dictionary
# Descripción:
"""Administra un pequeño catálogo de productos usando un diccionario donde:
- clave: nombre del producto (string)
- valor: precio unitario (float)

El programa debe:
1) Crear un diccionario inicial con al menos 3 productos.
2) Leer el nombre de un producto y la cantidad a comprar.
3) Calcular el total a pagar si el producto existe.
4) Si el producto no existe, mostrar un mensaje de error."""

#Inputs:
#- product_name (string)
#- quantity (int)

#Outputs:
#Si el producto existe:
#- "Unit price:" <unit_price>
#- "Quantity:" <quantity>
#- "Total:" <total_price>

#Si el producto no existe:
#- "Error: product not found"

#Validaciones:
#- quantity > 0
#- product_name no vacío tras strip()
#- Verificar si product_name está en el diccionario


#Código: 
product_prices = {"apple": 10.0, "milk": 25.0, "bread": 35.0}

product_name = input("Enter product name (apple, milk or bread): ").strip()
quantity_input = input("Enter quantity: ")

try:
    quantity = int(quantity_input)

    if product_name == "":
        print("Error: product name cannot be empty.")
    elif quantity <= 0:
        print("Error: quantity must be greater than 0.")
    else:
        if product_name in product_prices:
            unit_price = product_prices[product_name]
            total_price = unit_price * quantity

            print("Unit price:", unit_price)
            print("Quantity:", quantity)
            print("Total:", total_price)
        else:
            print("Error: product not found")

except ValueError:
    print("Error: quantity must be a number.")

# Test cases:
# 1) Normal:
""" Enter product name (apple, milk or bread): apple
Enter quantity: 4
Unit price: 10.0
Quantity: 4
Total: 40.0"""

# 2) Border:
"""Enter product name (apple, milk or bread): bread
Enter quantity: 1
Unit price: 35.0
Quantity: 1
Total: 35.0"""

# 3) Error:
""" Enter product name (apple, milk or bread): milk
Enter quantity: 0
Error: quantity must be greater than 0."""


#  PROBLEMA 4: Student grades with dict and list
# Descripción:
"""Administra las calificaciones de un grupo usando un diccionario:
- clave: nombre del estudiante (string)
- valor: lista de calificaciones (list of float)"""

#El programa debe:
#1) Crear un diccionario con al menos 3 estudiantes, cada uno con una lista de calificaciones.
#2) Leer el nombre de un estudiante.
#3) Calcular el promedio de sus calificaciones.
#4) Indicar si el estudiante está aprobado (average >= 70.0) usando un booleano is_passed.

#Inputs:
#- student_name (string)

#Outputs:
#Si el estudiante existe:
#- "Grades:" <grades_list>
#- "Average:" <average>
#- "Passed:" true|false

#Si el estudiante no existe:
#- "Error: student not found"

#Validations:
#- student_name no vacío tras strip()
#- Verificar si student_name es clave en el diccionario
#- La lista de calificaciones no debe estar vacía antes del promedio

#Código:
student_grades = {"josue": [90.0, 85.0, 92.0], "mike": [100.0, 60.0, 75.0],
"vitor": [55.0, 65.0, 50.0]}

student_name = input("Enter student name (josue, mike, vitor): ").strip().lower()

if student_name == "":
    print("Error: no student name")
else:
    if student_name in student_grades:
        grades_list = student_grades[student_name]

        if len(grades_list) == 0:
            print("Error: this student has no grades.")
        else:
            average = sum(grades_list) / len(grades_list)
            is_passed = average >= 70.0

            print("Grades:", grades_list)
            print("Average:", average)
            print("Passed:", is_passed)
    else:
        print("Error: student not found")

if student_name == "josue":
    print("date de baja vro")


# Test cases:
# 1) Normal:
"""Enter student name (josue, mike, vitor): josue
Grades: [90.0, 85.0, 92.0]
Average: 89.0
Passed: True
date de baja vro"""

# 2) Border:
"""Enter student name (josue, mike, vitor): vitor
Grades: [55.0, 65.0, 50.0]
Average: 56.666666666666664
Passed: False"""

# 3) Error:
"""Enter student name (josue, mike, vitor): jose
Error: student not found"""

#  PROBLEMA 5: Word frequency counter (list + dict)
# Descripción:
"""Cuenta la frecuencia de cada palabra en una oración usando:
- Una lista de palabras.
- Un diccionario donde:
  - clave: palabra (string)
  - valor: frecuencia (int)"""

#El programa debe:
"""1) Leer una oración.
2) Convertirla a minúsculas y separarla en una lista de palabras.
3) Construir un diccionario de frecuencias.
4) Mostrar el diccionario completo y la palabra más frecuente."""

#Input:
#- sentence (string)

# Outputs:
#- "Words list:" <words_list>
#- "Frequencies:" <freq_dict>
#- "Most common word:" <word>

# Validations:
#- sentence no vacía tras strip()
#- Manejo simple de puntuación usando replace() para quitar .,!? (decisión documentada)
#- Lista de palabras no vacía tras split()

# Código: 
sentence = input("Enter a sentence: ").strip()

if sentence == "":
    print("Error: there isn't a sentence.")
else:
    clean_text = sentence.lower()

    # Remove simple punctuation 
    """ I prefer to use replace() to remove .,!? 
    because it is straightforward and easy to understand.
    It is used to replace substrings within 
    a text string with other specified substrings.
"""

    clean_text = clean_text.replace(".", "")
    clean_text = clean_text.replace(",", "")
    clean_text = clean_text.replace("!", "")
    clean_text = clean_text.replace("?", "")

    words_list = clean_text.split()

    if len(words_list) == 0:
        print("Error: no words found.")
    else:
        freq_dict = {}

        for word in words_list:
            if word in freq_dict:
                freq_dict[word] += 1
            else:
                freq_dict[word] = 1

        # Find most common word
        most_common_word = ""
        highest_count = 0

        for word in freq_dict:
            if freq_dict[word] > highest_count:
                highest_count = freq_dict[word]
                most_common_word = word

        print("Words list:", words_list)
        print("Frequencies:", freq_dict)
        print("Most common word:", most_common_word)


# Test cases:
# 1) Normal:
"""
Enter a sentence: hoy es martes y los martes hay promo en el pollo feliz que vivan los martes
Words list: ['hoy', 'es', 'martes', 'y', 'los', 'martes', 'hay', 'promo', 'en', 'el', 'pollo', 'feliz', 'que', 'vivan', 'los', 'martes']
Frequencies: {'hoy': 1, 'es': 1, 'martes': 3, 'y': 1, 'los': 2, 'hay': 1, 'promo': 1, 'en': 1, 'el': 1, 'pollo': 1, 'feliz': 1, 'que': 1, 'vivan': 1}
Most common word: martes"""

# 2) Border:
"""
Words list: ['alo', 'alo']
Frequencies: {'alo': 2}
Most common word (the 1st if there aren't a common): alo"""


# 3) Error:
"""
Enter a sentence:
Error: there isn't a sentence."""



# PROBLEMA 6: Simple contact book (dictionary CRUD)
# Descripción:
"""Implementa un mini "contact book" usando un diccionario donde:
- clave: nombre de contacto (string)
- valor: número de teléfono (string)"""

# El programa debe:
"""
1) Crear un diccionario inicial con algunos contactos.
2) Leer una acción action_text ("ADD", "SEARCH" o "DELETE").
3) Según la acción:
   - "ADD": lee name y phone, agrega o actualiza el contacto.
   - "SEARCH": lee name y muestra el teléfono si existe.
   - "DELETE": lee name y elimina el contacto si existe.
4) Mostrar un mensaje indicando el resultado de la operación."""

# Inputs:
"""- action_text (string; "ADD", "SEARCH" o "DELETE")
- name (string; depende de la acción)
- phone (string; solo para "ADD")
"""

# Outputs:
"""- Para "ADD":
  - "Contact saved:" name, phone
- Para "SEARCH":
  - Si existe: "Phone:" <phone>
  - Si no existe: "Error: contact not found"
- Para "DELETE":
  - Si existe: "Contact deleted:" name
  - Si no existe: "Error: contact not found"
  """

# Validations:
"""- Normalizar action_text a mayúsculas.
- Verificar que action_text sea una de las opciones válidas.
- name no vacío tras strip().
- Para "ADD": phone no vacío tras strip().
"""


# Código:
contacts = {
    "elpepe": "1234567890",
    "juancarlos": "9876543210",
    "vegetta": "7777777777"
}

action_text = input("Enter action (ADD, SEARCH, DELETE): ").strip().upper()

if action_text not in ["ADD", "SEARCH", "DELETE"]:
    print("Error: invalid action.")
else:
    name = input("Enter contact name (elpepe, juancarlos, vegetta): ").strip()

    if name == "":
        print("Error: name cannot be empty.")
    else:
        if action_text == "ADD":
            phone = input("Enter phone number: ").strip()

            if phone == "":
                print("Error: phone cannot be empty.")
            else:
                contacts[name] = phone
                print("Contact saved:", name, phone)

        elif action_text == "SEARCH":
            if name in contacts:
                print("Phone:", contacts[name])
            else:
                print("Error: contact not found")

        elif action_text == "DELETE":
            if name in contacts:
                contacts.pop(name)
                print("Contact deleted:", name)
            else:
                print("Error: contact not found")


# Test cases:
# 1) Normal:
"""
Enter action (ADD, SEARCH, DELETE): SEARCH
Enter contact name (elpepe, juancarlos, vegetta): vegetta
Phone: 7777777777"""

# 2) Border:
"""Enter action (ADD, SEARCH, DELETE): DELETE
Enter contact name (elpepe, juancarlos, vegetta): elpepe
Contact deleted: elpepe"""

# 3) Error:
"""Enter action (ADD, SEARCH, DELETE): PLAY
Error: invalid action."""


# ======================================================================
# CONCLUSIONES 
# ======================================================================

"""
El uso de listas, tuplas y diccionarios en Python permite resolver una gran
variedad de problemas de manera organizada, eficiente y estructurada. Cada
estructura ofrece diferentes ventajas: las listas destacan por su flexibilidad
al permitir agregar, modificar o eliminar elementos; las tuplas protegen datos
que no deben cambiar, dando estabilidad y seguridad; y los diccionarios facilitan
la búsqueda directa mediante claves, lo que hace más simple manejar catálogos,
registros y colecciones complejas.

A lo largo de los seis programas desarrollados, se aplicaron estas estructuras
en situaciones reales como listas de compras, puntos en un plano, catálogos,
calificaciones, análisis de texto y libretas de contactos. Esto demuestra cómo
escoger la estructura adecuada influye directamente en la claridad y eficiencia
del código. Además, el proceso reforzó la importancia de validar entradas, manejar
errores y mostrar mensajes comprensibles para asegurar que los programas sean
robustos y fáciles de usar. En conjunto, estos ejercicios fortalecen la lógica
de programación y la capacidad de diseñar soluciones prácticas con fundamentos
sólidos en Python.
"""



# ======================================================================
# REFERENCIAS 
# ======================================================================

# https://developer.mozilla.org/es/docs/Web/JavaScript/Reference/Global_Objects/String/replace
# https://www.youtube.com/watch?v=CV2dDtuwCCM
# https://www.luisllamas.es/que-es-una-tupla/ 
# https://ellibrodepython.com/diccionarios-en-python 
# https://www.w3schools.com/python/ref_dictionary_get.asp 
# https://www.freecodecamp.org/espanol/news/python-lista-append-como-agregar-elementos-a-una-lista-explicado-con-ejemplos/ 
# https://www.picuino.com/es/python-booleanos.html
# https://ellibrodepython.com/
# https://www.pythonparatodo.com/?p=272 
# https://keepcoding.io/blog/metodos-para-contar-palabras-en-python/
# https://www.w3schools.com/python/ref_string_replace.asp 
# https://www.programiz.com/python-programming/methods/string/replace 
# https://keepcoding.io/blog/agenda-de-contactos-en-python/ 




# ======================================================================
# REPOSITORIO DE GITHUB
# ======================================================================

