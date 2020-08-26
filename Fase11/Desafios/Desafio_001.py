# Fase 01 - Primeiros Comandos

# Desafio 001

# Crie um programa em Python que leia o nome da pessoa

print('$' + '-' * 20 + '$')
print('$   DESAFIO 001' + ' ' * 6 + '$')
print('$' + '-' * 20 + '$')

print('')

nome = str(input('Qual é o seu nome ? '))

print('')
print('Olá, {}{}{} é um prazer te conhecer!'.format('\033[32m', nome, '\033[m'))
