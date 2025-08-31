import utiles_es as util
from utiles_es import pedir_texto, pedir_entero, titulo

#Declaracion de variables e inputs
nombre_completo = pedir_texto("Ingrese su nombre completo: ")
edad = pedir_entero("Ingrese su edad: ", 0)
ingresos_anuales = pedir_entero("Ingrese sus ingresos anuales: ", 0)
impuestos = 0
#Condicionales para el cobro de impuestos
if edad < 65:
    if ingresos_anuales >= 500000 and ingresos_anuales < 2000000:
        print (f"{nombre_completo}, usted debe pagar el 10% de impuestos.")
        impuestos = ingresos_anuales * 0.10
    elif ingresos_anuales >= 2000000 and ingresos_anuales <= 5000000:
        print (f"{nombre_completo}, usted debe pagar el 20% de impuestos.")
        impuestos = ingresos_anuales * 0.15
    elif ingresos_anuales > 5000000:
        print (f"{nombre_completo}, usted debe pagar el 35% de impuestos.")
        impuestos = ingresos_anuales * 0.35
    else:
        print (f"{nombre_completo}, usted no paga impuestos.")
else:
    print("Usted no paga impuestos")


#Salidas
titulo("Resumen de impuestos anuales")
print(f"Nombre completo: {nombre_completo}")
print(f"Edad: {edad}")
print(f"Ingresos anuales: ${ingresos_anuales}")
titulo("Resumen:")
print(f"    Ingresos:       ${ingresos_anuales}")
print(f"    Impuestos:      ${impuestos}")
print(f"    Total neto:     ${ingresos_anuales-impuestos}")