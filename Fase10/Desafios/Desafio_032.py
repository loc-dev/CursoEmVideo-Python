#   Fase 10 - Condições ( Parte 1 )
#   Desafio 32
#   Faça um programa que leia três números
#   e mostre qual é maior e qual é o menor.

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))

if n1 > n2:
    if n1 > n3:
        print('O maior número é {}'.format(n1))
        print('O menor número é {}'.format(n3))
    else:
        print('O maior número é {}'.format(n3))
        print('O menor número é {}'.format(n2))
else:
    if n2 > n3:
        print('O maior número é {}'.format(n2))
        print('O menor número é {}'.format(n1))
    else:
        print('O maior número é {}'.format(n3))
        print('O menor número é {}'.format(n1))
