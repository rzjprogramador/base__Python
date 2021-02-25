# -----  FORMATAÇÃO DE VALORES -------------------------------------
'''
:s -- Textos (strings)
:d -- Inteiros(int)  -- d de digito
:f -- Numeros de Ponto Flutuante - Decimais(float)
:.<Numero de Casas Decimais>(float) exemplo: :.2f >> São 2 casas decimais
:<Caractere> (> ou < ou ^) (Quantidade)(Tipo - s, d, ou f)
> -- Esquerda
< -- Direita
^ -- Centro

'''
# -----  :.<Casas>f  -- para float --------------------------------
num1 = 10
num2 = 3
divisao = num1 / num2
print('{:.2f}'.format(divisao))
# OU COM F-STRINGS
print(f'Com F-String mostra resultado {divisao:.2f}')


# -----  :s  -- para string -- pode ser só explicitar que é string----
nome = 'Reinaldo'
print(f'Meu nome é {nome:s} ')
