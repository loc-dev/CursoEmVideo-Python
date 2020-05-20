# Fase 08 - Utilizando módulos
# Teoria
# A biblioteca "random", gerando números pseudo-aleatórios

import random

# Funcionalidade : ( random ) onde gera uma flutuação aleatória na faixa entre 0 e 1
num = random.random()

print('Computador qual é o número: {}'.format(num))
print('')

# Funcionalidade : ( randint ) irá gerar número aleatório inteiro entre o tanto especificado
num = random.randint(1, 10)

print('Computador qual é o número: {}'.format(num))
