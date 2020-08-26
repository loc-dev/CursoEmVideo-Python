# Fase 01 - Primeiros Comandos

# Desafio 003

# Crie um programa em Python que leia dois números
# e tente mostrar a soma entre eles.

print('$' + '-' * 20 + '$')
print('$   DESAFIO 003' + ' ' * 6 + '$')
print('$' + '-' * 20 + '$')

print('')

n1 = int(input('Digite um número: '))
n2 = int(input('Digite um número: '))

print('')
print('A expressão númerica de adição é:')
print('{}{}{} + {}{}{} = {}{}{}\n'
      ''.format('\033[1;35m', n1, '\033[m', '\033[1;35m', n2, '\033[m', '\033[32m', n1 + n2, '\033[m'))
