# -----  TIPO DE DADOS PRIMITIVOS  ----------------------------------------

# int   -- inteiro ---  VALORES_INICIAIS:  0    -  exemplos: 43 10 -10 0 2021
# str   -- string  ---  VALORES_INICIAIS:  ''   -  exemplos: 'Assim' ou "Assim"
# float -- real/decimal VALORES_INICIAIS:  0.0  -  exemplos: 4.3 -4.3 0.30
# boll  -- booleano     VALORES_INICIAIS:  True -  exemplos: True / False

# VALORES INICIAIS NUMERICOS
# 0 = False
# 1 = True


# -----  PERGUNTAR O TIPO COM TYPE()  -------------------------------------

# type(<o que deseja saber o tipo>)
print('Reinaldo', type('Reinaldo'))
print(2021, type(2021))
print(23.23, type(23.23))
print(1_000_000, type(1_000_000))
print('l' == 'L', type('l' == 'L'))


# TYPE CASTING -- FUNDIR -- CONVERTER TIPO POR OUTRO TIPO
# SÓ CHAMAR O TIPO DESEJADO NA FRENTE DO TIPO NÃO MAIS DESEJADO
# convertendo string para inteiro e mostrando o tipo novo
print('10', type(int('10')))

# sintaxe conversões :: str() int() float() bool()
print('Era inteiro agora é : ', type(str(10)))
print('Era uma string agora é : ', type(int('10')))
print('Era um inteiro agora é : ', type(float(90)))
print('Era um inteiro agora é : ', type(bool(0)))


# ============ ORDENS ============

# Ordem Prescedencia  Expressões ::
# 1º -- () -- tudo que esta dentro dos parenteses
# 2º -- ** -- exponenciação
# 3º -- *  -- multiplicação
# 4º -- /  -- divisão
# Penultimo :: + soma
# Ultimo ::   - subtração


# -----  NUMERICOS  -------------------------------------

# ============ INTEIRO ============

# modulo resto da divisão :: 5 % 2 resposta 1
# (Porque 5 divide por 2 da 2 -- e sobra 1 --esta sobra é o resto da divisão)


# divisao float  :: 5 / 2 :: resposta 2.5


# divisão inteira sem sobra :: 5 // 2  :: resposta 2


# exponenciação :: 2 ** 3  (2 elevado a 3) :: resposta 8


# Numeros legiveis :casas decimais separadas por underscore _ anderline
# Um milhão == 1_000_000


# ===================================================


# ============ FLOAT -- NUMEROS DECIMAIS ============

# Converter inteiro em float :: int(<NumeroFloat)  -- ex: int(1.5)


# Converter float em inteiro :: float(<NumeroInteiro>) -- ex: float(1)
