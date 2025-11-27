# Manejo de bucles en Python
# Materia: Metodología de la Programación 
# Profesor: Charly Mercury 
# Estudiante: Gerardo Salazar de la Fuente (2530032) 1-1 IM  

# Resumen Ejecutivo:
"""
Este documento explica el uso de los bucles for y while en Python, mostrando 
sus diferencias y aplicaciones más comunes. El bucle for se utiliza cuando se 
conoce de antemano la cantidad de iteraciones, como al recorrer rangos o listas.
El bucle while es más adecuado cuando la repetición depende de una condición, 
como leer datos hasta un sentinela o manejar menús interactivos. Los contadores y acumuladores
permiten llevar control sobre cantidades y sumas dentro de los bucles, siendo fundamentales 
para cálculos repetitivos. Es importante definir correctamente la condición de salida para 
evitar ciclos infinitos, especialmente en bucles while. Este documento presenta la 
descripción completa de cada problema, incluyendo entradas, salidas, validaciones y casos de prueba.
También se muestran ejemplos concretos del uso de for y while en situaciones diversas 
como sumas, tablas, promedios, intentos de contraseña, menús y patrones.
Con ello, se logra comprender cómo elegir el tipo de bucle adecuado 
y cómo estructurar programas claros, seguros y funcionales.
"""

# Buenas practicas:
"""
En la construcción de algoritmos en Python, el uso adecuado de los bucles es fundamental 
para automatizar tareas repetitivas y mejorar la eficiencia del código. Los ciclos `for` 
resultan ideales cuando se requiere recorrer secuencias, iterar sobre listas o procesar 
elementos de manera ordenada, garantizando un flujo de ejecución claro y predecible. 
Por su parte, los ciclos `while` permiten ejecutar acciones basadas en condiciones dinámicas, 
lo que los hace apropiados en situaciones donde el número de repeticiones no es conocido 
de antemano.

Es importante aplicar buenas prácticas al trabajar con bucles, como asegurar que las 
condiciones de salida sean adecuadas para evitar ciclos infinitos y validar correctamente 
los datos que intervienen en la iteración. También conviene mantener un manejo cuidadoso 
de los contadores, índices y variables de control, así como emplear mensajes claros cuando 
se interactúa con el usuario dentro del ciclo.

El uso correcto de técnicas como romper la ejecución con `break`, omitir pasos con `continue` 
o aprovechar estructuras como `range()` permite crear bucles más seguros y expresivos. 
En conjunto, estas prácticas fomentan programas más organizados, eficientes y fáciles de 
depurar, asegurando que la lógica repetitiva se ejecute de manera precisa y confiable.

"""


# PROBLEMA 1: Sum of range with for
# Descripción:
"""Se calcula la suma de todos los enteros desde 1 hasta n (incluyendo n). Y además, calcular 
la suma solo de los números pares en ese mismo rango usando un bucle for."""

#Inputs:
"""- n (int; límite superior del rango)."""

#Outputs:
"""- "Sum 1..n:" <total_sum>
- "Even sum 1..n:" <even_sum>"""

#Validations:
"""- Verificar que n pueda convertirse a int.
- n >= 1; si no se cumple, mostrar "Error: invalid input"."""

#Código: 
n_input = input("Enter n: ")

try:
    n = int(n_input)
    if n < 1:
        print("Error: invalid input")
    else:
        total_sum = 0
        even_sum = 0

        for i in range(1, n + 1):
            total_sum = total_sum + i

            if i % 2 == 0:
                even_sum = even_sum + i

        print("Sum 1..n:", total_sum)
        print("Even sum 1..n:", even_sum)
except ValueError:
    print("Error: invalid input")

# Test cases:
# 1) Normal:
"""Enter n: 4
Sum 1..n: 10
Even sum 1..n: 6"""

# 2) Border:
"""Enter n: 1
Sum 1..n: 1
Even sum 1..n: 0"""

# 3) Error:
"""Enter n: a
Error: invalid input"""


# PROBLEMA 2: Multiplication table with for
# Descripción:
"""
Genera y muestra la tabla de multiplicar de un número base, desde 1 hasta 
un límite m. Por ejemplo, si base = 5 y m = 4, muestra:
5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
5 x 4 = 20
"""

#Inputs:
"""
base (int): número del cual se generará la tabla.
m (int): límite superior de multiplicación (cantidad de filas de la tabla).
"""

#Outputs:
"""
Una línea por cada resultado:
"base x 1 = resultado"
"base x 2 = resultado"
...
"base x m = resultado"
"""

