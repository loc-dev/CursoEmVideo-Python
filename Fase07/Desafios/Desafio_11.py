#   Fase 07 - Operadores Aritméticos
#   Desafio 11
#   Crie um programa que leia quanto dinheiro
#   uma pessoa tem na carteira e mostre quantos
#   dólares ela pode comprar.

dolar = 5.65
saldo = float(input('Quantos reais você tem na carteira? '))

print('Posso comprar US${:.2f}'.format(saldo * dolar))
