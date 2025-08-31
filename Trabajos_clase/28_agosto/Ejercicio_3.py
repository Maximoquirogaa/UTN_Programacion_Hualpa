#Pedir funciones de la libreria
import utiles_es as util
from utiles_es import pedir_texto, pedir_entero, titulo, _OK, _ERR, _WARN, _INFO

#Primeros inputs y declaracion de variables
nombre_usuario = pedir_texto("Ingrese su nombre de usuario: ")
saldo_inicial = 100000
pin = int(input("Ingrese su pin: "))
intentos = 0
comision = 0

#Condicionales y validaciones
#Saber si el pin es correcto con un máximo de 3 intentos
if 1000 <= pin <= 9999 :
    print(_OK + "Pin ingresado correctamente!")
else:
    print(_ERR + "Pin incorreto, Intento 1/3")
    intentos = intentos + 1
    pin = int(input("Ingrese su pin: "))
    if 1000 <= pin <= 9999:
        print(_OK + "Pin ingresado correctamente!")
    else:
        print(_ERR + "Pin incorreto, Intento 2/3")
        pin = int(input("Ingrese su pin: "))
        intentos = intentos + 1
        if 1000 <= pin <= 9999:
            print(_OK + "Pin ingresado correctamente!")
        else:
            print(_ERR + "Pin incorreto, Intento 3/3")
            pin = int(input("Ingrese su pin: "))
            intentos = intentos + 1
            if 1000 <= pin <= 9999:
                print(_OK + "Pin ingresado correctamente!")
            else:
                print(_ERR + "Acceso bloqueado, llegó al límite")
                exit()

print(_INFO + (f"Su saldo es de ${saldo_inicial}\n Recuerde que si desea cancelar escriba 'CANCELAR'"))
retiro = pedir_entero(_OK + "Cuanto desea retirar?: ")
if retiro % 1000 == 0 and retiro <= saldo_inicial:
    if retiro >= 20000:
        comision = retiro * 0.02
else:
    print(_ERR + "Error \nSolo tenemos billetes de $1000\nSaldo insuficiente")

#Salidas    
titulo("Resumen del Retiro:")
print(f"Saldo:          ${saldo_inicial}")
print(f"Retiro:         ${retiro}")
print(f"Comisión:       ${comision}")
print(f"Saldo restante: ${saldo_inicial-(retiro+comision)}")