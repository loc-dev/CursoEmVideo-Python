#   Fase 10 - Condições ( Parte 1 )
#   Desafio 34
#   Desenvolva um programa que leia o comprimento de tês retas
#   e diga ao usuário se elas podem ou não formar um triângulo.

r1 = float(input('Digite o comprimento da reta 1 (cm): '))
r2 = float(input('Digite o comprimento da reta 2 (cm): '))
r3 = float(input('Digite o comprimento da reta 3 (cm): '))

a = r1
b = r2
c = r3

maior = 0
menor1 = 0
menor2 = 0

if a > b:
    if a > c:
        maior = a
        menor1 = b
        menor2 = c
    else:
        maior = a
        menor1 = b
        menor2 = a
else:
    if b > c:
        maior = b
        menor1 = a
        menor2 = c
    else:
        maior = c
        menor1 = a
        menor2 = b

if maior < menor1 + menor2:
    print('Pode formar um triângulo')
else:
    print('Não pode formar um triângulo')
