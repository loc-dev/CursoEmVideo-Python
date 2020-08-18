# Fase 10 - Condições ( Parte 1 )
# Teoria
# Estrutura Condicional

# Com um exemplo clássico
print('Condição Composta')
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2
print('A sua média foi {:.1f}'.format(m))
if m >= 6.0:
    print('Sua média foi boa! PARABÉNS!')
else:
    print('Sua média foi ruim! ESTUDE MAIS!')

# Utilizando Condição Simplificada
print('')
print('Condição Simplificada')
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2
print('A sua média foi {:.1f}'.format(m))
print('PARABÉNS!' if m >= 6.0 else 'ESTUDE MAIS!')
