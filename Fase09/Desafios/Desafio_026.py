#   Fase 09 - Manipulando Texto
#   Desafio 26
#   Faça um programa que leia um nome completo de uma pessoa,
#   mostrando em seguida o primeiro e o último nome separadamente.

nome = input("Digite o seu nome completo: ")

print('')
print("O primeiro nome é: {}".format(nome.split()[0]))

print('')
print("O último nome é: {}".format(nome.split()[-1]))
