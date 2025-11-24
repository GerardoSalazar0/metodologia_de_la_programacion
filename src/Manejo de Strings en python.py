# Manejo de strings en Python  
# Materia: Metodología de la Programación 
# Profesor: Charly Mercury 
# Estudiante: Gerardo Salazar de la Fuente (2530032) 1-1 IM  

# Resumen Ejecutivo:

"""
En Python, un string es un tipo de dato inmutable compuesto por una secuencia
de caracteres. Al ser inmutable, cualquier modificación genera una nueva cadena.
Python incluye operaciones fundamentales como concatenación, slicing, búsqueda,
reemplazo, normalización y formateo, que permiten procesar información como
nombres, correos, contraseñas, etiquetas y texto general.
Validar y limpiar las entradas del usuario es crucial para evitar errores,
garantizar coherencia y asegurar que los datos sean confiables.
Este documento cubre seis problemas donde se aplican métodos de string,
validaciones, normalización, patrones básicos y formateo de salida.  
Cada problema incluye entradas, salidas esperadas, reglas de validación
y tres casos de prueba (normal, borde y error).
"""

# Buenas prácticas al manejar strings en Python:
"""
Los strings son inmutables: cualquier modificación crea una cadena nueva.
Es recomendable normalizar texto con strip() y lower() antes de compararlo.
Evitar “números mágicos” en índices y documentar para qué sirve cada slice.
Preferir métodos incorporados de Python antes que reescribir lógica.
Diseñar validaciones claras: primero verificar que no esté vacío, luego formato.
Mantener nombres de variables en lower_snake_case y consistencia en el código.
"""

# PROBLEMA 1 Full name formatter (name + initials)
# Descripción:
"""
Este programa recibe el nombre completo de una persona en una sola cadena.
Se deben eliminar espacios innecesarios, estandarizar mayúsculas y minúsculas
y generar las iniciales correspondientes en formato X.X.X.
"""

# Entradas:
# - full_name (string).

# Salidas:
# - "Formatted name: <...>"
# - "Initials: <...>"

# Validaciones:
# - full_name no debe quedar vacío tras usar strip().
# - Debe contener al menos dos palabras.
# - No se aceptan cadenas formadas únicamente por espacios.

# Código:
full_name = input("Enter your full name: ")
full_name = full_name.strip()

if len(full_name) == 0:
    print("Error: empty name.")
else:
    parts = full_name.split()

    if len(parts) < 2:
        print("Error: enter at least two words.")
    else:
        title_name = ""
        for p in parts:
            title_name = title_name + p.title() + " "

        title_name = title_name.strip()

        initials = ""
        for p in parts:
            initials = initials + p[0].upper() + "."

        print("Formatted name:", title_name)
        print("Initials:", initials)


# Casos de prueba:
# 1) Normal: 
"""Enter your full name: gera salazar Perez
Formatted name: Gera Salazar Perez
Initials: G.S.P. """
# 2) Borde: 
"""Enter your full name: gera salazar 
Formatted name: Gera Salazar 
Initials: G.S. """
# 3) Error: 
"""Enter your full name:
Error: empty name.
"""

# PROBLEMA 2 Simple email validator (structure + domain)
# Descripción:
"""
Valida formato básico de correo: exactamente un '@', al menos un '.' después del '@',
sin espacios. Si es válido, muestra el dominio (parte después de '@').
"""
# Entradas:
#   - email_text (string)

# Salidas:
#   - "Valid email: true" o "Valid email: false"
#   - Si válido: "Domain: <domain_part>"

# Validaciones:
#   - email_text no vacío tras strip()
#   - Contar '@' y verificar ausencia de espacios


# Código:
email_text = input("Enter an email: ")
email_text = email_text.strip()

if len(email_text) == 0:
    print("Valid email: false")
else:
    if " " in email_text:
        print("Valid email: false")
    else:
        at_count = email_text.count("@")

        if at_count != 1:
            print("Valid email: false")
        else:
            at_pos = email_text.find("@")
            domain_part = email_text[at_pos+1:]

            if "." not in domain_part:
                print("Valid email: false")
            else:
                print("Valid email:", "true")
                print("Domain:", domain_part)

