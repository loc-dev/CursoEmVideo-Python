#   Fase 10 - Condições ( Parte 1 )
#   Desafio 30
#   Desenvolva um programa que pergunte a distância de uma viagem em Km.
#   Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200 Km
#   e R$ 0,45 para viagens mais longas.

distancia = float(input('Qual é a distância da viagem em (Km): '))

if distancia <= 200:
    passagem = 0.50 * distancia
    print('Você vai pagar R$ {:.2f}'.format(passagem))
else:
    passagem = 0.45 * distancia
    print('Você vai pagar R$ {:.2f}'.format(passagem))
