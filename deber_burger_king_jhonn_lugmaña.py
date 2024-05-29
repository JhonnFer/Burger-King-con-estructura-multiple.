print("----------BIENVENIDO AL BURGER_KING------------")

nombre = input("Ingrese su nombre: ")
cedula = input("Ingrese su numero de cedula: ")
correo = input("Ingrese su correo: ")
hamburguesas = int(input("Ingrese el numero de hamburguesas a adquirir: "))

print("Ingrese una de las siguientes tipos de hamburguesas: ")
print("1) Sencilla ")
print("2) Doble ")
print("3) Triple ")
tipo_hamburguesa = int(input("Ingrese la opción: "))
if tipo_hamburguesa not in [1, 2, 3]:
    print("Ese tipo de hamburguesa no existe")
    print("Muchas gracias")
    exit()

print("Ingrese su forma de pago: ")
print("1) Tarjeta de crédito ")
print("2) Efectivo ")
metodo_pago = int(input("Ingrese la opción: "))
if metodo_pago not in [1, 2]:
    print("Ese tipo de pago no existe")
    print("Muchas gracias")
    exit()
    
if tipo_hamburguesa == 1:
    precio_hamburguesa = 1.50
elif tipo_hamburguesa == 2:
    precio_hamburguesa = 2.50
elif tipo_hamburguesa == 3:
    precio_hamburguesa = 3.25

if metodo_pago == 1:
    descuento = 0.05
else:
    descuento = 0.00

precio_final = (precio_hamburguesa * hamburguesas)
precio_final_con_recargo = (precio_final + (precio_final * descuento))  
precio_final_1 = round (precio_final_con_recargo, 2 )

print(f"Genial, {nombre}, el precio final es: {precio_final_1}")
print(f"La factura se enviará a su correo: {correo}")
