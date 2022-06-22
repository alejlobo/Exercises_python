#Haga un programa que dado un número entero N, imprima todos los números desde N hasta 1.
#Ejemplo: si N=4, el programa imprime lo siguiente:


import time


i = 0
inicio = int(input("Digite desde cual número quiere hacer la cuenta regresiva: "))

while inicio > i:
    print(inicio)
    time.sleep(1)
    inicio-=1
