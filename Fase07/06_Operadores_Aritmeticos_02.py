# Fase 07 - Operadores Aritméticos
# Teoria
# Nesse script, iremos fazer todos os operadores aritméticos,
# utilizando o método da string .format().

print('Exemplo 01')
n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
print('A soma vale {}'.format(n1 + n2))
print('')

# Quando é que uso com uma variável para intermediação?
# Visto que o exemplo 01, não utilizamos uma variável,
# pois, realizamos dentro do método.
# Normalmente quando precisamos do certo valor depois.

print('Exemplo 02')
n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
s = n1 + n2
sb = n1 - n2
m = n1 * n2
d = n1 / n2
e = n1**n2
di = n1 // n2
r = n1 % n2
print('Soma é {}; Resto {}; Produto {}; Quociente {}'.format(s, sb, m, d))
print('Potência é {}; Divisão inteira é {}; Resto da divisão é {}'.format(e, di, r))
