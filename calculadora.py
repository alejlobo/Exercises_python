calculos=0
total=0.0
operacion=0
menu=0

# rutinas
def datos():
    num1 = int(input("Digite el primer número de la operación: "))
    num2 = int(input("Digite el segundo número de la operación: "))
    return num1,num2


def menu():
    print("1. Suma")
    print("2. Resta")
    print("3.Multiplicación")
    print("4. División")
    print("5. Salir")
    operacion = int(input("Digite el número de la operación que desea realizar: "))
    return operacion


def calculos(num1, num2, operacion):
    total=0
    if operacion == 1:
        total = num1+num2
        exit
    elif operacion == 2:
        total = num1-num2
    elif operacion == 3:
        total = num1*num2
    elif operacion == 4:
        total = num1/num2
    elif operacion == 5:
        print("Saliendo...")
        exit()
    # else: print("Número inválido")
    return total

# principal
num1,num2=datos()
operacion=menu()
total=calculos(num1,num2,operacion)

print("El resultado de la operación es: " + str(total))