# Casos de prueba:
#   1) Normal: 
""" Enter an email: gerardo@gmail.com
Valid email: true
Domain: gmail.com """
#   2) Border: 
"""Enter an email: gerardo@gmail..com
Valid email: true
Domain: gmail..com"""
#   3) Error: 
"""Enter an email: gera@@gmail.com
Valid email: false"""



# PROBLEMA 3: Palindrome checker (ignoring spaces and case)
# Descripcion:
# Determina si una frase es palíndromo ignorando espacios y mayúsculas/minúsculas.
# Engradas:
#   - phrase (string)
# Salidas:
#   - "Is palindrome: true" o "Is palindrome: false"
#   - (Opcional) "Normalized: <normalized_phrase>"
# Validaciones:
#   - phrase no vacía tras strip()
#   - Longitud mínima razonable (>=3) después de limpiar espacios

# Código:
phrase = input("Enter a phrase: ")
phrase = phrase.strip()

if len(phrase) == 0:
    print("Is palindrome: false")
else:
    clean_phrase = phrase.lower()
    clean_phrase = clean_phrase.replace(" ", "")

    if len(clean_phrase) < 4:
        print("Is palindrome: false")
    else:
        reverse_phrase = clean_phrase[::-1]

        if clean_phrase == reverse_phrase:
            print("Is palindrome: true")
        else:
            print("Is palindrome: false")

# Casos de prueba:
#   1) Normal: 
""" Enter a phrase: amada la dama
Is palindrome: true """
#   2) Border: 
"""Enter a phrase: jaaj
Is palindrome: true"""
#   3) Error: 
"""Enter a phrase: ouyessirrr
Is palindrome: false"""

# PROBLEMA 4: Sentence word stats (lengths and first/last word)
# Descripcion:
""" 
Dada una oración, normaliza espacios, separa palabras y muestra conteo,
primera, última, palabra más corta y más larga.
"""
# Entrada:
#   - sentence (string)
# Salidas:
#   - "Word count: <n>"
#   - "First word: <...>"
#   - "Last word: <...>"
#   - "Shortest word: <...>"
#   - "Longest word: <...>"
# Validaciones:
#   - Oración no vacía tras strip()
#   - Debe contener al menos una palabra válida

# Código: 
sentence = input("Enter a sentence: ")
sentence = sentence.strip()

if len(sentence) == 0:
    print("Error: empty sentence.")
else:
    words = sentence.split()

    if len(words) == 0:
        print("Error: no valid words.")
    else:
        word_count = len(words)
        first_word = words[0]
        last_word = words[-1]

        shortest_word = words[0]
        longest_word = words[0]

        for word in words:
            if len(word) < len(shortest_word):
                shortest_word = word
            if len(word) > len(longest_word):
                longest_word = word

        print("Word count:", word_count)
        print("First word:", first_word)
        print("Last word:", last_word)
        print("Shortest word:", shortest_word)
        print("Longest word:", longest_word)

# Casos de prueba:
#   1) Normal: 
"""Enter a sentence: hola gentee
Word count: 2
First word: hola
Last word: gentee
Shortest word: hola
Longest word: gentee"""
#   2) Border: 
"""Enter a sentence: wa
Word count: 1
First word: wa
Last word: wa
Shortest word: wa
Longest word: wa"""
#   3) Error: 
"""Enter a sentence:
Error: empty sentence."""

# PROBLEMA 5: Password strength classifier
# Descripción:
# Clasifica contraseña en weak, medium o strong según reglas simples.
# Entrada:
#   - password_input (string)
# Salida:
#   - "Password strength: weak" / "Password strength: medium" / "Password strength: strong"
# Validaciones:
#   - No aceptar contraseña vacía
# Reglas documentadas:
#   - Strong: length >= 8, has_upper, has_lower, has_digit, has_symbol
#   - Medium: length >= 8 and (two of the categories among upper/lower/digit)
#   - Weak: otherwise

# Código: 
password_input = input("Enter a password: ")

if len(password_input) == 0:
    print("Password without value.")
