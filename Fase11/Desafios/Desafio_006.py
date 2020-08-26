# Fase 07 - Operadores Aritméticos

# Desafio 006

# Crie um programa que leia quanto dinheiro uma pessoa tem
# na carteira e mostre quantos dólares ela pode comprar.
# Considere US$ 1.00 = R$ 5,62

from time import sleep

print('$' + '-' * 20 + '$')
print('$   DESAFIO 006' + ' ' * 6 + '$')
print('$' + '-' * 20 + '$')

print('')

nome = str(input('Olá, qual é o seu nome ? '))

print('')
reais = float(input('Olá {},'
                    '\nQual é o valor desejado a converter em dólar: R$ '.format(nome)))

print('O seu valor em R$ {}{:.2f}{}, convertido em dólar, será:'.format('\033[1;33m', reais, '\033[m'))
print('COTAÇÃO DO DIA: \033[30mUS$ 5.62\033[m')
print('PROCESSANDO...')
sleep(3)

print('')
print('US$ {}{:.2f}{}'.format('\033[1;34m', reais / 5.62, '\033[m'))
