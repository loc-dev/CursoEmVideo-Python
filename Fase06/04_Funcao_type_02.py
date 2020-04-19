# Fase 06 - Tipos Primitivos e Saída de Dados
# Teoria
# Com base na aula Fase06, vamos fazer um script
# que peça um determinado valor a ser guardado na memória
# logo, identificando o seu tipo primitivo.

# Demonstraremos, a soma entre o "valor digitador"
# e "outro valor digitado" vale "o valor x".

n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))

s = n1 + n2

print('A soma entre', n1, 'e', n2, 'vale', s)

# Método da string .format()
print('A soma entre {} e {} vale {}'.format(n1, n2, s))
