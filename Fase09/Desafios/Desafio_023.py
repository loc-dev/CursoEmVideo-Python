#   Fase 09 - Manipulando Texto
#   Desafio 23
#   Crie um programa que leia o nome de uma cidade
#   e diga se ela começa ou não com o nome "SANTO".

cidade = input("O nome da cidade: ")

print('')
print("Essa cidade começa com o nome (Santo) se sim, o resultado será 0,\n"
      "senão, o resultado será -1: \n"
      "{}".format(cidade.upper().find('SANTO')))
