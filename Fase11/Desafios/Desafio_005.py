# Fase 07 - Operadores Aritméticos

# Desafio 005

# Faça um programa que leia um número inteiro qualquer
# e mostre na tela a sua tabuada.

print('$' + '-' * 20 + '$')
print('$   DESAFIO 005' + ' ' * 6 + '$')
print('$' + '-' * 20 + '$')

print('')

n = int(input('Digite um número inteiro qualquer: '))

print('')
print('{}{}{} * {}{}{} = {}{}{} \n'
      ''.format('\033[1;30m', n, '\033[m', '\033[1;30m', 1, '\033[m', '\033[1;34m', n * 1, '\033[m'))
print('{}{}{} * {}{}{} = {}{}{} \n'
      ''.format('\033[1;30m', n, '\033[m', '\033[1;30m', 2, '\033[m', '\033[1;34m', n * 2, '\033[m'))
print('{}{}{} * {}{}{} = {}{}{} \n'
      ''.format('\033[1;30m', n, '\033[m', '\033[1;30m', 3, '\033[m', '\033[1;34m', n * 3, '\033[m'))
print('{}{}{} * {}{}{} = {}{}{} \n'
      ''.format('\033[1;30m', n, '\033[m', '\033[1;30m', 4, '\033[m', '\033[1;34m', n * 4, '\033[m'))
print('{}{}{} * {}{}{} = {}{}{} \n'
      ''.format('\033[1;30m', n, '\033[m', '\033[1;30m', 5, '\033[m', '\033[1;34m', n * 5, '\033[m'))
print('{}{}{} * {}{}{} = {}{}{} \n'
      ''.format('\033[1;30m', n, '\033[m', '\033[1;30m', 6, '\033[m', '\033[1;34m', n * 6, '\033[m'))
print('{}{}{} * {}{}{} = {}{}{} \n'
      ''.format('\033[1;30m', n, '\033[m', '\033[1;30m', 7, '\033[m', '\033[1;34m', n * 7, '\033[m'))
print('{}{}{} * {}{}{} = {}{}{} \n'
      ''.format('\033[1;30m', n, '\033[m', '\033[1;30m', 8, '\033[m', '\033[1;34m', n * 8, '\033[m'))
print('{}{}{} * {}{}{} = {}{}{} \n'
      ''.format('\033[1;30m', n, '\033[m', '\033[1;30m', 9, '\033[m', '\033[1;34m', n * 9, '\033[m'))
print('{}{}{} * {}{}{} = {}{}{} \n'
      ''.format('\033[1;30m', n, '\033[m', '\033[1;30m', 10, '\033[m', '\033[1;34m', n * 10, '\033[m'))
