#determinar si las medidas recibidas puedes realizar un triangulo
#a y b      a y c       b y c



from xmlrpc.client import boolean


lado_a = float
lado_b = float
lado_c = float


print("Favor digite la medida de 3 lados para comprobar que puedan formar un triangulo")

lado_a = float(input("Primero, digite la medida del lado A: "))
lado_b = float(input("Gracias, ahora digite la medida del lado B: "))
lado_c = float(input("Por último, digite  la medida del lado C: "))



if (lado_a + lado_b > lado_c and lado_a + lado_c> lado_b and lado_b + lado_c > lado_a):
    print("Utilizando las 3 medidas brindadas sí se puede hacer un triangulo")
    if (lado_a==lado_b and lado_b==lado_c):
        print("El triángulo es equilatero")
    if (lado_a==lado_b and lado_b!=lado_c):
        print("El triángulo es isósceles")
    if (lado_a!=lado_b and lado_b!=lado_c):
        print("El triángulo es escaleno")
else: print("No es posible hacer un triángulo con esas medidas")