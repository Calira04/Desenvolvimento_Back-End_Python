nome_usuario = ''
senha = ''

while len(nome_usuario) < 5 or len(senha) < 8:
    nome_usuario = str(input("Digite seu nome de usuário: "))
    senha = str(input("Digite sua senha: "))

    if len(nome_usuario) < 5:
        print('O nome de usuário deve ter pelo menos 5 caracteres.')
    elif len(senha) < 8:
        print('A senha deve ter pelo menos 8 caracteres.')
print('Cadastro realizado com sucesso!')