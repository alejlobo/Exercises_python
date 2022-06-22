#determinar si un estudiante logra una beca
#4 materias, sin reprobar
#promedio > 90 and notas >= 80
#promedio => 85 and cal_asis = "A" or "B"


import string


materias = 0
mat_a= 0.0
mat_b= 0.0
mat_c= 0.0
mat_d= 0.0
prom = 0.0
cali_asis = ""
asis = ""


print("Bienvenidos a la plataforma de Becas Internacionales")
print("A continuación se le solicitará cierta información")

materias = int(input("Favor digige el número de materias cursadas este cuatrimestre: "))

if (materias == 4) :
    print("Perfecto! Ahora, digite las notas de las 4 materias cursadas")
    mat_a = float(input("Favor digite la nota de la primera materia: "))
    mat_b = float(input("Digite la nota de la segunda materia: "))
    mat_c = float(input("Ahora, la nota de la tercera materia: "))
    mat_d = float(input("Por último, digite la nota de la cuarta materia: "))
    prom = (mat_a + mat_b + mat_c) / 3


    asis = input("En el presente cuatrimestre fue asistente? SI o NO.")

    if (asis == "SI" ): 
        cali_asis = input("Digite la letra de su calificación: ")
    else: cali_asis= "x"
    if (mat_a>= 70 and mat_b>= 70 and mat_c>= 70 and mat_d >= 70):    

        if (prom >= 85 and cali_asis == "A" or "B"):
            print("Felicidades, ud es elegible para una Beca. Favor póngase en contacto con nosotros.")
        
        if (mat_a> 80 and mat_b> 80 and mat_c> 80 and mat_d > 80 and prom >=90):
            print("Felicidades, ud es elegible para  una Beca . Favor póngase en contacto con nosotros.")

    else: print("No ha aprobado todas las materias :c")
else: print("No ha matriculado el mínimo de materias solicitadas")

