# Fase 08 - Utilizando módulos

# Desafio 007

# Crie um programa que leia um número real qualquer
# pelo teclado e mostre na tela a sua porção inteira.

from math import trunc

print('$' + '-' * 20 + '$')
print('$   DESAFIO 007' + ' ' * 6 + '$')
print('$' + '-' * 20 + '$')

print('')

n = float(input('Digite um número real: '))

print('')
print('O resultado inteiro será:')

print('{}{}{}'.format('\033[1;35m', trunc(n), '\033[m'))
