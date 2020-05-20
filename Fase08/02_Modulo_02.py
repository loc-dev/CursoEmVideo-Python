# Fase 08 - Utilizando módulos
# Teoria
# Explorando a biblioteca "math"

# Parte 02

# Segundo modo de utilizar biblioteca - Mais específico

from math import sqrt, floor

num = int(input('Digite um número: '))

raiz = sqrt(num)

# Funcionalidade : ( sqrt )
print('')
print('Utilizando o módulo math, e aplicando a funcionalidade ( sqrt ) ')
print('A raiz quadrada de {} é {:.2f}'.format(num, raiz))

# Duas Funcionalidades : ( sqrt e floor )
print('')
print('Utilizando o módulo math, e aplicando duas funcionalidades ( sqrt e floor ) ')
print('A raiz quadrada de {} é {:.2f}'.format(num, floor(raiz)))