#Validations:
"""
Verificar que base es convertible a entero.
Verificar que m es convertible a entero.
Validar:
m >= 1
Si no se cumple → mostrar "Error: invalid input" y no generar la tabla.
"""

#Código: 
base_input = input("Enter base: ")
m_input = input("Enter limit m: ")

try:
    base = int(base_input)
    m = int(m_input)
    if m < 1:
        print("Error: invalid input")
  
    for i in range(1, m + 1):
        result = base * i
        print(f"{base} x {i} = {result}")
except:
    print("Error: invalid input")


# Test cases:
# 1) Normal:
"""Enter base: 2
Enter limit m: 3
2 x 1 = 2
2 x 2 = 4
2 x 3 = 6"""

# 2) Border:
"""Enter base: 2
Enter limit m: 2
2 x 1 = 2
2 x 2 = 4"""

# 3) Error:
"""Enter base: s
Enter limit m: a
Error: invalid input"""



# PROBLEMA 3: Average of numbers with while and sentinel
# Descripción:
"""Lee números uno por uno hasta que el usuario ingrese un valor sentinela (por ejemplo, -1). 
Calcula el promedio de los números válidos ingresados y la cantidad de números leídos. 
Si el usuario sólo ingresa el sentinela sin números válidos, muestra un mensaje de error.
"""

#Inputs:
""" - number (float; se lee repetidamente).
- sentinel_value (fijo en el código, por ejemplo: -1).
"""

#Outputs:
"""- "Count:" <count>
- "Average:" <average_value>
- Si no se ingresan datos válidos:
  - "Error: no data"
"""

#Validations:
"""- Cada lectura debe intentar convertirse a float.
- Ignorar el sentinela en los cálculos.
"""


#Código: 
SENTINEL = -7
count = 0
total = 0.0

while True:
    value_input = input("Enter number (-7 to stop): ")

    try:
        number = float(value_input)
    except:
        print("Error: invalid input")
        continue 

    if number == SENTINEL:
        break  
    total += number
    count += 1

if count == 0:
    print("Error: no data")
else:
    average = total / count
    print("Count:", count)
    print("Average:", average)


# Test cases:
# 1) Normal:
"""Enter number (-7 to stop): 2.32
Enter number (-7 to stop): 32.
Enter number (-7 to stop): 23.2
Enter number (-7 to stop): 2.2
Enter number (-7 to stop): 2.2
Enter number (-7 to stop): -7
Count: 5
Average: 12.384"""

# 2) Border:
"""Enter number (-7 to stop): -7
Error: no data"""

# 3) Error:
""" Enter number (-7 to stop): a
Error: invalid input
"""


# PROBLEMA 4: Password attempts with while
# Descripción:
"""Se implementara un sistema sencillo de intento de contraseña. 
El codigo tendra una contraseña correcta con un máximo de MAX_ATTEMPTS intentos para introducirla. 
Si acierta dentro del límite, mostrar un mensaje de éxito. 
Si agota los intentos, mostrar un mensaje de bloqueo.
"""

#Inputs:
""" - user_password (string; se lee en cada intento).
"""

#Outputs:
""" "Login success" si la contraseña es correcta.
"Account locked" si se acaban los intentos sin éxito.
"""

#Validations:
"""- MAX_ATTEMPTS > 0 .
- Contar correctamente los intentos.
"""


#Código: 
CORRECT_PASSWORD = "Thepapus"
MAX_ATTEMPTS = 4

attempts = 0
success = False

while attempts < MAX_ATTEMPTS:
    password = input("Enter password: ")

    if password == CORRECT_PASSWORD:
        print("Login success")
        success = True
        break
    else:
        attempts += 1

if not success:
    print("Account locked")


# Test cases:
# 1) Normal:
"""Enter password: Thepapus
Login success"""

# 2) Border:
"""Enter password: 1
Enter password: 2
Enter password: 3
Enter password: Thepapus
Login success"""

# 3) Error:
"""Enter password: a
Enter password: a
Enter password: a
Enter password: a
Account locked"""



# PROBLEMA 5: Simple menu with while
# Descripción:
"""
Implementa un menú de texto que se repite hasta que el usuario seleccione la opción de salir. 
Ejemplo de menú:
1) Show greeting
2) Show current counter value
3) Increment counter
0) Exit
El programa debe ejecutar la acción correspondiente a cada opción y volver a mostrar el menú 
hasta que se elija 0.
"""

#Inputs:
""" - option (string o int; elección del usuario).
"""

