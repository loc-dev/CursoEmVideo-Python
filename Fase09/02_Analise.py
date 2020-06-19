# Fase 09 - Manipulando Texto
# Teoria
# Técnica de Análise

# Utilizaremos a variável 'frase' com o valor string

frase = 'Curso em Vídeo Python'

print('Utilizando a variável ( frase ) como exemplo da Técnica de Fatiamento')
print(frase)

# Vamos apresentar o primeiro tipo de Análise
# A função len()

print('')
print('A Função len(), é para obter o comprimento de uma determinada variável:')
print(len(frase))

# O segundo tipo de Análise
# O método .count()

print('')
print('O método .count(), retornará um número de vezes que aquele valor foi especificado:')
print(frase.count('o'))

# Continuação com o método .count()

print('')
print('Uma surpresa no método .count(), é o parâmetros opcionais(start, end):')
print('O parâmetro start, é o índice inicial, onde o caractere vai iniciar a pesquisa.')
print('O parâmetro end, é o índice de finalização, onde o caractere vai terminar a pesquisa.')
print(frase.count('o', 0, 13))

# O terceiro tipo de Análise
# O método .find()

print('')
print('O método .find(), começa uma pesquisa do valor especificado, retornará o índice deste caractere:')
print(frase.find('deo'))

# Continuação com o método .find()

print('')
print('O método .find() apresenta também os parâmetros opcionais(start, end)')
print('Mas, se você declarar um valor diferente e não for encontrado, retornará o -1.')
print(frase.find('Android'))

# Por último

print('')
print('O operador in, vai analisar se determinado valor especificado se encontra na variável:')
print('Curso' in frase)
