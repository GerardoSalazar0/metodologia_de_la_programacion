"""
    Programa que describa un pin correcto 
    definir, un maximo de intentos y el usuario debe ingresar pin correcto
    si pin correcto dar bienvenida, si no error
    si osbrepasa intentos bloqueo
"""

VALID_PIN = "777"   # UPPER SNAKE CASE
MAX_ATTEMPS = 4     # UPPER SNAKE CASE
ATTEMPS = 0

while ATTEMPS < MAX_ATTEMPS:
    pin = input("Ingresa tu PIN: ")
    if pin == VALID_PIN:
        print("Bienvenido.")
        break
    else:
        print("PIN incorrecto.")
        ATTEMPS += 1
        remaining_attemps = MAX_ATTEMPS - ATTEMPS
        if remaining_attemps >0 :
            print("Pin incorrecto. Te quedan", remaining_attemps, "intentos")
        else:
            print("Maximo de intentos, yama")

