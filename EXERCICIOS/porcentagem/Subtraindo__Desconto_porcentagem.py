# DESCONTANDO PERCENTUAL com FUNCAO - ENTRADA VIA INPUT
# O quanto em % deseja subtrair

valor1 = float(input('Valor 1 :  '))
descontar = float(input('Descontar :  '))


def sub_descontar(valor1, descontar):
    res = valor1 - (valor1 * descontar) / 100

    print(f'De {valor1:.2f} descontando {descontar:.0f}% restou {res:.2f} ... retirando {valor1 - res:.2f}')


sub_descontar(valor1, descontar)
