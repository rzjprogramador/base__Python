# Atribuições variaveis:

nome = 'Reinaldo'
sobrenome = 'Zacharias'
idade = 43
altura = 1.80
e_maior = idade > 18
peso = 80
imc = peso / (altura ** 2)

print(f'{nome} tem {idade} anos e seu imc é {imc:.2f} ')


# print formatado com variaveis
# print(f'{varivel} textos ')


# 2 casas decimais
# {variavel:.2f}


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
# PRINT : PULAR LINHAS COM 3 ASPAS ANTES E DEPOIS DO TEXTO
print(""" 
Quero pular
essa linha
e essa também 
""")

# STRING MULTIPLICADA
texto2 = 'a'
print(texto2 * 4)

texto3 = 'Ipsum Lorem '
print(texto3 * 5)

