#   Fase 07 - Operadores Aritméticos
#   Desafio 08
#   Desenvolva um programa que leia as duas notas de um aluno,
#   calcule e mostre a média.

nome = input('Digite o nome do(a) Aluno(a): ')

nota_01 = float(input('Qual é a nota da primeira prova: '))
nota_02 = float(input('Qual é a nota da segunda prova: '))

print('Aluno(a): {}'.format(nome))
print('Média: {:.2f}'.format((nota_01 + nota_02) / 2))
