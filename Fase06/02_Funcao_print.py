# Fase 06 - Tipos Primitivos e Saída de Dados
# Teoria
# Modo diferente de usar a função print()

n_01 = int(input('Digite o primeiro valor: '))
n_02 = int(input('Digite o segundo valor: '))

s = (n_01 + n_02)

print('A sua operação é:')
print(n_01, '+', n_02, '=', s)

print('')
print('A soma vale', s)

# Método da string .format()
print('A soma vale {}'.format(s))
