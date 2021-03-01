'''

- Faz a Logica do que precisa

- Faz  Validacao que do que vai receber é o tipo valido se nao for alerta o usuario.

- Faz casting para converter a string para o que quiser receber na entrada de dados

- Continua Complementando sua Logica.

# ------‐---------------------------------------------------------
No console averiguando valores caso resulyados forem Falso, nulos ou indefinidos 
fazer algoritimo para corrigir e chegar ao esperado.
.............................................................................

POSIÇÃO E VALOR ::
Todas Sequencias : elementos,variaveis, atributos, objetos tem posicao e valor
Posicao == indice/ i/ chave/
Valor == valor da variavel
.............................................................................
Para acessar Posicao ou Valor de uma sequencia 
podemos usar a função var.get('chave')

O metodo get() é melhor que as [posicao] porque nos permite tratar erros
caso a busca seja Nula ou None ex: 

# idade nao existe nos meus args, entao tratar a busca pra nao dar erro
    idade = kwargs.get('idade')

    if idade is not None:
        print(idade)
    else:
        print('Idade não existe.')
    # Se quiser omitir o None só retirar o else
    ---------------------------------------------






'''
lista = [1, 2, 3]
pessoa = {'nome': 'Reinaldo', 'idade': 43, 'profissao': 'Prograamdor'}


print(lista)
print(lista[0])


print(pessoa.get('nome'))

