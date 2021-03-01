'''
DICIONARIO == HASH / OBJETO em outras linguagens
dicionario = {'chave': 'valor'}

'''
# Criar Dicionario
d1 = {'chave0': 'valor0', 'chave1': 'valor1', 'chave2': 'valor2'}

# Criar dicionario com dict() -- obs: nao usar espaços
d2 = dict(chave3='Valor chave3', chave4='Valor chave 4')
print(d2)

# Nome da chave tem que ser unico
# se tiver mais com mesmo nome a ultima tera o valor real da chave
d4 = {
    'chave4': 'vale1',
    'chave4': 'vale22',
    'chave4': 'Ultimo este sim, tem o valor real da chave4'
}
print(d4)

# Adicionar nova chave
d1['nova_chave'] = 'valor_nova-chave'
print(d1)

# Adicionando nova chave com metodo dicionario.update({'nova_chave': 'novo-valor'})
d1.update({'nova_chave': 'novo_valor'})

# Deletar chave e valor com del dicionario['chave']
del d1['chave2']
print(d1)

# Acessar valor da chave -- dicionario['nome_chave']
print(d1['chave0'])
# Acessar com dicionario.get()
print(d1.get('chave1'))

# No conteudo do Dicionario posso usar qualquer tipo de dado Imutavel
# Como chave somente dados que nao mudam
# Para acessa-los usa-se esta mesma chave
d5 = {
    'str': 'valor',
    123: 'Outro valor',
    (100, 200, 300): 'Valores da tupla'
}
print(d5[(100, 200, 300)])
print(d5[123])
print(d5['str'])


# Checar se a chave existe no dicionario
print('chave1' in d1)  # retorna um booleano
print('chave1' in d1.keys())  # mesma coisa pra checar chave acima

# Checar se existe um valor com dicionario.values()
print('valor0' in d1.values())  # retorna um booleano

# Contar com a função len , quantos pares temos no dicionario
print(len(d1))

# Interar percorrer o dicionario com for
# Só o nome do dicionario retornará só as chaves
for k in d1:
    print(k)

# Interar sobre os valores com .values()
for v in d1.values():
    print(v)

# Interar sobre chave e valor com dicionario.items()
# retornará um tupla com as chaves e valores
for chave_valor in d1.items():
    print(chave_valor)
    print(chave_valor[0], chave_valor[1])  # Acessar separado por indice

# Outra forma de interar chave e valor sem indice 
# passando 2 argumentos
for k, v in d1.items():
    print(k, v)


# Interando em dicionarios dentro de Dicionarios
clientes = {
    'cliente1' : {
        'nome': 'Reinaldo',
        'sobrenome': 'Zacharias',
    },
    'cliente2' : {
        'nome': 'Gustavo',
        'sobrenome': 'Eduardo',
    },

}

# interando sobre as chaves do dicionario Filho dentro do Pai
for clientes_k, clientes_v in clientes.items():
    print(f'Exibindo {clientes_k}')
    
    # interacao sobre os valores do dicionario Filho dentro do Pai
    for dados_k, dados_v in clientes_v.items():
        print(f'\t {dados_k} = {dados_v}')
    

# Para criar uma copia de um dicionario usar varNova = dicionario.copy
# Bom usa ro copy() para no caso de fazer alterações ela é feita só no desejado
# è uma copia raza de referencia , para copia real só com modulo copy, deepcopy
copiado = d1.copy()
print(f' Este é o dic copiado : {copiado}')

