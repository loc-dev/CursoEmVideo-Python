#   Fase 10 - Condições ( Parte 1 )
#   Desafio 31
#   Faça um programa que leia um ano qualquer
#   e mostre se ele é BISSEXTO.

ano = int(input('Digite um ano qualquer: '))

ano = str(ano)

if ano[-2:] != "00":
    ano = int(ano)
    if ano % 4 == 0:
        print('É Bissexto')
    else:
        print('Não é Bissexto')
else:
    ano = int(ano)
    if ano % 400 == 0:
        print('É Bissexto')
    else:
        print('Não é Bissexto')
