# função len -- contador de caracteres

usuario = input('Digite seu nome: ')
quant_caracteres = len(usuario)

print(f'Seu nome é {usuario} e tem {quant_caracteres} caracteres.')

# Analisar se digitou quantidade certa de caracteres
if quant_caracteres < 6:
    print('Você precisa digitar pelo menos 6 caracteres')
else:
    print('Cadastrado com sucesso')

# Obs: dados float e booleanos não tem len
