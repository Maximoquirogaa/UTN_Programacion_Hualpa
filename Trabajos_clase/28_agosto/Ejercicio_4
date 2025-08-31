#Pedir funciones de la biblioteca
from utiles_es import pedir_texto, pedir_entero, titulo, _OK, _ERR, _WARN, _INFO

#Entrada de datos / inputs
nombre = pedir_texto("Ingrese su nombre: ")
edad = pedir_entero("Ingrese su edad: ")
años_manejo = pedir_entero("Ingrese la cantidad de años manejando: ")
categoria = ""

#Variables y condicionales
if edad < 18:
    print("Usted no puede conducir")
    exit()
elif edad >= 18 and años_manejo < 1:
    categoria = "PRINCIPIANTE"
elif edad >= 21 and 1 <= años_manejo <= 5:
    categoria = "CONDUCTOR INTERMEDIO"
elif edad >= 30 and años_manejo > 10:
    categoria = "CONDUCTOR PROFESIONAL"
else:
    categoria = "CONDUCTOR ESTÁNDAR"

titulo("Categoría de conductor:")
print(_OK + f"Nombre:        {nombre}")
print(_OK + f"Edad:          {edad}")
print(_OK + f"Categoría:     {categoria}")