# ACESSOS FATIADOS EM SEQUENCIAS
nome = 'Reinaldo'
lista = ['Guga1', 'Leo2', 'Victor3', 'Renata4', 'Mara5', 'Dayane6', ]

# função len ::tamanho da sequencia :: sintaxe : len(variavel)
print(f'O nome {nome} tem {len(nome)} caracteres')

# tamanho da lista
print(len(lista))


# alvo[indice]
print(nome[0])
print(lista[0])

# indice -1 == pega o ultimo elemento do alvo
print(nome[-1])
print(lista[-1])

# indice -2 == pega o penultimo elemento do alvo
print(nome[-2])
print(lista[-2])

# Pegar do indice 0 ao indice 6 ex: var[0:6]
nova_string = nome[0:6]
print(nova_string)

# Pegar do indice 3 ao final ..Só colocar nada depois do : >> ex: var[3:]
nova_string = nome[3:]
print(nova_string)

# Ir pulando de quantos vai PULAR ex: [COMEÇO:ATÉONDE:PULOS]
# exemplo ir do 0 ao 8 ,pulando de 2 em 2
# exemplo em string
nova_string = nome[0:8:2]
print(nova_string)

# exemplo em lista
nova_sequencia = lista[0:6:2]
print(nova_sequencia)

# [COMEÇO::PULOS] --Sem nada no meio vai do inicio ao fim no passo definido por ultimo
# exemplo do começo ao fim pulando de 3 em 3
nova_lista = lista[0::3]
print(nova_lista)

# Sem colocar nada a direita ou esquerda pega inteiro sem mudar nada
nova_inteira = lista[:]
print(nova_inteira)


# Dar um for in ... para manipular elemento por elemento
for elementos in lista:
    print(elementos)
    # posso pegar elementos e manipula-los

# Pegar letra por letra da string

for letra in nome:
    print(letra)
    # posso pegar as letras e manipula-las