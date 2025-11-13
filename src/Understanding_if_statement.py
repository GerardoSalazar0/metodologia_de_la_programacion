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

