#   Fase 09 - Manipulando Texto
#   Desafio 22
#   Faça um programa que leia um número de 0 a 9999
#   e mostre na tela cada um dos dígitos separados.

n = input("Digite um número de 0 a 9999: ")

print("Unidade: {}".format(n[3]))
print("Dezena: {}".format(n[2]))
print("Centena: {}".format(n[1]))
print("Milhar: {}".format(n[0]))
