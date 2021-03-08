# OPERADORES LOGICOS

# True == Verdadeiro    # False == Falso

# ---------------------------------------------------------------------------
a = 3
b = 2
c = 5

# ---------------------------------------------------------------------------
# not == INVERSOR - INVERTE VALOR ::: Só precisa de uma expressao nao de duas
# SINTAXE:: comando not (<expressao a ser Invertida> )
if not a > b:
    print(f'"a" que vale {a} é maior que "b" que vale {b} ')
else:
    print(f'No NOT "b" que vale {b} é maior que "a" que vale {a} ')

# Usando not com variavel vazia ou zerada
e = ''
f = 0

# se " var e" não tem um valor faça:
if not e:
    print('Preencha o valor de "e" ')

# ---------------------------------------------------------------------------
# or == OU -- Para retornar False todos operandos tem que ser False

# and == E -- Para retornar False basta um dos operando ser False

# ==   Igual

# != diferente ::: ex: 6 != 7 resposta : True

# n =6
# 1 < n and n < 5  ::: retorna False
# Esta expressao pode melhorar a legibilidade assim :
# Expressando um Intervalo :; exemplo:
# 1 < n < 5  <<Um menor que n(6) e menor que 5 ::: continuará retornar False
