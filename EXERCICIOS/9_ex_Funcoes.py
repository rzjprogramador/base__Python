'''
1- Crie uma função que recebe uma funcao que exibe uma saudação
com os parametros saudacao e nome
'''


def saudacao(saudacao, nome):
    print(f'{saudacao} {nome}')


saudacao('Olá', 'Reinaldo')
saudacao('Oi', 'Gustavo')
saudacao('Hey', 'Leonardo')


'''
2- Crie uma função que recebe 3 numeros como parametros
e exiba a soma entre eles.
'''


def soma(n1, n2, n3):
    print(n1 + n2 + n3)


soma(2, 4, 4)


'''
3- Crie uma função que recebe 2 numeros
O primeiro é um valor e o segundo um percentual (ex. 10%)
Retorne (return) o valor do primeiro numero somado
do aumento do percentual do mesmo
'''

# ENTRADAS
valor_enviado = 50
percentual_desejado = 20


def aumento_percentual(valor, percentual):
    return valor + (valor * percentual / 100)


ap = aumento_percentual(valor_enviado, percentual_desejado)
print(ap)

# OUTRAS INVOCAÇÕES -- valor e quanto deseja acrescentar de porcentagem
ap = aumento_percentual(80, 100)
print(ap)

'''
3- Fizz Buzz - Se o aprametro da funcao dor divisivel por 3 :retorne Fizz
Se o parametro da funcao for divisivel por 5 , retorne Buzz
Se o parametro da função for divisivel por 5 e 3 retorne FizzBuzz
Caso contrario retorne o numero invalido !
'''


def fb(num):
    if not num % 3 == 0 and not num % 5 == 0:
        return f'O Numero {num} é Invalido - Não é divisivel por 3 e nem 5'
    if num % 3 == 0 and num % 5 == 0:
        return f'FIZZBUZZ, o Enviado {num} é Divisivel por 3 e 5'
    if num % 5 == 0:
        return f'BUZZ, o Enviado {num} é Divisivel por 5'
    if num % 3 == 0:
        return f'FIZZ , o Enviado  o Enviado{num} é Divisivel por 3'


print(fb(7))
print(fb(10))
print(fb(15))
print(fb(22))

# 7 , 22 nao são divisiveis nem por 3 nem por 5


'''
4- Crie uma função que recebe uma funcao2 como parametro 
e retorna o valor da funcao2 executada
'''
