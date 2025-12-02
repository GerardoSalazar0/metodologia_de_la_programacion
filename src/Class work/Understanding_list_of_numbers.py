"""
    Las listas tambien pueden almacenar numeros y de hecho son ideales para eso.
    Python ofrece muchas herramientas que ayudan a trabajar de manera eficiente
    con las listas de números.
    
    """

# Metodo range()
# Nos ayuda a generar facilmente series de numeros
# Ejemplo:
print("Imprime los primeros 10 numeros")
for number in range(10): # ES UN GENERADOR DE NUMEROS
    print(number)

first_10_numbers= list(range(10))
print(first_10_numbers)

print("Imprime los numeros del 0 al 4")
for number in range(0,5): # Desde el 0 hasta el 4 
    print(number)

numbers_0to4= list(range(0,5))
print(numbers_0to4)

print("Imprime los numeros pares entre el 0 y el 10")
for number in range(0,11,2): # Los numeros pares entre el 0 y el 10
    print(number)

numbers_par= list(range(0,11,2))
print(numbers_par)

print("Imprime los numeros impares entre el 0 y el 10")
for number in range(1,11,2): # Los numeros impares entre el 0 y el 10
    print(number)

numbers_impar= list(range(1,11,2))
print(numbers_par)

print("Imprime los numeros impares entre el 0 y el 10")
for number in range(0,51,5): # La tabla del 5 
    print(number)

tabla_del_5= list(range(0,51, 5))
print(tabla_del_5)


print("Generar una lista de cuadrados de los primeros 10 numeros")
squares= []
for number in range (1,11):
    square= number**2
    squares.append(square)
print(squares)

# Otros metodos built-in
digits= [1,2,3,4,5,6,7,8,9,0]
print(min(digits)) #Valor Minimo
print(max(digits)) #Valor Maximo
print(sum(digits)) #Suma de todo. Salida 45

