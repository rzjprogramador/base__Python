'''
CONDICIONAL TERNARIA PYTHON

'''

avaliado = True

msg = 'Msg se avaliado true' if avaliado else 'Msg se avaliado Falso'
print(msg)

# ...........................
# Exemplo 2:

idade = 18
es_maior = (idade >= 18)

msg = 'Msg se avaliado true' if es_maior else 'Msg se avaliado Falso'
print(msg)

# ------‐---------------------------------------------------------



# Escopo ::: Escopo começa em 2 ponto : e termina na ultima linha vazia.

# Identação super importante pra rodar o codigo
# if == Se
# elif == senao se (Posso repetir quanto quiser esta opção )
# else == senão >>> ultima opção do if

'''

# CONDICIONAIS

Quando usar o bloco elif ?
R: Quando preciso verificar outras condições .

O bloco elif é usado quando se faz necessário checar outras condições 
ou variações da mesma condição. O bloco elif depende do bloco if, ou seja, 
é necessário primeiro usar o bloco if e somente se a expressão do
bloco if for falsa, o bloco elif será verificado.

-------------------------------------
Quando utilizar o bloco else:
R: Quando preciso de um valor padrao ou resposta contraria a condição

O bloco else só é executado quando nenhuma condição 
de if ou elif for verdadeira. 
Por isso, quando precisamos de um valor padrão 
ou de uma resposta contrária à condição, 
é necessário adicionar o bloco else.

-------------------------------------


'''
