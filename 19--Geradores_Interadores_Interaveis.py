import sys
import time

# Para saber se é um objeto interavel
# hasattr(<objeto>, '__iter__')  -->> retorna um boleano
lista = [0, 1, 2, 3, 4, 5]
print(hasattr(lista, '__iter__'))

string = 'Palavras'
print(hasattr(string, '__iter__'))

# Numeros nao sao iteraveis
numeros = 1234
print(hasattr(numeros, '__iter__'))

# SE É UM ITERAVEL PODEMOS USAR O FOR PARA EXIBIR A LISTA LINHA A LINHA
# o FOR TRANSFORMA NOSSA SEQUENCIA EM UM INTERADOR
# PARA EXIBIR LINHA A LINHA SEU VALOR

# ============================
# PARA SABER SE É UM ITERADOR USAR O METODO '__next__'
# A lista nao é um iterador o for a transforma em iterador usando o iter()
lista = iter(lista)
print(hasattr(lista, '__next__'))
# agora a lista é um iterador com o metodo iter(<lista>)

# cada vez que executar o next na lista vc vai ver o q o for faz , cada valor de uam vez
print(next(lista))
print(next(lista))
print(next(lista))

'''
A diferença de um iteravel e um interador 
é que o Iteravel é um obj que podemso iterar sobre ele
não vai dar um valor de cada vez

E um interador vai dar um valor de cada vez

'''

'''
GERADORES :
Para gerar valores que consomem menas memoria

'''
# Com o metodo getsizeof(<obj>) pegamso quantos bytes ta usando o obj
lista = list(range(10))
print(sys.getsizeof(lista))
# esta esta consumindo 136 bytes

# Aumentando os bytes conforme tamanho da lista
lista2 = list(range(1000))
print(sys.getsizeof(lista2))

'''
VAMOS UTILIZAR OS GERADORES PARA NAO ABRIR TODOS VALORES 
DE UMA VEZ SOMENTE O NECESSARIO - UM VALOR DE CADA VEZ
SEM ESPERAR TODOS VALORES DE UMA VEZ
OTIMO PARA OPERAÇÕES PESADAS
'''

# Simular uma função geradora com yield ==> rendimento


def gera():
    for n in range(10):
        yield n
        time.sleep(0.1)


g = gera()

for v in g:
    print(v)

# UTILIZAR A CADA CHAMADA UM VALOR NA ORDEM COM NEXT E YIELD
# PROXIMO RENDIMENTO -- NA SEQUENCIA


def gera2():
    variavel = 'valor1'
    yield variavel
    variavel = 'valor2'
    yield variavel
    variavel = 'valor3'
    yield variavel


g2 = gera2()

print(next(g2))
print(next(g2))
print(next(g2))
# Como nao tem mais valores pra mostrar o Python vai dar erro
# StopIteration
# A melhor maneira pe usar com for essa interação ...
# Só pra caso especifico usar uma funcao geradora yield com next()

'''
TRANSFORMAR UMA LISTA EM GERADOR
PARA DIMINUIR O CONSUMO DE MEMORIA

'''
l1_grande = [x for x in range(1000)]
l2_grande = (x for x in range(1000))

# 2 listas iguais -- 
# mais a segunda criada com () é a geradora 
# Que vai consumir menos memoria
print(sys.getsizeof(l1_grande))
print(sys.getsizeof(l2_grande))

# Os geradores nao vai salvar todos dados na memoria
# Só vai te entregar o valor quando vc pedir com next ou com for
for v in l2_grande:
    print(v)
    
# O SEGREDO DA CRIAÇÃO DE GERADORES QUE BAIXAM CONSUMO É :
# Ao criar a list Comprehension trocar o [] por ()
