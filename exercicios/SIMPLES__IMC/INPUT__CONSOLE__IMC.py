"""
# DESAFIO desafio_dados_anoNascimento_imc_== INPUT CONSOLE

Captar com o Input do console : nome, idade, altura e peso de uma pessoa
Criar variavel com ano atual
Obter ano de nascimento da pessoa (baseado na idade e no ano atual)
Obter imc da pessoa com 2 casas decimais (peso e na altura da pessoa)
Exibir um texto com todos valores na tela com F-Strings (com as chaves)

"""
nome = input('Qual seu nome ? ')
ano_atual = input('Em que ano estamos ? ')
ano_nascimento = input('em que ano você nasceu ? ')
peso = input('Qual o seu peso ? ')
altura = input('Qual a sua altura ? ')

idade = int(ano_atual) - int(ano_nascimento)
imc = int(peso) / (float(altura) ** 2)

print(f'''
{nome} tem {idade} anos, pesa {peso} kilos,
tem {altura} de altura e está com IMC de {imc:.2f}
''')

# Obs: pode converter a string que vem do input por padrao na parte da logica