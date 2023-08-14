print('por favor escribir los litros de leche producidos en el dìa')
litros_dia=int(input())

print('por favor escribir el precio del litro de leche')
precio_litro_leche=int(input())

#calcular de litros a galones
galon_leche=3785

numero_galones_dia=litros_dia/galon_leche

#calcular precio galon
precio_galon_leche=galon_leche*precio_litro_leche
Pago_productor=precio_galon_leche*numero_galones_dia
print('el costo a recibir es:')
print(Pago_productor)

print('el numero de galones es:')
print(numero_galones_dia)
