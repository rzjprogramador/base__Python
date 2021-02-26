
# TABUADA COM WHILE

tabuada_desejada = int(input('Tabuada do : '))
limite_tabuada = int(input('Quantas vezes deseja a tabuada : '))

i = 1
while i <= limite_tabuada:
    res = i * tabuada_desejada
    print(f'{tabuada_desejada} x {i} = {res}')
    i += 1
