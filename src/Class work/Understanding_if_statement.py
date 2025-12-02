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


# If statement
"""
    Programa para pedir la edad al usuario y que diga si el usuario es menor de edad
    o mayor de edad.

"""

#Try: Except
try:
    input_msj = input()
    age=int(input_msj)
# If-elif-else
    if age >= 18 and age <= 100: 
        print("eres legalito")
    elif age <18 and age >=0: 
        print("eres ilegalito")
    
    elif age >= 101:
        print("un siglo vivo pa")
    elif age < 0:
        print("que pedo, aun no naces")

except:
    print("Hola papoi, no se permiten letras")


"""
    Ejercicio:
    
        Elabore un progrrama que contemple lo siguiente:
        - Si la edad es menor a 4 entrada gratuita
        - Si es entee 4 y 18, costo de 200
        - Mayor que 18 500 
"""

age_1 = input("Inserta edad: ")
age = int(age_1)
if age <= 4:
    print("Entrada gratis")
elif age >4 and age <= 18:
    print("Paga 200")
elif age >18:
    print("Paga 500")


#multiple if-elif-else blocks

age_1 = input("Inserta edad: ")
age = int(age_1)
if age >18 and age <=100:
    print("Paga 500")
elif age >4 and age <= 18:
    print("Paga 200")
elif age >= 0 and age< 4:
    print("Entrada gratis")


# multiple if-elif-else blocks
# else en ocasiones se puede omitir (depende la situacion)
# como se va ejecutando el if-elif-else

## Multiple coditions
print("Guisos en bloque if-else")
guisos= ["desebrada", "salsa verde", "picadillo"]

if "desebrada" in guisos:
    print("Hay desebrada".upper()) 
else:
    print("no Hay desebrada".upper()) 

if "salsa verde" in guisos:
    print("Hay salsa verde".swapcase()) 
else:
    print("no Hay salsa verde".swapcase())

if "picadillo" in guisos:
    print("Hay picadillo".title()) 
else:
    print("no Hay picadillo".title()) 

if "mole" in guisos:
    print("Hay mole") 
else:
    print("no Hay mole") 

print("Guisos en bloque if-elif-else")
guisos=["desebrada", "salsa verde", "picadillo"]
if "desebrada" in guisos:
    print("Hay desebrada")
elif "mole" in guisos:
    print("Hay mole")  
elif "salsa verde" in guisos:
    print("Hay salsa verde")  

print("Listas vacias")
# Listas vacias
guisos= [] #Lista vacia
if guisos:
    print("hay guisos")
else:
    print("en la casa hay fijoles")


##Utilzando dos listas 
guisos_disponibles= ["salsa verde", "deshebrada", "picadillo", "huevo con chorizo"]
guisos_a_ordenar=["barbacoa","deshebrada", "cabrito"]

print("Que guiso quiere?")
for guiso in guisos_a_ordenar:
    if guiso in guisos_disponibles:
        print(f"Si tenemos {guiso}")
    else:
        message_no_guiso = f"""
        Una disculpa somos la cafe de la uat no tenemos {guiso}"""
print(message_no_guiso)
print("realizando pedido")
