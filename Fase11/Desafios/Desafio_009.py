# Fase 09 - Utilizando módulos

# Desafio 009

# Um professor quer sortear um dos seus quatro alunos
# para apagar o quadro. Faça um programa que ajude
# ele, lendo o nome deles e escrevendo o nome do escolhido.

print('$' + '-' * 20 + '$')
print('$   DESAFIO 009' + ' ' * 6 + '$')
print('$' + '-' * 20 + '$')

print('')

nome = input('Digite o seu nome completo: ')

print('')
print('O seu nome completo, com todas as letras maiúsculas: {}{}{}'.format('\033[1;33m', nome.upper(), '\033[m'))

print('')
print('O seu nome completo, com todas as letras minúsculas: {}{}{}'.format('\033[1;33m', nome.lower(), '\033[m'))

print('')
print('Quantas letras no total: {}{}{}'.format('\033[1;33m', len(nome.replace(" ", "")), '\033[m'))

print('')
print('Quantas letras tem o primeiro nome: {}{}{}'.format('\033[1;33m', len(nome.split()[0]), '\033[m'))
