"""
    Un list comprehension combina el for loop y la creacion de nuevos elementos
    en una sola linea y automaticamente agrega cada nuevo elemento a la lista, sin
    tener que utilizar el metodo append

"""

#Generar una lista de los cuadradosde los primeros 10 numeros
squares= [value**2 for value in range(1,11)]
print(squares)

#Genera una lista con los numeros pares
evens= [value for value in range(101) if value%2==0] 
print(evens)

#Genera una lista con los numeros impares
odds= [value for value in range(101) if value%2==1] 
print(odds)
