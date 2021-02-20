"""
# DESAFIO desafio_dados_anoNascimento_imc_== INPUT CONSOLE

Captar com o Input do console : nome, idade, altura e peso de uma pessoa
Criar variavel com ano atual
Obter ano de nascimento da pessoa (baseado na idade e no ano atual)
Obter imc da pessoa com 2 casas decimais (peso e na altura da pessoa)
Exibir um texto com todos valores na tela com F-Strings (com as chaves)

"""
nome = str(input('Qual seu nome ? '))
ano_atual = int(input('Em que ano estamos ? '))
ano_nascimento = int(input('em que ano você nasceu ? '))
peso = int(input('Qual o seu peso ? '))
altura = float(input('Qual a sua altura ? '))
idade = ano_atual - ano_nascimento
imc = peso / (altura ** 2)

print(f'''
{nome} tem {idade} anos, pesa {peso} kilos,
tem {altura} de altura e está com IMC de {imc:.2f}
''')
