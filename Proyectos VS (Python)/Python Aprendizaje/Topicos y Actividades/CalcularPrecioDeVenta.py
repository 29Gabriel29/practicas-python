msj1 = float(input("Ingrese valor de producto"))
print(msj1)
# toma del valor del producto

msj2 = float(input("Ingrese valor del IGV (Impuesto General a las Ventas)"))
print(msj2)
# toma del porcentaje de IGV

print("A continuacion se calculara el valor de venta del producto...")
print("El valor de venta es; " , msj1+(msj1 * (msj2/100) ) )
# se calcula tanto la suma del impuesto como el impuesto en si dado el porcemntaje estimado