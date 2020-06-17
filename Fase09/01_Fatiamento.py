# Fase 09 - Manipulando Texto
# Teoria
# Técnica de Fatiamento

# Utilizaremos a variável 'frase' com o valor string

frase = 'Curso em Vídeo Python'

print('Utilizando a variável ( frase ) como exemplo da Técnica de Fatiamento')
print(frase)

# Se apresentamos esse exemplo ( frase[9] )
# O Python irá identificar dentro da cadeia de caracteres, somente o caracter 9

print('')
print('Identificar o caracter (9)')
print(frase[9])

# Essa outra maneira ( frase[9:13] )
# Primeiramente, o Python irá identificar dentro da cadeia de caracteres,
# o caracter 9, logo o caracter 13, porém, o caracter 13 será excluído.
# Isso significa que a sintaxe [i : f], i de início e f de final, o f será sempre f-1.

print('')
print('Identificar o caracter (9) e até o caracter (13)')
print(frase[9:13])

# Um outro exemplo ( frase[9:21] )

print('')
print('Identificar o caracter (9) e até o caracter (21)')
print(frase[9:21])

# Também temos essa maneira ( frase[9:21:2] )
# Sabemos que a sintaxe é composta por [i : f], mas, também pode ser [i : f : p]
# Significa que o p será passos, ou seja, iremos fatiar a cada n passos

print('')
print('Identificar o caracter (9) e até o caracter (21) a cada 2 caracter')
print(frase[9:21:2])

# Se colocamos ( frase[:5] )
# A sintaxe está desta forma [:f], sabendo que o f será sempre f-1.
# Mas, o início não foi especifícado, houve uma omissão
# Isso significa que irá começar desde o caracter (0)

print('')
print('Partir do início até o caracter (5)')
print(frase[:5])

# E nesse exemplo ( frase[15:] )
# Nesse caso será ao contrário, temos a sintaxe [i:], que é o início.
# Quando não é especificado o final, queremos ir até o final

print('')
print('Identificar o caracter (15) e ir até o fim')
print(frase[15:])

# Por último ( frase[9::3] )
# Esse tipo, temos a seguinte sintaxe [i::p]
# Significa que ao identificar o início temos passos e ir até o final

print('')
print('Identificar o caracter (9), cada 3 caracter e ir até o fim')
print(frase[9::3])
