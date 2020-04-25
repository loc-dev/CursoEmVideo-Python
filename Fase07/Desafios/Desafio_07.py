#   Fase 07 - Operadores Aritméticos
#   Desafio 07
#   Crie um algoritmo que leia um número
#   e mostre o seu dobro, triplo e raiz quadrada.

n = int(input('Digite um número: '))

print('O número digitado foi {}'.format(n))
print('O dobro de {} é {}'.format(n, n * 2))
print('O triplo de {} é {}'.format(n, n * 3))
print('A Raiz quadrada de {} é {:.2f}'.format(n, n**(1/2)))
