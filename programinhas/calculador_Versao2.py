# CALCULADOR COM WHILE

while True:
    print()
    num_1 = input('Digite um numero: ')
    num_2 = input('Digite outro numero: ')
    operador = input('Digite o Operador: ')

    # Precaver que seja digitado os esperados numeros
    if not num_1.isnumeric() or not num_2.isnumeric():
        print('Você precisa digitar um numero: ')
        continue
    # com continue nada pra baixo é executado se der erro ele volta ao laço

    # casting para garantir numeros na atribuição
    num_1 = int(num_1)
    num_2 = int(num_2)

    # resposta mostrando resultado
    def resposta():
        print(f'O resultado de {num_1} {operador} {num_2} é {res}')

    if operador == '+':
        res = num_1 + num_2
        resposta()
    elif operador == '-':
        res = num_1 - num_2
        resposta()
    elif operador == '/':
        res = num_1 / num_2
        resposta()
    elif operador == '*':
        res = num_1 * num_2
        resposta()
    else:
        print('Operador Inválido !')

    # sair do loop de perguntas iniciais
    sair = input('Deseja Continuar S / N : ')

    if sair == 'n':
        break
print('Obrigado por utilizar nosso Sistema Calculador')

'''
# função isnumeric checa se o que vem só tem numero-senão tiver retorna False



'''
