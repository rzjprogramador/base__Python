nome = 'Reinaldo'
idade = '43'
es_maior = True

# feita aqui um conversao da str idade para int
idade = int(idade)

if idade > 18:
    print(f'{nome} é maior de idade ')
else:
    print(f'{nome} é menor de idade ')
