# While con centinela
"""
    Sumar n numeros hasta que el usuario escriba la palabra exit. 
    Tambien vamos a decir cuantos numeros ingreso el usuario.
    Cual es el minimo y cual es el maximo
    
"""
print("\n Captura de importes. Bienvenidos a la calculadora de importes")
print("Pa salir escribe exit")
counter=0
sum_values=0.0
minimum= None
maximum = None

while True:
    user_input = input("Ingresa una cantidad:")
    if user_input == "exit":
        break
    try: 
        quantity= float(user_input)
    except:
        print("Ingresa un valor valido")
        continue
    
    counter+=1 #counter = counter + 1 (Contador)
    sum_values+=quantity # sum = sum + quantity (acumulador)

    if minimum is None or quantity < minimum:
        minimum= quantity
    if maximum is None or quantity > maximum:
        maximum = quantity


print(sum_values)
print(counter)
print(maximum)
print(minimum)

"""
    Docstring for understanging_while_sentinel

    sentinel is useful when you want to ensure that a loop runs
    at least once before checking a condition

    Vamos a realizar un ejemplo que realice la suma de n numeros ingresados por el usuario,
    no sabemos cuantos numeros se ingresaran, quiere contabilizar cuantos numeros
    se han ingresado, mostrar la suma , el minimo y el maximo de los numeros ingresados. 
"""



