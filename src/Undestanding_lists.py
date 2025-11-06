#LISTS

"""
    Las listas nos permiten almacenar informacion en un lugar, 
    'la cantidad que tengas': ya sean pocos o millones de elementos.

    Se recomienda nombrar una variable del tipo lista en PLURAL.

    En Python los corchetes [] indican o definen una lista, los elementos en una lista
    se separan por comas.

    Ejemplo:
"""

bicycles = ['trek', 'cannondale', 'redline', 'giant']
print(bicycles, type(bicycles))
print(bicycles[0]. title(), type(bicycles[0]))  

# Acceder a elementos de una lista
print(bicycles[0]. title(), type(bicycles[0]))  
print(bicycles[3]. title(), type(bicycles[3]))  

# Acceder al ultimo elemento de una lista
print(bicycles[-1]. title(), type(bicycles[-1])) # ultimo
print(bicycles[-2]. title(), type(bicycles[-2])) # penultimo
print(bicycles[-4]. title(), type(bicycles[-4])) # el antes del antepenultimo


message= "My first bicible was a " + bicycles[0] .title() + "."
print(message)



#Agregar elementos a una lista
motocycles = ["honda", "yambda", "susuki"]
print("Lista original:", motocycles)

motocycles.append("ducati")
print("lista append:", motocycles)

"""
    Append nos deja agregar elementos al final de una lista.
"""

# Crear una lista vacia y luego agregar elementos
cars= []
print("Lista de carros: ", cars)
cars.append("bwm")
print("Lista de carros: ", cars)
cars.append("audi")
print("Lista de carros: ", cars)
cars.append("toyota")
print("Lista de carros: ", cars)

#Agregar elementos en una posicion especifica
motocycles= ["honda", "yamaha", "susuki"]
print("Lista de motos", motocycles)
motocycles.insert(0, "ducati")
print("Lista de motos nueva:", motocycles)

#Eliminar elementos de una lista usando del (no es un metodo)
print("lista original de motos", motocycles)

del motocycles [0]
print("lista de motos luego de del", motocycles)

# Eliminar un elemento usando el metodo pop 
print("lista de motos originales: ", motocycles)
popped_motocycle = motocycles.pop()
print("lista de motos con pop: ", motocycles)
print("moto con pop: ", popped_motocycle)

print("lista de motos originales: ", motocycles)
second_motocycles= motocycles.pop(1)
print("lista de motos despues de pop (): ", motocycles)
print("moto eliminada: ", second_motocycles)

# Eliminar elementos de una lista por valor
motocycles= ["mortalika", "ducati", "hd"]
motocycles.pop()
print(motocycles)
motocycles.pop(0)
print(motocycles)
motocycles.remove("ducati")
print(motocycles) 

#ORDENAR  LISTAS/METODOS DE LISTAS
# .insert2, .append1, .pop0,1, .remove1, .sort0,1, .reverse0
#Permamente metodo .sort

cars= ["bmw", "toyota", "kia", "ford"]
cars.sort() # ordena alfabeticamente
print(cars) # bmw, ford, kia, toyota
# con .sort(reverse=True) ordena en orden inverso
cars.sort(reverse=True)
print(cars) # toyota, kia, ford, bmw

# BUILT/IN
#str()
#type()
#print()
#len()

print(len(cars))  #cantidad de elementos en la lista

favorite_fruits = ["mango", "manzana", "uvas", "durazno"]
print(favorite_fruits)
favorite_fruits.reverse()
print(favorite_fruits)

sorted_fruits= sorted(favorite_fruits) # ordena temporalmente
print(sorted_fruits) # lista ordenada temporalmente
print(favorite_fruits) # la lista original no cambia