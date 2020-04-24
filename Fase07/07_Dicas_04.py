# Fase 07 - Operadores Aritméticos
# Teoria
# Essa é uma dica bônus, podemos formatar um saída de Números Reais (float)
# e, também veja que cada função print() é concedida uma nova linha.
# Vamos entender um parâmetro chamado ( , end='' ) e o caractere de escape ( \n' ), na função print().

print('Exemplo 01 - Formatando números reais ( float )')
d = 4 / 3
print('O resultado da divisão é {:.2f}'.format(d))
print('')

print('Exemplo 02 - Unindo frases com o parâmetro ( end )')
n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
s = n1 + n2
sb = n1 - n2
m = n1 * n2
d = n1 / n2
e = n1**n2
di = n1 // n2
r = n1 % n2
print('Soma é {}; Resto é {}; Produto é {}; Quociente é {:.2f}'.format(s, sb, m, d), end=' ')
print('Potência é {}; Divisão inteira é {}; Resto da divisão é {}'.format(e, di, r))
print('')

print('Exemplo 03 - Quebrando linhas com o caractere de escape')
print('Olá \nMundo!')
