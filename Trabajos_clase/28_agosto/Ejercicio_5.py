#Pedir funciones de la biblioteca
from utiles_es import pedir_texto, pedir_entero, pedir_float, pedir_opcion, titulo, _OK, _ERR, _WARN, _INFO

#Entrada de datos / inputs y declaracion de variables:
nombre = pedir_texto("Ingrese su nombre: ")
cant_produc = pedir_entero("Ingrese la cantidad de productos: ", 0)
monto_total = pedir_float("Ingrese el monto total de la compra: ", 0)
medio_pago = pedir_opcion("Elige tu medio de pago: ",{"efectivo", "debito", "credito", "mercado pago"})
descuento = 0
recargo = 0

#Condicionales del medio de pago:

if medio_pago == "efectivo":
    descuento = monto_total*0.15
elif medio_pago == "debito":
    descuento = monto_total*0.10
elif medio_pago == "credito":
    recargo = monto_total*1.05-monto_total
elif medio_pago == "mercado pago" and monto_total > 10000:
    descuento = monto_total*0.2

#En caso de superar 10 productos:
if cant_produc > 10:
    descuento = descuento + (monto_total*0.05)

#Salidas
titulo("CARRITO DE COMPRAS")
print (_OK + f"Nombre:                   {nombre}")
print (_OK + f"Cantidad de productos:    {cant_produc}")
print (_OK + f"Precio total:            ${monto_total}")
print (_OK + f"Descuento aplicado:      ${descuento}")
print (_OK + f"Recargo aplicado:        ${recargo}")
print (_OK + f"Total:                   ${monto_total-descuento+recargo}")