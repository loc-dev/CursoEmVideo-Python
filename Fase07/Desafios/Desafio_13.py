#   Fase 07 - Operadores Aritméticos
#   Desafio 13
#   Faça um algoritmo que leia o preço de um produto
#   e mostre seu novo preço, com 5 % de desconto.

v_prod = float(input('Qual é preço do produto? '))

desc = 5
desc = ((v_prod * desc) / 100)

print('O preço com 5% de desconto é {}'.format(v_prod - desc))
