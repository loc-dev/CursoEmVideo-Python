# Fase 09 - Manipulando Texto
# Teoria
# Técnica de Divisão e Junção

# Utilizando o mesmo valor na técnica de Fatiamento, Análise e Transformação

frase = 'Curso em Vídeo Python'

print('Estamos novamente com a frase anterior, para compreender as novas categorias \n'
      'Divisão e Junção')
print(frase)

# Primeiramente a categoria Divisão
# Apresentando o método .split()

print('')
print('O primeiro apresentar é a categoria Divisão, temos o método .split() \n'
      'Esse método, é feito através dos espaços vazios, ocorrendo uma quebra \n'
      'na cadeia de caracteres, retornará uma Lista:')
print(frase.split())

frase = frase.split()

# De forma análoga, a categoria Junção

print('')
print('A categoria Junção, pelo nome já diz é efeito de juntar, o que fizemos com o método .split() \n'
      'vamos refazer, ou seja, unir cada elemento de uma iterável, por exemplo, a Lista, esse efeito \n'
      'será com o método .join(), se gostariamos deixar novamente o espaço em branco, ficará nesse exemplo:')
print(' '.join(frase))

# Outro exemplo com hífen

print('')
print('Nesse exemplo estou utilizando o hífen, para compreender melhor o efeito de do método .join():')
print('-'.join(frase))
