'''
DESCOBRIR QUANTO AUMENTOU EM PORCENTAGEM
COM VALOR FINAL JA DEFINIDO.

'''


peca1_nome = 'Cart'
valor_inicial_peca1 = 400
v_atual_peca1 = 450


# Descobrindo quanto aumentou
quanto_aumentou = v_atual_peca1 - valor_inicial_peca1
# print(quanto_aumentou)

# Descobrindo a fração do aumento
fracao_do_aumento = quanto_aumentou / valor_inicial_peca1
# print(fracao_do_aumento)

# Descobrindo quanto em porcentagem aumentou
porc_aumentou = fracao_do_aumento * 100
print(f'''
{peca1_nome} teve um aumento de {porc_aumentou}% 
passando de {valor_inicial_peca1:.2f} para {v_atual_peca1:.2f}
    ''')
