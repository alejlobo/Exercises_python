


import time


promedio =0
acum=0
i=0
materias=0


materias = int(input("Digite cuantas materias cursa: "))

while materias >0:
    nota = int(input("NOTA " + str(i+1) + ": "))
    acum+=nota
    i+=1
    materias-=1
promedio = acum / i


contador = 3
while contador > 0:
    print("Procesando nota...")
    time.sleep(1)
    contador-=1


if promedio >=70:
    print("Su promedio es de: ",promedio,". Ud está aprobado :)")
elif promedio >=60 and promedio <70:
    print("Su promedio es de: ",promedio,". Ud está aplazado :/")
elif promedio < 60 :
    print("Su promedio es de: ",promedio,". Ud está reprobado :c")