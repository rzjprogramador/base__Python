# ADICIONA ELEMENTOS A LISTA ::EXTEND::
# Sintaxe:: lista.extend([elemento, elemento2])
lista1 = [1, 2, 3, 4, 5]
lista1.extend([6, 7, 8])
print(lista1)


# REMOVE ULTIMO ELELMENTO DA LISTA
# SINTAXE:: alvo.metodo()
lista1.pop()
print(lista1)


# SINTAXE :: split == valor.split()
# POR PADRAO SPLIT SEPARA O ESPAÇO POR VIRGULA ORIGINANDO CADA ITEM DNO ALVO
# SPLIT COM APRAM VAZIO, VAI SUBSTITUIR O ESPAÇO POR VIRGULA, ORIGINANDO ITEMS
texto = 'Um Dois'.split()
print(texto)

lista3 = ['Cinco', 'Seis']

# SUBSTITUINDO SEPARADOR POR VIRGULA E RETORNANDO ITEMS CRIADOS
texto2 = 'Tres-Quatro'.split('-')
print(texto2)
print(len(texto2))

# ADICIONANDO ELEMNETOS NOVOS FATIADOS NA LISTA com APPEND()
# lista3.append(texto2)
# print(lista3)


# MODIFICANDO OS SEPARADORES DA LISTA COM JOIN()
lista4 = ['Sete', 'Oito', 'Nove']
modifique = ' # '
lista5 = modifique.join(lista4)
print(lista5)
