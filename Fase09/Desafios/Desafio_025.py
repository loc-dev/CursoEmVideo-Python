#   Fase 09 - Manipulando Texto
#   Desafio 25
#   Faça um programa que leia uma frase pelo teclado e mostre:
#   - Quantas vezes aparece a letra "A".
#   - Em que posição ela aparece a primeira vez.
#   - Em que posição ela aparece a última vez.

# frase = "Embora ninguém possa voltar atrás e fazer um novo começo, qualquer um pode começar agora e fazer um novo fim."
# frase2 = "Mantenha o foco no objetivo, centralize a força para lutar e utilize a fé para vencer."

frase = input("Digite uma frase: ")

print('')
print("Quantas vezes aparece a letra (A): {}".format(frase.upper().count('A')))

print('')
print("Em que posição ela aparece a primeira vez: {}º posição".format(frase.upper().find('A')))

print('')
print("Em que posição ela aparece a última vez: {}º posição".format(frase.upper().rfind('A')))
