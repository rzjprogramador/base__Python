'''
LIST COMPREHENSION == COMPREENSÃO DE LISTA
Forma otimizada de fazer uma interação varrer
e aplicar modificações na lista

# SINTAXE: 
# [<Operacao> for interar var da operacao in listaAlvo]
# exemplo : [v.replace('a', '@') for v in l2]
# + exemplo : [v * 2 for v in l1]

'''
l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Multiplicar por 2 os elementos da lista
ex1 = [v * 2 for v in l1]
print(ex1)

# CRIAR UMA TUPLA COORDENADA PARA CADA ELEMNTO COLOCAR O INDICE NOS VALORES DE 1 A 3
# Um laço interando sobre outro laço
# O primeiro vai definir indice e valor
# O segundo vai criar uma sequencia de 1, 2, 3 com o range
# ficando assim indice de 0 a 3 em cada valor
ex3 = [(v, v2) for v in l1 for v2 in range(3)]
print(ex3)


# TROCAR O a POR @  E EM MAIUSCULO NA LISTA DE STRINGS
l2 = ['Renata', 'Thayna', 'Dayanne', 'Dara']
ex4 = [v.replace('a', '@').upper() for v in l2]
print(ex4)

# Inverter onde é chave pra valor e onde é valor pra chave na tupla
tupla = (
    ('chave', 'valor'),
    ('chave2', 'valor2'),
)
# Mostrar normal
ex5 = [(x, y) for x, y in tupla]
print(ex5)

# Mostrar invertido de chave e valor para valor e chave
# mudando só a ordem dos args
ex5 = [(y, x) for x, y in tupla]
print(ex5)

# FAZENDO UM CASTING DE TUPLA PARA DICIONARIO COM dict(<tuplaAlvo>)
ex5 = dict(ex5)

# Acessando valor 2 invertido do agora dicionario
print(ex5['valor2'])
