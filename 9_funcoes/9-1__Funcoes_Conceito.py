'''
FUNCOES
Finalidade com dados : LER ou MOSTRAR ::
..............................................................
LER ::
Lêr e processa tratar dados
Dentro da funcao tratar os dados e retornar um valor (Nao se dá print)
.............................................................
MOSTRAR ::
preciso de Parametros pra mostrar algo ou atribuir valor
..............................................................
NO CORPO DA FUNÇÃO : Todos parametros passados podem ser usados
NA INVOCAÇÃO : Tem que preencher os valores dos parametros passados na funcao

'''

# FUNÇÃO SIMPLES :


def saudacao(msg, nome, frase):
    return f'{msg} {nome} {frase}'


ola = saudacao('Ola', 'Reinaldo', 'Como vai !')
print(ola)
ola2 = saudacao('Hello', 'Renata', 'Tudo bem')
print(ola2)


# FUNÇÃO REDUZIDA -- TIPO LAMBDA
# Reduzindo a mesma função para a expressao lambda ou Reduzida
def var_funcional(msg, nome, frase): return f'{msg} {nome} {frase}'


print(var_funcional('Minha MSG-3', 'Meu Nome-3', 'Minha frase-3'))


'''
FUNÇÃO LAMBDA == FUNCAO ANONIMA 

- Funcao lambda é uma funcao anonima com a clausula lambda
- Retorna a uma var a sua execucao
- ao inves de criar uma funcao nomeada e atribui-la a uma var a lamba faz o 
- mesmo sem a palavra return , parenteses nos params e sem nome da funcao.

# Substitui o modo de implementacao das  funcoes tradicionais.


- Sintaxe: Lambda ::
- var_funcional = lambda param1, param2, param3: o que quer fazer com params
- Invocação : var_funcional('valor dos Parametros passados')

- O Interpretador do Python está mudando a lambda para def função reduzida
do not assign a lambda expression, use a def ==
 não atribua uma expressão lambda, use um def


Mudando de LAMBDA PARA FUNCAO REDUZIDA : INTERPRETADOR PY ::
var_funcional = lambda msg, nome, frase: f'{msg} {nome} {frase}'
### para : ###
def var_funcional(param1,param2, param3): return fazer ALGO e usar os params

'''


def var(x,  y): return x + y


print(var(2, 2))


'''
RETORNO
- em Python se a funcao nao encontrar um return ela retorna None
- Quase sempre teremos return na funcao e a atribuiremos a uma var funcional 

Sempre que tiver return é pra retornar para uma var o valor da funcao.
Entao pra invocar essa funcao agora tem que atribuir esta funcao a uma 
nova var que tera o valor da funcao...sera uma VAR_FUNCIONAL
 '''

# Passando Função para dentrod e Função e atribuindo a var


def f(var):
    print(var)


def dumb():
    return f


var2 = dumb()
print(var2('E colocar o valor da funcao f - aqui'))


'''
   # PARAMETROS :

   - Na receita sao copos /variaveis vazios
   - Vc recebe pra adicionar valor e 
   - Atribui valor na invocacao

   - É o que vc tem de pegar 
      _ Pra mim pegar isso , preciso disso e disso
   - exemplo:
   pegarEmail(PRECISO DE : email, senha)
   buscarUsuario(PRECISO DE : id, nome)
  
    '''
