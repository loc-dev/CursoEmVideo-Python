# Fase 08 - Utilizando módulos
# Teoria
# Explorando a biblioteca "math"

import math

num = int(input('Digite um número: '))

raiz = math.sqrt(num)

# Padrão
print('')
print('Utilizando a formatação de ponto flutuante dentro da máscara {}')
print('A Raiz quadrada de {} é {:.2f}'.format(num, raiz))

# Com a Funcionalidade : ceil
print('')
print('Utilizando o módulo math, e aplicando a funcionalidade ( ceil ) ')
print('A Raiz quadrada de {} é {}'.format(num, math.ceil(raiz)))

# Com a Funcionalidade : floor
print('')
print('Utilizando o módulo math, e aplicando a funcionalidade ( floor ) ')
print('A Raiz quadrada de {} é {}'.format(num, math.floor(raiz)))
