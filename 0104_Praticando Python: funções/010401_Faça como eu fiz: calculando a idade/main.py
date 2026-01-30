import os

def idade(ano_nascimento, ano_atual):
    os.system('clear')

    idade = ano_atual - ano_nascimento
    print(f'Você tem {idade} anos.')

ano_nascimento = int(input('Digite o ano do seu nascimento: '))
ano_atual = int(input('Digite o ano atual: '))

idade(ano_nascimento, ano_atual)    