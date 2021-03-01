# variavel = 'valor global' ### boas praticas :: evitar
# Não usar variavel global
# nao tentar acessar variavel global dentro de funções


def func():
    variavel2 = 'Reinaldo'
    return variavel2


def func2(arg):
    print(arg)


var_funcional = func()
func2(var_funcional)


'''
Na primeira func para deixar acessivel suas variaveis  
foi dado return na sua variavel que carrega um valor

Foi criada a func2 passando argumentos e 
dizendo que desse parametro quer que seja feito um print

a primeira funcao com o valor e return foi atribuida a var_funcional
agora Chamamos a func2 com a var funcional como valor variavel, porque agopra ela carrega o valor

RESUMO : Na segunda função exibimos o valor da primeira função
'''

# MAIS EXEMPLO : Na segunda função exibindo o valor da primeira função


def valores():
    valor1 = 'Meu valor 1'
    return valor1


def recebeFunc(param_valor1):
    print(param_valor1)


var_funcional2 = valores()
recebeFunc(var_funcional2)
