#   Fase 08 - Utilizando módulos
#   Desafio 18
#   Um professor quer sortear um dos seus quatro alunos
#   para apagar o quadro. Fala um programa que ajude ele,
#   lendo o nome deles e escrevendo o nome do escolhido.

import random

aluno_01 = input('Digite o nome do 1ª aluno(a): ')
aluno_02 = input('Digite o nome do 2ª aluno(a): ')
aluno_03 = input('Digite o nome do 3ª aluno(a): ')
aluno_04 = input('Digite o nome do 4ª aluno(a): ')

aluno = random.choice([aluno_01, aluno_02, aluno_03, aluno_04])

print('O aluno(a) escolhido(a) é : {}'.format(aluno))
