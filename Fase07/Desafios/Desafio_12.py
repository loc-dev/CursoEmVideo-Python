#   Fase 07 - Operadores Aritméticos
#   Desafio 12
#   Faça um programa que leia a largura e a altura de uma parede em metros,
#   calcule a sua área e a quantidade de tinta necessária para pintá-la,
#   sabendo que cada litro de tinta, pinta uma área de 2m².

a = float(input('Qual é a altura da parede em metros? '))
l = float(input('Qual é a largura da parede em metros? '))

area = a * l

print('Para pintar uma área de {:.2f}m²'.format(area))
print('A quantidade de tinta necessária será: {:.2f}l'.format(area / 2))
