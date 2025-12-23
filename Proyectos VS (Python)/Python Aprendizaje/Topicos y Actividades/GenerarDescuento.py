monto_consumo = float(input("Ingrese el monto de consumo: "))
if monto_consumo > 50 and monto_consumo <= 100:
    descuento = 0.1
elif monto_consumo > 100 and monto_consumo <= 200:
    descuento = 0.2
elif monto_consumo > 200:
    descuento = 0.3
else:
    descuento = 0.0

monto_descuento = monto_consumo * descuento
total = monto_consumo - monto_descuento

print("\nResumen de la cuenta")
print("Monto de consumo: ", monto_consumo)
print("Descuento Aplicado: ", descuento * 100, "%")
print("Monto Total con descuento", total)

