# Fase 01 - Primeiros Comandos

# Desafio 002

# Crie um programa em Python que leia o dia, o mês
# e o ano de nascimento de uma pessoa
# e mostre na tela com a data formatada.

print('$' + '-' * 20 + '$')
print('$   DESAFIO 002' + ' ' * 6 + '$')
print('$' + '-' * 20 + '$')

print('')

d = int(input('Dia: '))
m = int(input('Mês: '))
a = int(input('Ano: '))

print('')
print('Data formatada: \n{}{}{}/{}{}{}/{}{}{}'.format('\033[1;32m', d, '\033[m', '\033[1;33m', m, '\033[m', '\033[1;34m', a, '\033[m'))
