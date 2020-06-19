# Fase 09 - Manipulando Texto
# Teoria
# Técnica de Transformação

# Iremos alterar o valor da variável 'frase'

frase = '   Aprenda Python  '

print('É comum na área de tecnologia, pessoas incluir espaços na caixa de texto')
print(frase)

# As linguagens de Programação apresenta funcionalidades internas para remoção desses espaços
# Vejamos o método .strip()

print('')
print('O método .strip() pode ajudar no momento de remover todos os caracteres \n'
      'iniciais e finais:')
print(frase.strip())

# Continuação com o método .strip()

print('')
print('O método .rstrip() pode fazer a mesma ajuda, porém, remove somente os caracteres da direita:')
print(frase.rstrip())

print('')
print('De forma análoga, não podemos esquecer o left (esquerda) \n'
      'O método .lstrip(), remove todos os caracteres da esquerda:')
print(frase.lstrip())
