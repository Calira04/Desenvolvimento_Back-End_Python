horario_atual = int(input('Digite o horario atual (0-23): '))

def saudacao(horario_atual):
    if horario_atual <= 5:
        print('Boa madrugada!')
    elif horario_atual <= 11:
        print('Bom dia!')
    elif horario_atual <= 17:
        print('Boa tarde!')
    else:
        print('Boa noite!')

saudacao(horario_atual)    