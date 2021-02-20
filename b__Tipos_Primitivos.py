# TIPO DE DADOS PRIMITIVOS
# str   --- string  ---  exemplos: 'Assim' == "Assim"
# int   --- inteiro ---  exemplos: 43 10 -10 0 2021
# float --- real/decimal exemplos: 4.3 -4.3 0.30
# boll  --- booleano     exemplos: True / False


# PERGUNTAR O TIPO COM TYPE()
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
