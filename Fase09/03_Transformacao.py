# Fase 09 - Manipulando Texto
# Teoria
# Técnica de Transformação

# Utilizaremos a variável 'frase' com o valor string

frase = 'Curso em Vídeo Python'

print('Utilizando a variável ( frase ) como exemplo da Técnica de Fatiamento')
print(frase)

# Por via de regra uma cadeia de caracteres é imutável
# Mas, podemos alterar através dos métodos

# O primeiro método é o .replace()

print('')
print('O método .replace() irá substituir valor especificada, por um novo valor')
print('Sua sintaxe ocorre da seguinte forma .replace(antigo, novo):')
print(frase.replace('Python','Android'))

# O segundo método é o .upper()

print('')
print('O método .upper(), retornará uma sequência em que todos os caracteres estão em maiúsculas:')
print(frase.upper())

# O terceiro método é o .lower()

print('')
print('O método .lower(), retornará uma sequência em que todos os caracteres estão em minúsculos:')
print(frase.lower())

# O quarto método é o .capitalize()

print('')
print('O método .capitalize(), irá converter o primeiro caractere em letra maiúscula \n'
      'e todos outros irão ser caracteres em letras minúsculas:')
print(frase.capitalize())

# O quinto método é o title()

print('')
print('O método .title(), é uma pesquisa profunda de quantas palavras tem na cadeia de caracteres. \n'
      'Transformando somente o primeiro caractere das palavras em maiúsculo')
print(frase.title())
