'''

LIMITE DE 18 A 30 ANOS APRA PEGAR EMPRESTIMO
capturar nome e idade
e definir que 
Só pode pegar emprestimo maior de 18 até 30 anos

'''
nome = input('Digite o seu nome : ')
idade = int(input('Digite a sua idade : '))

idade_inicial = 18
idade_limite = 30

if idade > idade_inicial and idade <= idade_limite:
    print(f'{nome} pode pegar emprestimo !')
else:
    print(f'{nome} não pode pegar emprestimo')
