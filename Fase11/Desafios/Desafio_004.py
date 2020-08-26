# Fase 07 - Operadores Aritméticos

# Desafio 004

# Faça um programa que leia um número inteiro
# e mostre na tela o seu sucessor e antecessor.

print('$' + '-' * 20 + '$')
print('$   DESAFIO 004' + ' ' * 6 + '$')
print('$' + '-' * 20 + '$')

print('')

n = int(input('Digite um número: '))

print('')
print('O sucessor e antecessor de {}{}{}:'.format('\033[4;34m', n, '\033[m'))
print('{}{}{} < {}{}{} < {}{}{}\n'
      ''.format('\033[1;31m', n - 1, '\033[m', '\033[4;34m', n, '\033[m', '\033[1;32m', n + 1, '\033[m'))
