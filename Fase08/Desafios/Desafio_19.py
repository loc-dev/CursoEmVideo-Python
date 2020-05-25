#   Fase 08 - Utilizando módulos
#   Desafio 19
#   O mesmo professor do desafio anterior quer sortear
#   a ordem de apresentação de trabalhos dos alunos.
#   Faça um programa que leia o nome dos quatro alunos
#   e mostre a ordem sorteada.

import random

aluno_01 = input('Digite o nome do 1ª aluno(a): ')
aluno_02 = input('Digite o nome do 2ª aluno(a): ')
aluno_03 = input('Digite o nome do 3ª aluno(a): ')
aluno_04 = input('Digite o nome do 4ª aluno(a): ')

alunos = [aluno_01, aluno_02, aluno_03, aluno_04]

print('A ordem de apresentação será : ')
print(random.sample(alunos, 4))
