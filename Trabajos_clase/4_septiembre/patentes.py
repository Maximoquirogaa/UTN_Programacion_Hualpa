numero_patente = []
abc="abcdefghijklmnopqrstuvxwyz"
patente_usuario = int(input("Ingrese un numero:   "))
contador = 0
patente = ""
for z in abc:
    for x in abc:
        for y in abc:
            for i in range(10):
                for j in range(10):
                    for k in range(10):
                        contador = contador + 1
                        if contador == patente_usuario:
                            patente = (f"{z}{x}{y}{i}{j}{k}")
                            print(f"Su patente es: {patente}")
                            break