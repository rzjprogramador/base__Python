'''
# TAMANHO CARACTERES

Pergunte o nome do usuario
Se o nome tiver 4 letras ou menos escreva 
'Seu nome é curto'

Se tiver entre 5 e 6 letras 
escreva 'Seu nome é normal'

Se tiver mais que 6 letras 
escreva 'Seu nome é muito grande'

'''

nome = input('Digite seu Nome : ')

# Sempre que for usar uma var mais que uma vez jogue o valor em outra var
tamanho_nome = len(nome)

if tamanho_nome <= 4:
    print('Seu nome é curto')
elif tamanho_nome <= 6:
    print('Seu nome é normal')
else:
    print('Seu nome é grande !')