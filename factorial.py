


from math import factorial


i=1
factorial =1
n = int(input("Digite un número y el programa regresará su factorial: "))


while i <= n:
    factorial*=i
    i+=1
print("El factorial de", n, "es:",factorial)