# Fibonacci Series with Python
# Materia: Metodología de la Programación 
# Profesor: Charly Mercury 
# Estudiante: Gerardo Salazar de la Fuente (2530032) 1-1 IM  

# Resumen Ejecutivo:
"""
La serie de Fibonacci es una secuencia numérica donde cada término se obtiene sumando los 
dos anteriores, comenzando con 0 y 1. Calcular la serie hasta un número de términos n 
significa generar exactamente los primeros n valores siguiendo esta regla. Este programa 
lee n desde la entrada, valida que sea un entero positivo y luego usa un bucle para 
construir la serie término por término. Finalmente, muestra la secuencia completa 
en pantalla. También maneja entradas inválidas para evitar errores durante la ejecución.
"""


# PROBLEMA: Fibonacci series generator  
# Descripción:
"""
This program reads an integer n and prints the first n terms of the Fibonacci
series, starting with 0 and 1. It first checks that the input is valid and that
n is at least 1. Then it uses a loop to generate each term by adding the two
previous numbers. Finally, it prints the full sequence in one line.
"""

# Inputs:
"""
- n (int; number of terms to generate)  
"""

# Outputs:
"""
- "Fibonacci series:" followed by the n terms separated by spaces or commas  
"""

# Validations:
"""
- n must be an integer  
- n must be >= 1  
- n must be <= 25  
"""

# Código:
try:
    n=int(input("Enter the value of 'n': "))
    if n>1 and n<25:
        a=0
        b=1
        sum=0
        count=1
        print("Fibonacci Sequence: ")
        while(count<=n):    
            print(sum)
            count+=1
            a=b
            b=sum
            sum=a+b	
    else:
        print("Enter a valid number")
except:
    print("Put a valid number")

# Test cases:
# 1) Normal:
"""
Enter the value of 'n': 7
Fibonacci Sequence:
0
1
1
2
3
5
8
"""

# 2) Border:
"""
Enter the value of 'n': 24
Fibonacci Sequence:
0
1
1
2
3
5
8
13
21
34
55
89
144
233
377
610
987
1597
2584
4181
6765
10946
17711
28657
"""

# 3) Error:
"""
Enter the value of 'n': a
Put a valid number
"""

# ======================================================================
# CONCLUSIONES 
# ======================================================================
"""
El uso de un ciclo facilitó generar la serie de Fibonacci paso a paso, calculando
cada término a partir de los dos anteriores. También fue importante manejar
correctamente los casos especiales n = 1 y n = 2 para asegurar que la salida
fuera precisa desde el inicio. Esta misma lógica puede reutilizarse en otros
programas que trabajen con secuencias o cálculos iterativos.
"""



# ======================================================================
# REFERENCIAS 
# ======================================================================

# https://es.stackoverflow.com/questions/213161/es-posible-hacer-m%C3%A1s-simple-esta-secuencia-de-fibonacci-en-python-usando-loop
# https://conpilar.es/3-formas-de-generar-la-secuencia-de-fibonacci-en-python/ 
# https://www.datacamp.com/es/tutorial/fibonacci-sequence-python 
# https://www.youtube.com/watch?v=fdvVx06IeeY 
# https://altocodigo.blogspot.com/2018/07/sucesion-de-fibonacci-programada-en.html 
# https://www.mycompiler.io/view/3833QlX0QBB 



# ======================================================================
# REPOSITORIO DE GITHUB
# ======================================================================

# 