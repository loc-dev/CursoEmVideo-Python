#   Fase 09 - Manipulando Texto
#   Desafio 24
#   Crie um programa que leia o nome de uma pessoa
#   e diga se ela tem "SILVA" no nome.

nome = input("Digite o seu nome completo: ")
nome = nome.upper()

print('')
print("Existe (Silva) no seu nome completo: \n"
      "{}".format("SILVA" in nome))
