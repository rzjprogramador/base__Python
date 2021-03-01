

lista = [1, 2, 3, 4]
# Desempacotando lista com *
print(*lista)
# Mudando o separador do desempacotamento da lista
print(*lista, sep='-')


# Desempacotamento de listas e atribuindo a variaveis
lista2 = ['Reinaldo', 'Gustavo', 'Leonardo', 1, 2, 3, 4, 5]

n1, n2, n3, *demais = lista2

print(n1, n2, n3, demais)
