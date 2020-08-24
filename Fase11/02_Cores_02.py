# Fase 11 - Cores no terminal
# Prática

# Usando ANSI escape sequences, com o fundo padrão e a cor do texto em branco

print('\033[30mOlá, Mundo!\033[m')
print('')

# Agora com o texto cor preta e fundo cor a branca

print('\033[7;30mOlá, Mundo!\033[m')
print('')

# Agora com o texto cor branca e fundo vermelho

print('\033[1;30;41mOlá, Mundo!\033[m')
