'''
TUPLAS == LISTAS IMUTAVEIS EM PYTHON
Tuplas vc Não pode adicionar, remover e editar seus elementos
Não pode mudar o valor do indice

Caso de Uso : Caso tvc tenha uma lista que nao queira que o valor 
dela seja alterado acidentalmente por segurança converter em tupla

Um Objeto que seja só pra leitura fazer em tupla


'''
# Criar uma tupla basta colocar ()
# Para adicionar elementos tem que ser na sua criação
t1 = (1, 2, 3, 'a', 'Rei')
print(type(t1))

# Pode ser criada sem os parenteses tambem
t2 = 10, 20, 30, 'Gustavo', 'Leonardo'
print(t2)

# Criar sem aprenteses com apenas 1 elemento colocar a virgula no fim
t3 = 100,
print(t3)

# Para acessar elementos , acessar pelo indice tuple[indice]
print(t1[4])

# Interar percorrer a tuple  usar o for
# A cada interação da tupla vc vai ver por linha cada elemento dela
for elementos in t1:
    print(elementos)

# Fatiar tupla -- da posicao 2 ate o ultimo elemento
print(t1[2:])

# Concatenar tuplas -- criar uma nova tupla = tupla1 + tupla2 + ....
t4 = t1 + t2 + t3
print(t4)

# Desempacotar em variaveis -- recebe1, recebe2... *recebeRestante = tuplaAlvo
n1, n2, n3, *_ = t1
print(n3)
print(_)  # pegou os ultimos e guardou em lista


# Multiplicar Tuplas - Criará nova tupla com conteudo multiplicado dentro de dessa nova
t6 = (1000, 2000, 3000) * 5
print(t6)

# Converter tupla em lista -- Para poder edita-la:
# tupla = list(tupla)
t1 = list(t1)
print(t1)

t1[1] = 'Cem'   # editando
print(t1)

# Converter  a lista para tupla -- lista = tuple(lista)
t1 = tuple(t1)
print(t1)
