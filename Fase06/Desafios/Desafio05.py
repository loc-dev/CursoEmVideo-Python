#   Fase 06 - Tipos Primitivos e Saída de Dados
#   Desafio 05
#   Faça um programa que leia algo pelo teclado
#   e mostre na tela o seu tipo primitivo
#   e todas as informações possíveis sobre ela.

dado = input('Digite alguma coisa: ')

print('')
print('Informação da variável: {}'.format(dado))
print('Datalhes: ', type(dado))

print('')
print('Método .isnumeric(): ', dado.isnumeric())
print('Método .isalpha(): ', dado.isalpha())
print('Método .isalnum(): ', dado.isalnum())
