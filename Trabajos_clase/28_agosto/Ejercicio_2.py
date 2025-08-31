#Pedir funciones de la libreria
import utiles_es as util
from utiles_es import pedir_texto, pedir_entero, titulo, _OK, _ERR, _WARN, _INFO

#Input y declaracion de variables
nombre = pedir_texto("Ingrese su nombre: ")
legajo = pedir_entero("Ingrese su nroº de legajo: ")
nota1 = pedir_entero ("Ingrese su primera nota: ", 0, 10)
nota2 = pedir_entero ("Ingrese su segunda nota: ",0, 10)
nota3 = pedir_entero ("Ingrese su tercer nota: ", 0, 10)
estado_academico = ""

#Calcular promedio
promedio = (nota1 + nota2 + nota3) / 3

#Condicionales
if nota1 < 4 or nota2 < 4 or nota3 < 4:
    estado_academico = "DESAPROBADO DIRECTO"
elif promedio < 6:
    estado_academico = "DESAPROBADO"
elif promedio < 8:
    estado_academico = "APROBADO CON FINAL"
else:
    estado_academico = "PROMOCIONADO"              

#Salidas con colores
titulo(_OK + "RESUMEN DEL ALUMNO")
print(_INFO + f"Nombre:     {nombre}\nNº de legajo:     {legajo}\nPromedio:     {promedio:.2f}")
print(_WARN + f"Estado académico:        {estado_academico}")