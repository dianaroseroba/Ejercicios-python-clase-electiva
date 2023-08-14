print('por favor ingrese lado a')
lado_a=int(input())

print('por favor ingrese lado b')
lado_b=int(input())

print('por favor ingrese lado c')
lado_c=int(input())

#calculando el área del rectangulo
base_rectangulo=lado_b
altura_rectangulo=lado_c

area_rectangulo=base_rectangulo*altura_rectangulo

#calculando área del triangulo
altura_triangulo=lado_a-lado_c
base_triangulo=lado_b

area_triangulo=(base_triangulo*altura_triangulo)/2

#calculando área total
area=area_rectangulo+area_triangulo

print('el área total es:')
print(area)
