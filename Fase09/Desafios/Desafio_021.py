#   Fase 09 - Manipulando Texto
#   Desafio 21
#   Crie um programa que leia o nome completo de uma pessoa e mostre:
#   - O nome com todas as letras maiúsculas.
#   - O nome com todas as letras minúsculas.
#   - Quantas letras no total (sem considerar os espaços).
#   - Quantas letras tem o primeiro nome.

nome = input("Digite o seu nome completo: ")

print('')
print("O seu nome completo, com todas as letras maiúsculas:")
print(nome.upper())

print('')
print("O seu nome completo, com todas as letras minúsculas:")
print(nome.lower())

print('')
print("Quantas letras no total:")
print(len(nome.replace(" ", "")))

print('')
print("Quantas letras tem o primeiro nome:")
print(len(nome.split()[0]))
