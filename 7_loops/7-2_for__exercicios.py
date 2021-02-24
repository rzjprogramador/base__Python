sequencia2 = ['Reinaldo', 'Gustavo', 'Victor', 'Leornardo']


# MOSTRAR VALORES DA LISTA
for v in sequencia2:
    print(v)


# MOSTRAR VALORES DA LISTA
numeros = [1, 3, 4, 2, 6, 7]

for v2 in numeros:
    print(v2)


# MOSTRAR VALORES DA LISTA
for novosNumeros in numeros:
    print(f'Esses são os numeros da lista : {novosNumeros} !!!')


# MOSTRAR INDICE E VALORES DA LISTA
for indice, valoresPegaeMostra in enumerate(numeros):
    print(
        f'Este é o indice: {indice} e esses os valores : {valoresPegaeMostra}')
