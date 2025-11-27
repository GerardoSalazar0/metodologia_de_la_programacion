"""
    Estrucura basica del bucle while:

    conditional --- boleano

    while conditional:
        actiones

"""

# estructura try- except

# While infinito
while True: # While infinito 
    try:
        number = int(input("Escribe un numero entre 25 y 50:"))
        if number >= 25 and number <= 50:
            print("Hola estas dentro del rango")
            break
        else:
            print("Lastima margarito")
    except ValueError:
        print("Caracter invalido")
    except KeyboardInterrupt:
        print("Caracter invalido")
        break
print("tupu")
