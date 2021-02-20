usuario = input('Digite seu nome de usuario : ')
senha = input('Escolha uma senha : ')

# usuarios ja definidos
usuario_bd = 'Reinaldo'
senha_bd = '123'

if usuario == usuario_bd and senha == senha_bd:
    print(f'{usuario} ... Bem vindo Usuario Logado !')
else:
    print('ERRO...Dados Invalidos !')
