print('ingrese por favor lado a en metros de la alberca')
lado_a=int(input())

print('ingrese por favor lado l en metros de la alberca')
lado_l=int(input())

print('ingrese por favor lado p en metros de la alberca')
lado_p=int(input())

print('ingrese por favor valor en pesos del metro cubico de agua')
valor_m3=int(input())

#calculando volumen de la alberca
Volumen_alberca=lado_a*lado_l*lado_p

print(Volumen_alberca)

#calculando pago de llenado de alberca en m3
costo_pago_m3=Volumen_alberca*valor_m3

print(costo_pago_m3)