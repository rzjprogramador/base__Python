"""
# SIMPLES__IMC

Captar nome, idade, altura e peso de uma pessoa
Criar variavel com ano atual
Obter ano de nascimento da pessoa (baseado na idade e no ano atual)
Obter imc da pessoa com 2 casas decimais (peso e na altura da pessoa)
Exibir um texto com todos valores na tela com F-Strings (com as chaves)

"""
nome = 'Reinaldo'
ano_atual = 2021
ano_nascimento = 1977
peso = 90
altura = 1.90
idade = ano_atual - ano_nascimento
imc = peso / (altura ** 2)

print(f'''
{nome} tem {idade} anos, pesa {peso} kilos,
tem {altura} de altura e imc de {imc:.2f}
''')
