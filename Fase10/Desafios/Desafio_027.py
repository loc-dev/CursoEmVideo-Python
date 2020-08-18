#   Fase 10 - Condições ( Parte 1 )
#   Desafio 27
#   Escreva um programa que faça o computador "pensar"
#   em um número inteiro entre 0 e 5 e peça para o usuário
#   tentar descobrir qual foi o númerp escolhido pelo computador.

#   O programa deverá escrever na tela se o usuário venceu ou perdeu.

import random

computador = random.randint(0, 5)

usuario = int(input('Qual é o número inteiro de 0 à 5, meu computador está pensando: '))

if usuario == computador:
    print('PARABÉNS! Você venceu!')
else:
    print('Não foi dessa vez, você perdeu!')
