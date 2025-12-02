# Simple dictionary
alien_0 = {"color" : "green", "points" : 5}
print(alien_0["color"])

# The simpliest dictionary
alien_1= {"color": "yelow"}

#Accessing values in a dictionary
print(alien_1["color"])
print(alien_0["points"])

# Emoty dictionary
alien_2 = {}

#Modifying key-value pairs to a dictionary
alien_2= {"color": "yelow"}
alien_2["color"] = "blue"

#Adding new key-value pairs
alien_2["x_position"] = 0
alien_2["y_position"] = 25
print( alien_2)

# Dictionary to store similar objects
favorite_lenguages = { 
    "jen": "python",
    "sarah": "c",
    "edward": "ruby",
    "phil": "python",

}
print (f"Sarah favorite lenguaje is {favorite_lenguages['sarah']}")

# Looping through all key-value pairs
for key, value in favorite_lenguages.items():
    print(f"{key.title()} 's favorite lenguaje is {value}.")


covenant_grunts = {
    "color": "oranje",
    "height": "small",
    "weapon": "plasma-gun", 
    "hit-points": 4,
    "health": 3, 
    "points": 1, 
 }

covenant_elites = {
    "color": "blue",
    "height": "big",
    "weapon": "plasma-sword", 
    "hit-points": 6,
    "health": 6, 
    "points": 3,
 }

covenant_jackal = {
    "color": "green",
    "height": "medium",
    "weapon": "plasma-gun", 
    "hit-points": 7,
    "health": 3, 
    "points": 2,
 }

for key, value in covenant_grunts.items():
    print(key, value)

# Estudiar - Listas de diccionarios 
# Estudiar - Listas en diccionarios 
# Estudiar - Diccionario de diccionarios 

covenants=[
covenant_grunts, 
covenant_elites, 
covenant_jackal
]

for aux in covenants:
    print("\n Covenant:", aux) 
    for key, value in aux.items():
        print(key, value)

# Listas en diccionarios
students = {
    "pablo": ["cars", "programar en python", "hacer tarea"],
    "gerardo-pelom": ["motos", "programar en arduino", "no le gusta chambear"],
    "gerardo-ame": ["America"],

}
print(students["gerardo-pelom"])

# Diccionario de diccionarios
sensors = {
    "temperature": {
        "id": "temp_1",
        "locatios": "classroom_a1",
        "value": 20,
    },

    "humidity": {
        "id": "hum_1",
        "location": "classroom_a2",
        "value": 60,
    },
}


# Imprimir el valor de la temperatura
print("Temperature")
print(sensors["temperature"]["value"])
print("ID")
print(sensors["temperature"]["id"])

# Investigar el metodo get
"""
como método de los diccionarios para obtener un valor de forma segura y como un 
patrón de diseño en POO (programación orientada a objetos) para acceder a 
atributos de una clase.
"""

