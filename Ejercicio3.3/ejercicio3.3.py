print('por favor inserte la cantidad de lapices a comprar')
cantidad_lapices=int(input())

if cantidad_lapices>1000:
    precio_lapiz_mayorista=85
    Costo_pago_lapices=cantidad_lapices*precio_lapiz_mayorista
    print(Costo_pago_lapices)
    
elif cantidad_lapices==1000:
    precio_lapiz_mayorista=85
    Costo_pago_lapices=cantidad_lapices*precio_lapiz_mayorista
    print(Costo_pago_lapices)

else :
    precio_lapiz_minorista=90
    Costo_pago_lapices1=cantidad_lapices*precio_lapiz_minorista
    print(Costo_pago_lapices1)


