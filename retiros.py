balance = int(input("Digite el balance actual de su cuenta: "))


while balance >= 0 :
    # retiro = int(input("Digite el monto que desea retirar: "))
    # print("*********************************************************")
    # balance -= retiro
    balance-=int(input("Digite el monto que desea retirar: "))


    if balance >= 0:
        print("El balance restante es de: ",balance)

    if  balance ==0:
        print("No es posible retirar mas dinero")
        exit()


print("Monto insuficiente")
