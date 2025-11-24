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

