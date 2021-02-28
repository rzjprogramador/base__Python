'''

Programa que pergunte a hora ao usuario
baseando no horario descrito exiba a saudacao
Bom dia das 0 as 11
Boa tarde das 12 as 17
Boa noite das 18 as 23

'''
horario = input('Digite um horario das 0 as 23 : ')

if horario.isdigit():
    horario = int(horario)

    if horario < 0 or horario > 23:
        print('Horario tem que estar entre as 0 e 23')
    else:
        if horario <= 11:
            print('Bom dia')
        elif horario <= 17:
            print('Boa Tarde')
        else:
            print('Boa noite')

else:
    print('Por favor , digite um horario entre 0 e 23.')


'''
CONCEITO 
- PERGUNTAR HORARIO 
- CONVERTER RESPOSTA PARA FORMATO ESPERADO

- CERTIFICAR QUE ESTA RECEBENDO HORARIO VALIDO ENTRE OS LIMITES DE HORAS
- SENAO RESPONDER QUE O LIMITE NAO É VALIDO

- LOGICA SAUDACOES ::
- SE HORARIO <= A NUMERO -- FAÇA ALGO
- SENAO SE HORARIO <= A OUTRO NUMERO -- FAÇA ALGO
- SENAO DEFAULT SÓ PODE SER A ULTIMA OPÇÃO -- FAÇA ALGO

'''
