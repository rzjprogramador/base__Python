'''
# FUNCOES

 Finalidade com dados : LER ou MOSTRAR ::
..............................................................
LER ::
Lêr e processa algo, tipo soma()
Tem return e atribui a varFuncional a funcao
.............................................................
MOSTRAR ::
preciso de Parametros pra mostrar algo ou atribuir valor

# ===================================
Todos param passados pode usar dentro da funcao.

Todas variaveis passadas por param tem q dar seu valor na invocacao da funcao:
'''
def saudacao(msg, nome, frase):
	print(msg, nome, frase)

saudacao('Ola', 'Reinaldo', 'Como vai !')
saudacao('Hello', 'Renata', 'Tudo bem')


# ----------------------------------------------------------------
'''
#  RETORNO
- Quase nunca se da print dentro da funcao
- Quase sempre teremos return na funcao e a atribuiremos a uma var funcional 

# Sempre que tiver return é pra retornar para uma var o valor da funcao.
Entao pra invocar essa funcao agora tem que atribuir esta funcao a uma 
nova var que tera o valor da funcao...sera uma VAR_FUNCIONAL
 '''

def soma(x,  y):
   	return x + y
	
result =  soma(10, 10)
print(result)

# ............................

def saudacao(frase):
	return frase.upper()
	
funcional = saudacao( 'Ola')
print(funcional)

# ----------------------------------------------------------
 '''
 FUNÇÃO LAMBDA == FUNCAO ANONIMA 

# Funcao lambdaé uma funcao anonima com a clausula lambda
# Retorna a uma var a sua execucao
# ao inves de criar uma funcao nomeada e atribui-la a uma var a lamba faz o 
# mesmo sem a palavra return , parenteses nos params e sem nome da funcao.

# Substitui o modo de implementacao das  funcoes tradicionais.

 '''
var = lambda x,  y:  x + y
print(var(2, 2))

# ----------------------------------------------------------------
 '''
# PARAMETROS :

- Na receita sao copos /variaveis vazios
- Vc recebe pra adicionar valor e 
- Atribui valor na invocacao

É o que vc tem de pegar 
_ Pra mim pegar isso , preciso disso e disso
# exemplo:
pegarEmail(PRECISO DE : email, senha)
buscarUsuario(PRECISO DE : id, nome)
.................
ARGUMENTOS == Sao valores para os parâmetros passados na função. 

 '''

# ----------------------------------------------------------------
 '''
ASSINCRONO
Assincrono : Nao depende de vc 
CALLBACK : Te avisa quando ta pronto a promessa.

 '''
 # ----------------------------------------------------------------

