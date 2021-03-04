venda = input('Valor que vendeu : ')

venda = float(venda)

venda_nivel_1 = 1000
venda_nivel_2 = 2000


comissao_2p = 0.020
comissao_2_5p = 0.025
comissao_3p = 0.030


def msg_premio(venda, comissao):
    total_comissao = venda + comissao
    print(
        f'O valor da venda é {venda}..Sua Comissão é {comissao}')


if venda < 0:
    print('ERRO - Valor gativo é invalido !')
else:
    if venda < venda_nivel_1:
        comissao = venda * comissao_2p
        msg_premio(venda, comissao)
    elif venda < venda_nivel_2:
        comissao = venda * comissao_2_5p
        msg_premio(venda, comissao)
    else:
        comissao = venda * comissao_3p
        msg_premio(venda, comissao)

'''
PROGRAMA PREMIO PARA VENDAS :: 

PREMIO DE 2% DO VALOR DA VENDA, PARA VENDAS ACIMA DE 1000
PREMIO DE 2,5% DO VALOR DA VENDA, PARA VENDAS ACIMA DE 2000
PREMIO DE 3% DO VALOR DA VENDA, PARA VENDA ACIMA DE 3000

'''
