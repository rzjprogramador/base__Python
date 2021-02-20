# Atribuições variaveis:
nome = 'Reinaldo'
sobrenome = 'Zacharias'
idade = 43


# Função sep'<Define um separador a cada string>'
# Função end end='<Define o que podera ir no final das strings>'
print('Rei', 'Junior', sep='-', end='')
print('---------------------------')


# ATRIBUIÇÃO COMPACTA ::
# n += 1 :: (Faz n mais ele mesmo mais 1 )é como se fizesse n = n + 1
n = 1
n += 1
print(n)

# FORMAT COM O COMANDO PRINT com o f antes das aspas
print(f'O Sr. {nome} com o sobrenome {sobrenome} tem {idade} anos de idade ')

# ESCAPES NO TEXTO::
print(r"Vai escapar o /n que é um comando quebra-linha  com o caractere r")
print('Vai "escapar" com "aspas" simples escapa duplas e vice versa')

# PULANDO LINHAS
print()
