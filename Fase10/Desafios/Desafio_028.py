#   Fase 10 - Condições ( Parte 1 )
#   Desafio 28
#   Escreva um programa que leia a velocidade de um carro.
#   Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
#   A multa vai custar R$7,00 por cada Km acima do limite.

vel = int(input('Qual foi a velocidade do carro (Km): '))

if vel > 80:
    print('Você foi multado!')
    m = 7 * (vel - 80)
    print('A multa foi de R$ {}'.format(m))
