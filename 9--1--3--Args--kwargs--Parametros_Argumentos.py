def func(a1, a2, a3, a4, nome=None, outro=None):
    print(a1, a2, a3, a4, nome, outro)


func(1, 2, 3, 4, nome='Rei', outro='Outro')


'''
Posso ter parametros nomeados, os nomeados tem que ser por ultimo
tem que passar a chave do nomeado ao dar valor opcional na invocação

Neste momento a funcao nao reorna nada reorna None
para retornar algo tem que colocar return nela e atribuir a uma var 
assim a função e a var funcional tera valor


'''


def func(a1, a2, a3, a4, nome=None, outro=None):
    print(a1, a2, a3, a4, nome, outro)
    # Posso retornar só os argumentos que quiser
    return nome, outro


var1 = func(1, 2, 3, 4, nome='Rei', outro='Outro')

# Acessar os valores da var1 [posicao] -- posso acessar as posicoes que tiver
print(var1[0], var1[1])
# Retornará uma tupla  com 2 valores


'''
*ARGS == (ILIMITADOS ARGUMENTOS SEM VALUE) -- NA EXECUÇÃO RESULTA = TUPLAS
**KWARGS (ILIMITADOS ARGS NOMEADOS COM VALUE)- NA EXECUÇÃO RESULTA = DICIONARIO

'''


'''
*args == ARGUMENTOS ILIMITADOS
QUANDO NÃO SABEMOS QUANTOS ARGUMENTOS TEREMOS
com o * ASTERISTICO VC FAZ UM EMPACOTAMENTO --GURDA UM ILIMITADO


'''


def func3(*args):
    print(args)       # mostra toda tupla
    print(args[0])    # mostra primeira posicao do valor da tupla
    print(args[-1])   # mostra ultima posição do valor da tupla
    print(len(args))  # mostra o tamanho da tupla


func3(1, 2, 3, 4, 5)  # Tupla que esta sendo referenciada na func3


'''
**kwargs -- nome usado por convenção pode ser outro
**kwargs -- = podemos passar ILimitados argumentos nomeados por param
na invocação ele resulta em um Divionario Hash/Objeto 
com os valores dos argumentos nomeados
'''


def func4(*args, **kwargs):
    print(args)
    print(kwargs)

    # idade nao existe nos meus args, entao tratar a busca pra nao dar erro
    idade = kwargs.get('idade')

    if idade is not None:
        print(idade)
    else:
        print('Idade não existe.')
    # Se quiser omitir o None só retirar o else


lista1 = [1, 2, 3]
lista2 = [10, 20, 30]


func4(*lista1, *lista2, nome='Reinaldo', sobrenome='Zacharias')
