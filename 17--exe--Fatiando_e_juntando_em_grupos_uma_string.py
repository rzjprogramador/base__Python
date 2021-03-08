'''
Pegar strings unidas e retornar grupos separados de strings

Ex a fazer:
string = '01234567890123456789012345678901234567890123456789'
lista = ['0123456789', '0123456789', '0123456789', '0123456789',]
retorno = '0123456789.0123456789.0123456789.0123456789.'

'''
string = '01234567890123456789012345678901234567890123456789'
n = 10
lista = [string[i:i + n] for i in range(0, len(string), n)]
# Definir na var n a quantidade de vezes que vamos pular
# Fazer o fatiamento [string fatiar o indice: indice + n que é 10]
# no tamanho da string len colocado o param de aprada que é n ou seja de 10 em 10

# juntar os valores numa string com join e separando divisões por . ponto
retorno = '.'.join(lista)
print(retorno)

# assim pegaria de 10 em 10 posicoes
# print(string[0:10])
# print(string[10:20])
# print(string[20:30])
