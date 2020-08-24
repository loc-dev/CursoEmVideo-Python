# Fase 11 - Cores no terminal
# Prática

# Usando as cores - Determine a média anual final do aluno,
# caso ele seja aprovado, utilize a cor verde, senão utilize a
# cor vermelha

nome = str(input('Digite o nome do Aluno(a): '))
n1 = float(input('Digite a nota de {} no 1º Bim: '.format(nome)))
n2 = float(input('Digite a nota de {} no 2º Bim: '.format(nome)))
n3 = float(input('Digite a nota de {} no 3º Bim: '.format(nome)))
n4 = float(input('Digite a nota de {} no 4º Bim: '.format(nome)))

soma = n1 + n2 + n3 + n4
media = soma / 4

if media >= 7:
    print('Aluno(a) {} foi aprovada com sua média final : \033[1;32m{:.2f}\033[m.\nEstá de \033[32mP\033[33ma\033[34mr\33[35ma\033[32mb\033[33mé\033[34mn\33[35ms\033[31m!!!\033[m'.format(nome, media))
else:
    print('Infelizmente, aluno(a) {} não foi aprovada, sua média final : \033[31m{:.2f}\033[m'.format(nome, media))
