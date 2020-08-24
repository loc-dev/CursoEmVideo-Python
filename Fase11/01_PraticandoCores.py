# Fase 11 - Cores no terminal
# Prática

# Frase Clássica

print('Frase com a cor vermelha: ')
print('\033[31mOlá, Mundo!\033[m')

print('')
print('Frase com o fundo amarelo: ')
print('\033[31;43mOlá, Mundo!\033[m')

print('')
print('Frase com a faixa de cor até o último caracter: ')
print('\033[1;31;43mOlá, Mundo!\033[m')

print('')
print('Frase com sublinhado: ')
print('\033[4;30;45mOlá, Mundo!\033[m')