#Outputs:
"""
- Mensajes según la opción:
- "Hello!" para saludo.
- "Counter:" <counter_value> para mostrar contador.
- "Counter incremented" al incrementar.
- "Bye!" al salir.
- Para opciones inválidas:
- "Error: invalid option"
"""

#Validations:
"""
- Normalizar option.
- Asegurar que sólo 0,1,2,3 sean aceptadas como válidas.
"""


#Código: 
counter = 0

while True:
    print("1) Show greeting")
    print("2) Show current counter value")
    print("3) Increment counter")
    print("0) Exit")

    option_input = input("Choose an option: ")

    try:
        option = int(option_input)
    except:
        print("Error: invalid option")
        continue

    if option == 1:
        print("Hi!")
    elif option == 2:
        print("Counter:", counter)
    elif option == 3:
        counter += 1
        print("Counter incremented by 1") 
    elif option == 0:
        print("Bye Bye")
        break
    else:
        print("Error: invalid option")



# Test cases:
# 1) Normal:
"""
1) Show greeting
2) Show current counter value
3) Increment counter
0) Exit
Choose an option: 1
Hi!
1) Show greeting
2) Show current counter value
3) Increment counter
0) Exit
"""

# 2) Border:
"""
1) Show greeting
2) Show current counter value
3) Increment counter
0) Exit
Choose an option: 0
Bye Bye
"""

# 3) Error:
"""
1) Show greeting
2) Show current counter value
3) Increment counter
0) Exit
Choose an option: 4
Error: invalid option
"""


# PROBLEMA 6: Pattern printing with nested loops
# Descripción:
"""
Usa bucles for anidados para imprimir un patrón de asteriscos en forma de triángulo rectángulo. 
Por ejemplo, para n = 4:
*
**
***
****

"""

#Inputs:
""" - n (int; número de filas del patrón).
"""

#Outputs:
""" - Patrón línea por línea
"""

#Validations:
""" 
- n convertible a int.
- n >= 1; si no, "Error: invalid input".
"""


#Código: 
n_input = input("Enter n: ")

try:
    n = int(n_input)
except:
    print("Error: invalid input")
    exit()

if n < 1:
    print("Error: invalid input")
    exit()

for i in range(1, n + 1):
    line = ""
    for j in range(i):
        line += "*"
    print(line)


# Test cases:
# 1) Normal:
"""Enter n: 4
*
**
***
****
"""

# 2) Border:
"""Enter n: 1
*
"""

# 3) Error:
"""
Enter n: a
Error: invalid input
"""



# ======================================================================
# CONCLUSIONES 
# ======================================================================

"""
Al hacer estos ejercicios entendí mejor cuándo conviene usar for y cuándo while.
El for es perfecto cuando ya sabemos cuántas veces se repetirá algo, como en rangos
o patrones. En cambio, el while sirve más para situaciones que dependen del usuario,
como menús o intentos de contraseña, aunque hay que tener cuidado porque si no se
controla bien la condición puede volverse un ciclo infinito.

También vi lo útiles que son los contadores y acumuladores para llevar control de
sumas, promedios o simplemente para ir contando acciones. Los menús y el login fueron
buenos ejemplos del uso real de while en programas interactivos. Finalmente, los bucles
anidados ayudaron a entender cómo se pueden generar patrones más complejos combinando
repeticiones dentro de otras repeticiones.
"""



# ======================================================================
# REFERENCIAS 
# ======================================================================

# https://www.revsys.com/tidbits/sentinel-values-python/ 
# https://www.w3schools.com/python/ref_keyword_break.asp 
# https://www.programiz.com/python-programming/break-continue 
# https://www.codingwithsid.in/2020/10/menu-driven-program-in-python.html 
# https://discuss.python.org/t/sum-of-even-numbers-help/56693 
# https://stackoverflow.com/questions/41446833/what-is-the-difference-between-i-i-1-and-i-1-in-a-for-loop 
# https://stackoverflow.com/questions/72078359/sum-of-even-numbers-in-python 
# https://www.programiz.com/python-programming/examples/multiplication-table 
# https://www.freecodecamp.org/news/python-for-loop-for-i-in-range-example/ 
# https://stackoverflow.com/questions/77197170/to-print-a-pattern-in-python-using-nested-for-loops 
# https://medium.com/@dnaresh2323/nested-loops-pattern-printing-in-python-8d3503340f1d 
# https://tutorial.recursospython.com/bucles/
# https://www.datacamp.com/es/tutorial/loops-python-tutorial 
# https://www.youtube.com/watch?v=GQGhU1526Oo 




# ======================================================================
# REPOSITORIO DE GITHUB
# ======================================================================

#