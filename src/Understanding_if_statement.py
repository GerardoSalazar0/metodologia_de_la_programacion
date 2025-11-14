cars = ["audi", "bmw", "volvo", "tesla", "toyota"]
for car in cars:
    if car == "bmw" or car == "tesla": 
        print(car.upper())
    else:
        print(car.lower())

#El condicional es el corazon del if ==
# Ejemplos de condicionales

#Condicional true
car_1= "bmw"
print(car_1== "bmw")


#Condicional false
car_2= "Audi"
print(car_2== "audi")

car_3 = "Audi"
print(car_3.lower()=="audi")


#Condicional != para determinar desigualdad
requested_topping = "mushrooms"
if requested_topping != "anchoves":
    print("Hold the anchovies")


# Comparaciones numericas 
age = 18
print(age==18) # True

answer = 17
if answer != 42: # True
    print("Esa no es la respuesta intenta de nuevo")


age=19
print(age<21) # True
print(age<=21) # True
print(age>21) # False
print(age>=21) # False


# Condicionales multiples 
age_0 = 22
age_1 = 18

print(age_0>=21) # True
print("and")
# Operacion Logica and
print(age_0>=21 and age_1>21) # False
print(age_0>=21 and age_1>=18) # True


age_0 = 22
age_1 = 18
print("or")
# Operacion Logica or
print(age_0>=22 or age_1>21) # True
print(age_0>=23 or age_1>=21) # False

print("elementos en una lista")
# Preguntarme si un valor esta en una lista 
cars = ["micro", "vocho", "tsuru", "tsubaro"]
print("vocho" in cars) # True
print("chevy" in cars) # False


print("elementos q no estan en una lista")
# Preguntar si un valor no esta en la lista 
alumnos = ["victor", "ana", "maiki", "gera"]
user = "josue"

print(user not in alumnos) #True
print("maiki" not in alumnos) # False

# Datos booleanos 
game_active = True
can_edit = False
