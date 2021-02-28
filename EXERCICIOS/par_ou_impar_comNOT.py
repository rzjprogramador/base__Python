'''
# NUMEROS INTEIROS PAR OU IMPAR
Faça um programa que peça ao usuario para digitar um numero inteiro
informe se este numero é par ou impar, 
Caso o usuario não digite um numero inteiro 
informe que não é um numero inteiro
'''


# CHECAGEM INVERTIDA COM NEGAÇÃO NOT
numero = input('digite um numero: ')

if not numero.isdigit():
    print('Isso não é um numero inteiro')
else:
    numero = int(numero)

    if not numero % 2 == 0:
        print(f'{numero} é impar ')
    else:
        print(f'{numero} é par ')

'''
CONCEITO :: NUMERO INTEIRO PAR OU IMPAR INVERTIDO COM NEGAÇÃO NOT:

- PEDIR PRO USUARIO DIGITAR O NUMERO

- VERIFICAR SE NAO É UM NUMERO INTEIRO COM A FUNÇÃO isdigit()
- RESPONDER NO ISDIGIT()- CASO NAO FOR UM NUMERO

- CONVERTER COM CASTING O DIGITADO PARA INTEIRO

- LOGICA PRA VER SE NUMERO É PAR OU IMPAR::
- SE NÃO É UM NUMERO % 2 == 0 'É IMPAR'
- SENÃO É PAR
'''
