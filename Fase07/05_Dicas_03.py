# Fase 07 - Operadores Aritméticos
# Teoria
# A última dica é utilizar o método da string .format(),
# com o uso das chaves {}, a máscara, refinando algumas formatações de saída.

print('Exemplo 01:')
print('Saída com 20 caracteres sendo espaços')
nome = input('Qual é o seu nome? ')
print('Prazer em te conhecer {:20}!'.format(nome))
print('')

print('Exemplo 02:')
print('Fazendo alinhamentos a partir dos espaços destacados')
nome = input('Qual é o seu nome? ')
print('Prazer em te conhecer {:>20}!'.format(nome))
print('')

print('Exemplo 03:')
print('Alinhamento a esquerda, com o sinal de menor ( < )')
nome = input('Qual é o seu nome? ')
print('Prazer em te conhecer {:<20}!'.format(nome))
print('')

print('Exemplo 04:')
print('Centralizando a saída, com acento circunflexo ( ^ )')
nome = input('Qual é o seu nome? ')
print('Prazer em te conhecer {:^20}!'.format(nome))
print('')

# Uma formatação especial

print('Exemplo 05:')
print('20 caracteres de sinal igual ( = ) sendo centralizado')
nome = input('Qual é o seu nome? ')
print('Prazer em te conhecer {:=^20}!'.format(nome))
print('')
