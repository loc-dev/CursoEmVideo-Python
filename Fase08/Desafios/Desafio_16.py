#   Fase 08 - Utilizando módulos
#   Desafio 16
#   Faça um programa que leia o comprimento do cateto oposto e
#   do cateto adjacente de um triângulo retângulo,
#   calcule e mostre o comprimento da hipotenusa.

import math

print('=' * 25)
print('  TEOREMA DE PITÁGORAS')
print('=' * 25)
print('')
cat_op = float(input('Digite o valor do cateto oposto: '))
cat_adj = float(input('Digite o valor do cateto adjacente: '))

cat_op = math.pow(cat_op, 2)
cat_adj = math.pow(cat_adj, 2)
sum_cats = cat_op + cat_adj

print('O comprimento da hipotenusa é {}'.format(math.trunc(math.sqrt(sum_cats))))
