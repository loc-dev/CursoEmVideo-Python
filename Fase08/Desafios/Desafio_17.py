#   Fase 08 - Utilizando módulos
#   Desafio 17
#   Faça um programa que leia um ângulo qualquer
#   e mostre na tela o valor do seno, cosseno
#   e tangente desse ângulo.

import math

ang_grau = float(input('Digite o valor do ângulo: '))

ang_rad = math.radians(ang_grau)

print('')
print('O Seno de {}º é : {:.6f}'.format(ang_grau, math.sin(ang_rad)))
print('O Cosseno de {}º é : {:.6f}'.format(ang_grau, math.cos(ang_rad)))
print('O Tangente de {}º é : {:.6f}'.format(ang_grau, math.tan(ang_rad)))
