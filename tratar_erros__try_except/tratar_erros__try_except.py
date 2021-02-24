num1 = input('Digite um numero: ')
num2 = input('Digite o segundo numero: ')

try:
    num1 = float(num1)
    num2 = float(num2)

    print(f'Voce digitou {num1} + {num2} :: A soma é: {num1 + num2}')
except:
    print('ERRO - SÓ É ACEITO NUMEROS')

# Tratamento de Erros Python
# try == mostra se dér tudo acerto
# except == mostra o tratamento se der erro
