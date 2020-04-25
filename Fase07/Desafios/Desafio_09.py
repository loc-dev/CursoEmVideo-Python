#   Fase 07 - Operadores Aritméticos
#   Desafio 09
#   Escreve um programa que leia um valor em metros
#   e o exiba convertido em centímetros e milímetros.

m = float(input('Indica qual é o valor em metro(m): '))
print('Valor convertido em centímetros(cm): {:.0f}cm'.format(m * 100))
print('Valor convertido em milímetros(mm): {:.0f}mm'.format(m * 1000))
