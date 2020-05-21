#   Fase 08 - Utilizando módulos
#   Desafio 15
#   Crie um programa que leia um número real qualquer
#   pelo teclado e mostre na tela a sua porção inteira.

from math import trunc

n = float(input('Digite um número: '))

print('O número {} tem a parte Inteira {}.'.format(n, trunc(n)))
