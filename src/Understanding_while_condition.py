"""
    Programa que describa un pin correcto 
    definir, un maximo de intentos y el usuario debe ingresar pin correcto
    si pin correcto dar bienvenida, si no error
    si osbrepasa intentos bloqueo
"""

pin_correcto = "777"
max_intentos = 4
intentos = 0

while intentos < max_intentos:
    pin = input("Ingresa tu PIN: ")
    if pin == pin_correcto:
        print("Bienvenido.")
        break
    else:
        print("PIN incorrecto.")
        intentos += 1

if intentos == max_intentos:
    print("Demasiados intentos. Tarjeta bloqueada.")