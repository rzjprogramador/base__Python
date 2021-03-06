# Sets Conjunto coleção de lementos dentro de uma estrutura de dados
# Só suporta elementos unicos
# Não pode criar um set vazio com chaves só com set()
# Só recebe valores ..nao tem chave e valor ..nao tem indice ,
# nao acessa por indice
# Só suporta elementos IMUTAVEIS

s1 = set()
# Elementos
# Adicionar com add() / Remover com discard() //
# Editar ou adicionar novos com update()
# SET noa aceita elem. duplicados ele exclui limpa os duplicados

s1.add(1)
s1.add(2)
s1.add(3)

s1.discard(2)

s1.update({1, 2, 3, 4, 5}, {5, 6, 7, 8})


print(s1)

# ===============================

l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 'Reinaldo', 'Reinaldo']
# Casting - Transformar a lista em set   >> <lista> = set(<lista>)

# Fez o Casting , trnsformou e nao tem mais duṕlicados no set novo
l1 = set(l1)
print(l1)

# Casting - Voltar a ser uma lista sem os duplicados >> <set> = list(<set>)
# Elementos podem voltar fora de ordem
l1 = list(l1)
print(l1)

# =====================================================
# FUNÇÕES PARA SETS
# utilizando esses 2 sets para todos exemplos abaixo
s11 = {1, 2, 3, 4, 5, 7}
s22 = {1, 2, 3, 4, 5, 6}

# union com pippeline | >> une os sets
s3 = s11 | s22
print(s3)


# intersection == entre seções USA O " & ">>
# Retorna todos elem. presentes nos 2 sets -- elimina qual nao esta presente no outro
s4 = s11 & s22
print(s4)


# Diference -- << USA SINAL DE MENOS - >> neste a ordem importa
# Vc pega somente o elemento que esta no set da esquerda da instrucao e nao esta na direita
s5 = s11 - s22
print(s5)


# Symmetric diference == Diferença simetrica >> USA O ^ "SINAL DE TIO"
# Só pega elem. que estao num set e noa estao no outro
# Resumindo pega os que nao estao nos 2 sets --NÃO TEM ORDEM
s6 = s11 ^ s22
print(s6)
