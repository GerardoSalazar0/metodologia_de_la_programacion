# LAS TUPLAS SON INMUTABLES

"""
    Tuplas: Las tuplas son listas de elementos que no cambian de tamaño.    
    Las tuplas son listas inmutables.

    Se utilizan los () para definir una tupla.
    O la palabras reservada tuple ().

    Si tenemos un rectangulo que siempre va a tener cierto tamaño, podemos asegurar
    que su tamaño no va a cambiar si colocamos sus valores en una tupla.

"""

# Ejemplo  de tuplas
Dimensions = (200, 50)
print(Dimensions)
print(Dimensions[0])
print(Dimensions[1])

# Dimensions[0]= 300 NO SE PUEDE
for dimension in Dimensions:
    print(dimension)


"""
    No podemos modificar una tupla directamente, lo que si podemos hacer es cambiar la asignacion
    a una variable que almacena una tupla.
"""
Dimensions=(200, 50)
print(Dimensions)
Dimensions=(400, 20, 40)
print(Dimensions)
