# FOR == PARA -- REPETIR  UMA SEQUENCIA
sequencia1 = [1, 2, 3, 4, 5]

for valores in sequencia1:
    print(valores)

# SINTAXE :
# for <recebeValores> in <sequencia>:
# print(recebeValores)

print('-------------------------‐-----------')
# -------------------------‐-----------------------

# QUANDO QUÉR PEGAR O INDICE JUNTO USAR O ENUMERATE

for i, valores in enumerate(sequencia1):
    print(i, valores)

print('-------------------------‐-------------')
# ==========================

# Exemplo depreciado com while
nome = 'Reinaldo'

i = 0
while i < len(nome):
    print(nome[i])
    i += 1

# while == enquanto
# repete uma sequencia enquanto a condicao for true
# inicia o valor do indice interador fora
# enquanto indice for menor que o alvo
# faz algo
# scape do loop é incremento ex: indice += 1

# diferenca para o for é que o indice é iniciado fora
# e o incremento é depois da instrucao.

print('-------------------------‐---------')
