'''
Dictionary Comprehension == Compreensão de Dicionario
A diferença para list comprehension ao inves de usar [] usa {} com chave:valor

'''

# Criando uma compreensao para chave e valor numa lista
lista = [
    ('chave1', 'valor1'),
    ('chave2', 'valor2'),
    #('chave3', 3),
]

d1 = {x: y for x, y in lista}
print(d1)

# Posso fazer operações -- vai duplicar string ou numero
d2 = {x: y * 2 for x, y in lista}
print(d2)

# Mais operações e modificações deixar Maiusculo
d3 = {x.upper(): y.upper() for x, y in lista}
print(d3)

# Criando um dicionario com indice nas chaves e os valores elevado a 2
d4 = {f'chave_{x}': x**2 for x in range(5)}
print(d4)
