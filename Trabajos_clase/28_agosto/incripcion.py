nombre = input("Ingrese su nombre: ")
dni = input("Ingrese su DNI: ")
edad = int(input("Ingrese su edad: "))
obra_social = input("Tiene obra social? (si/no): ")
prioridad = int(input("Ingrese su prioridad medica (1. emergencia, 2. urgente, 3. control): "))

if prioridad == 2: # prioridad urgente
    if obra_social == "si":
        print ("Turno en menos de 24 hs")
    else:
        print ("Turno en menos de 48 hs")
elif prioridad == 3:
    if edad > 65:
        print("Turno preferencial en 72 hs")
    else:
        print("Turno normal en 7 días.")    
else:
    print("Turno inmediato, dirijase a guardia")