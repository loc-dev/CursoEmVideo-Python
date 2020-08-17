# Fase 10 - Condições ( Parte 1 )
# Teoria
# Estrutura Condicional

# Simples

print('Estrutura Condicional Simples')
print('Exemplo:')
nome = input('Como você se chama? ')

if (nome == "Leonardo"):
    print('Verdade, o seu nome é {}'.format(nome))

# Composta
print('')
print('Estrutura Condicional Composta')
print('Exemplo:')
tempo = int(input('Quantos anos tem o seu carro? '))

if (tempo<= 3):
    print('Carro novo')
else:
    print('Carro velho')
print('--FIM--')
