'''
# NUMEROS INTEIROS PAR OU IMPAR
Faça um programa que peça ao usuario para digitar um numero inteiro
informe se este numero é par ou impar, 
Caso o usuario não digite um numero inteiro 
informe que não é um numero inteiro
'''


# CHECAGEM NORMAL
numero = input('digite um numero: ')

if numero.isdigit():
    numero = int(numero)

    if numero % 2 == 0:
        print(f'{numero} é par ')
    else:
        print(f'{numero} é impar ')
else:
    print('Isso não é um numero')

'''
CONCEITO :: NUMERO INTEIRO PAR OU IMPAR :
- PEDIR PRO USUARIO DIGITAR O NUMERO
- VERIFICAR SE O NUMERO É INTEIRO COM A FUNÇÃO isdigit()
- CONVERTER COM CASTING O DIGITADO PARA INTEIRO
- LOGICA PRA VER SE NUMERO É PAR OU IMPAR
- SE O NUMERO % 2 == 0 'É PAR'
- SENÃO É IMPAR
FAZER ELSE FINAL PARA O ISDIGIT()- CASO NAO FOR UM NUMERO
'''