else:
    has_upper = False
    has_lower = False
    has_digit = False
    has_symbol = False

    for character in password_input:
        if character.isupper():
            has_upper = True
        if character.islower():
            has_lower = True
        if character.isdigit():
            has_digit = True
        if not character.isalnum():
            has_symbol = True

    if len(password_input) < 8:
        print("Password strength: weak")
    else:
        if has_upper and has_lower and has_digit and has_symbol:
            print("Password strength:", "strong")
        else:
            print("Password strength:", "medium")


# Casos de prueba:
#   1) Normal: 
"""Enter a password: contraMegaFuerte:v!@
Password strength: strong"""
#   2) Border: 
"""Enter a password: waxdcfvgbtfvbhbyvgbhjh
Password strength: weak"""
#   3) Error: 
"""Enter a password:
Password without value."""


# PROBLEMA 6: Product label formatter (fixed-width text)
# Descripcion:
"""
Genera etiqueta en una sola línea: "Product: <NAME> | Price: $<PRICE>"
La cadena completa debe tener exactamente 30 caracteres; rellenar con espacios
o recortar según se requiera.
"""
# Entradas:
# - product_name (string)
# - price_value (string o número convertible)
# Salida:
# - "Label: '<exactly 30 characters>'"
# Validaciones:
# - product_name no vacío tras strip()
# - price_value convertible a número positivo


# Código: 
product_name = input("Enter product name: ")
product_name = product_name.strip()

price_value = input("Enter price: ")

if len(product_name) == 0:
    print("Error: empty product name.")
else:
    try:
        price_num = float(price_value)
        if price_num <= 0:
            print("Error: price must be positive.")
        else:
            label = "Product: " + product_name + " Price: " + str(price_num)

            if len(label) > 30:
                label = label[:30]

            while len(label) < 30:
                label = label + " "

            print("Label:", "'" + label + "'")
    except:
        print("Error: invalid price.")

# Casoas de prueba:
#   1) Normal: 
"""Enter product name: bread
Enter price: 15
Label: 'Product: bread Price: 15.0      ' """
#   2) Border: 
"""Enter product name: longnameofanarticleofsorianaxdxd
Enter price: 20
Label: 'Product: longnameofanart Price: 20.0' """
#   3) Error: 
"""Enter product name: cereal
Enter price: 0
Error: price must be positive."""

# ======================================================================
# CONCLUSIONES 
# ======================================================================
"""
El manejo de cadenas de texto es esencial en programas que reciben y muestran
información, ya que nombres, correos, contraseñas y etiquetas requieren procesos
de normalización y validación. Métodos como lower(), strip(), split() y join()
permiten realizar transformaciones comunes de manera sencilla y ayudan a que el
código sea más legible y robusto. Normalizar antes de comparar evita errores
causados por espacios adicionales o diferencias en mayúsculas y minúsculas.
Además, diseñar validaciones en un orden lógico —primero verificar que no esté
vacío, después revisar el formato y finalmente el contenido— reduce la posibilidad
de recibir datos incorrectos o basura. También es importante recordar que los
strings en Python son inmutables, por lo que cada operación genera una nueva
cadena, haciendo necesario el uso adecuado de slices y métodos para extraer o
modificar información dentro del texto.
"""

# ======================================================================
# REFERENCIAS 
# ======================================================================
# https://apuntes.de/python/manipulacion-de-strings-en-python-conceptos-basicos/#gsc.tab=0
# https://www.freecodecamp.org/espanol/news/metodos-de-cadenas-split-y-join-en-python/  
# https://ellibrodepython.com/booleano-python 
# https://es.stackoverflow.com/questions/139346/practica-palindromo 
# https://www.guru99.com/es/palindrome-program-in-python.html 
# https://www.delftstack.com/es/howto/python/python-pad-string-with-spaces/ 
# https://programminghistorian.org/es/lecciones/manipular-cadenas-de-caracteres-en-python 
# https://platzi.com/blog/metodos-de-strings-en-python-domina-el-poder-de-las-cadenas-de-texto/ 
# https://www.ionos.mx/digitalguide/paginas-web/desarrollo-web/python-len/ 

# ======================================================================
# REPOSITORIO DE GITHUB
# ======================================================================



