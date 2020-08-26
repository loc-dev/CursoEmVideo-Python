# Fase 09 - Utilizando módulos

# Desafio 010

# Crie um programa que leia o nome de uma cidade
# e diga se ela começa ou não com o nome "SANTO".

print('$' + '-' * 20 + '$')
print('$   DESAFIO 010' + ' ' * 6 + '$')
print('$' + '-' * 20 + '$')

print('')

cidade = input('O nome da cidade: ')

print('')
print('Essa cidade começa com o nome (SANTO), '
      '\nse sim o resultado será \033[1;30m0\033[m, senão, o resultado será \033[1;30m-1\033[m: ')

print('')
print('{}{}{}'.format('\033[1;33m', cidade.upper().find('SANTO'), '\033[m'))
