telefones = ["11987654321", "21912345678", "31987654321", "11911223344"] 
telefones_corrigidos = []
mensagem = ''

def conversor_de_telefones(telefones):
    for telefone in telefones:
        telefone = int(telefone)
        telefones_corrigidos.append(telefone)

def verificar_conversor(telefones_corrigidos):
    global mensagem
    for telefone in telefones_corrigidos:
        if type(telefone) is str:
            mensagem = f'O telefone {telefone} é uma string.'
            break
        elif type(telefone) is int:
            mensagem = 'Todos os números foram convertidos corretamente!'
    print(mensagem)

conversor_de_telefones(telefones)
verificar_conversor(telefones_corrigidos)
