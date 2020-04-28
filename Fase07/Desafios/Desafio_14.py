#   Fase 07 - Operadores Aritméticos
#   Desafio 14
#   Faça um algoritmo que leia o salário de um funcionário
#   e mostre seu novo salário, com 15% de aumento.

nome_func = str(input('Digite o nome do funcionário(a): '))
sal_func = float(input('Digite o salário de {}: '.format(nome_func)))
print('')

print('O salário de {}, teve um reajuste de 15%,'.format(nome_func), end=' ')
print('agora o seu novo salário é, R${:.2f}'.format(((sal_func * 15) / 100) + sal_func))
