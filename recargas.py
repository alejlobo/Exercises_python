#Haga un programa que reciba el nombre del cliente, el monto de la
# recarga y la cantidad de años que tienen de ser cliente, y retorne si le aplica o no la promoción, y el monto total de
# la recarga incluyendo la promoción

# D: menos de un año
# C: 1 a 3 años
# B: 3 a 5 años
# A: mas de 5 años

#recarga < 2000 or recarga > 5000 or cliente = D

#2000 a 3800 and cliente C (duplicado)
#recarga > 3800 and recarga <= 5000 and cliente B (triplicado)
#cliente A (triplicado)

from xmlrpc.client import boolean


nombre = input("Nombre de la persona que tramita: ")
numero = int(input("Número al que desea aplicar la recargar: "))
recarga = int(input("Monto de la recarga: "))
print("Hace cuanto tiempo es cliente de nuestra empresa")
cliente = input("D. Menos de 1 año C. 1 a 3 años B. 3 a 5 años A. Mas de 5 años: ")
invalido = False

invalido = recarga < 2000 or recarga > 5000 or cliente == "D" 

if invalido == False:
    if recarga >= 2000 and recarga <= 3800 and cliente.upper() == "C":
        recarga = recarga *2
        print("La promoción de nuestro mes le duplicó su recarga para un total de: ",recarga)
    elif recarga >3800 and cliente.upper() == "B":
        recarga = recarga *3
        print("La promoción de nuestro mes le triplicó su recarga para un total de: ",recarga)
    elif cliente.upper() == "A":
        recarga= recarga *3
        print("Gracias por su larga preferencia! Su recarga fue triplicada para un total de: ",recarga)
else: print("La promoción no es válida. Su recarga será: ",recarga)