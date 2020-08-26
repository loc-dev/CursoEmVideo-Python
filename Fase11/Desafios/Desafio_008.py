# Fase 08 - Utilizando módulos

# Desafio 008

# Um professor quer sortear um dos seus quatro alunos
# para apagar o quadro. Faça um programa que ajude
# ele, lendo o nome deles e escrevendo o nome do escolhido.

from random import choice

print('$' + '-' * 20 + '$')
print('$   DESAFIO 008' + ' ' * 6 + '$')
print('$' + '-' * 20 + '$')

print('')

a01 = input('Digite o nome do 1º aluno(a): ')
a02 = input('Digite o nome do 2º aluno(a): ')
a03 = input('Digite o nome do 3º aluno(a): ')
a04 = input('Digite o nome do 4º aluno(a): ')

aluno = choice([a01, a02, a03, a04])

print('O aluno(a) escolhido(a) é : {}{}{}'.format('\033[4;36m', aluno, '\033[m'))
