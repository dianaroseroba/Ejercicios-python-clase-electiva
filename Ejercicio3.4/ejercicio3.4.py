print('por favor ingrese el valor del traje')
valor_traje=int(input())

if valor_traje>2500:
    porcentaje_descuento=25
    costo_total_pago=valor_traje-((valor_traje*porcentaje_descuento)/100)
    print(costo_total_pago)

elif valor_traje==2500:
    porcentaje_descuento1=8
    costo_total_pago1=valor_traje-((valor_traje*porcentaje_descuento1)/100)
    print(costo_total_pago1)
else:
    porcentaje_descuento_compras_menores=8
    costo_total_pago_compras_menores=valor_traje-((porcentaje_descuento_compras_menores*valor_traje)/100)
    print(costo_total_pago_compras_menores)