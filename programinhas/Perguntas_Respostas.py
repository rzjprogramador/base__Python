print('SISTEMA PERGUNTAS E RESPOSTAS')

perguntas = {
    'Pergunta 1': {
        'pergunta': 'Quanto é 2 + 2 ? ',
        'respostas': {'a': '1', 'b': '4', 'c': '5'},
        'resposta_certa': 'b'
    },
    'Pergunta 2': {
        'pergunta': 'Quanto é 3 * 2 ? ',
        'respostas': {'a': '4', 'b': '10', 'c': '6'},
        'resposta_certa': 'c'
    },
}

print('--------------------------------------')

respostas_certas = 0

for pk, pv in perguntas.items():
    print(f'{pk} : {pv["pergunta"]}')
    print('Escolha as Opções :')

    for rk, rv in pv['respostas'].items():
        print(f'[{rk}] : {rv} ')

    resposta_usuario = input('Sua Resposta: ')

    if resposta_usuario == pv['resposta_certa']:
        print('EHHH VOCE ACERTOU !!!')
        respostas_certas += 1
    else:
        print('IXIII...VOCE ERROU :)')

    print('--------------------------------------')

qtd_perguntas = len(perguntas)
porcentagem_acerto = respostas_certas / qtd_perguntas * 100

print(f'Entre as {len(perguntas)} Perguntas, você acertou {respostas_certas} ')
print(f'Sua porcentagem de acerto foi de {porcentagem_acerto}% ')


'''
CONCEITO DO PROGRAMA PERGUNTAS E RESPOSTAS:

Iniciar o Dicionario perguntas = {}

Dentro as perguntas 'Pergunta 1' : 
    {'chave- Pergunta': 'valor - Pergunta'}
    'chave-Respostas': {# 
        DICIONARIO PARA RESPOSTAS COM chave e valor respostas}

# INTERAÇÕES
    for pergunta-key, pergunta-valor in perguntas.items():
        print(f'NOS ARGS PEDIDOS {pk} e {pv}')

        #Mostrar no loop filho as opções
        for respostas-keys, respostas_valor in perguntas_valor['respostas'].items():

OBS:No for # para mostrar os items do filho q são os netos
arg_do_key_Filho['chave_do_Filho'] 

# LOGICA :
Definir fora do loop for a variavel que vai inicar o contador de respostas certas
respostas_certas = 0

e na logica incrementar esta variavel contadora 
dentro do loop filho :: na condicao True
respostas_certas += 1 -- dentro do loop

# logica do negocio :

if resposta_usuario == pv['resposta_certa']:
        print('EHHH VOCE ACERTOU !!!')
        respostas_certas += 1
    else:
        print('IXIII...VOCE ERROU :)')

qtd_perguntas = len(perguntas)
porcentagem_acerto = respostas_certas / qtd_perguntas * 100

print(f'Entre as {len(perguntas)} Perguntas, você acertou {respostas_certas} ')
print(f'Sua porcentagem de acerto foi de {porcentagem_acerto}% ')




'''
