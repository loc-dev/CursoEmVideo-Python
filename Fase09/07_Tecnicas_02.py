# Fase 09 - Manipulando Texto
# Teoria
# Colocando em prática as técnicas

# Parte 02

# Combinação das técnicas

frase = 'Curso em Vídeo Python'
print("Tudo no Python é objeto")
print("Técnica de Análise - .count()")
print('Está será a frase de exemplo: ', frase)
print('Resultado de quantas letras (o):')
print(frase.count('o'))

print('')
print("Técnicas de Transformação e análise - .upper() e .count()")
print('Resultado de quantas letras (O):')
print(frase.upper().count('O'))

print('')
print("Técnica de Análise - len()")
print('Resultado do comprimento da variável (frase):')
print(len(frase))

# Outro exemplo - len()
print('')
frase = '   Curso em Vídeo Python   '
print('Está será a frase de exemplo: ', frase)
print('Resultado do comprimento da variável (frase):')
print(len(frase))

print('')
print("Técnica de Transformação - replace()")
frase = 'Curso em Vídeo Python'
print('Está será a frase de exemplo: ', frase)
print('Resultado da substituição da palavra Python para Android:')
print(frase.replace('Python', 'Android'))

print('')
print('Mas, essa frase não está definitiva, vejamos:')
print(frase)

print('')
print('Então, vamos fazer uma atribuição:')
frase = frase.replace('Python', 'Android')
print(frase)

print('')
print('Técnica de Análise - operador in')
frase = 'Curso em Vídeo Python'
print('Está será a frase de exemplo: ', frase)
print('Resultado da pesquisa do valor especificado no caso (Curso), retornará uma valor lógico:')
print('Curso' in frase)

print('')
print('Técnica de Análise - .find()')
print('Resultado da pesquisa do valor especificado no caso (Curso), retornará o índice do caractere (C):')
print(frase.find('Curso'))

print('')
print('Técnica de Divisão - .split()')
print('Resultado de uma técnica de divisão entre os mini espaços vazios, retornará uma Lista:')
print(frase.split())

print('')
print('Obtendo um item da Lista, com a técnica de Divisão')
dividido = frase.split()
print(dividido[2][3])
