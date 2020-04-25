#   Fase 07 - Operadores Aritméticos
#   Desafio 06
#   Faça um programa que leia um número inteiro
#   e mostre na tela o seu sucessor e antecessor.

n = int(input('Digite um número: '))

ant = n - 1
suc = n + 1

print('O número digitado foi: {}'.format(n))
print('O seu antecessor é {}'.format(ant))
print('O seu sucessor é {}'.format(suc))
