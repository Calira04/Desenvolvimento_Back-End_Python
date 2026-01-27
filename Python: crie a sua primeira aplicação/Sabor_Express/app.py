import os

# Lista global que armazena os restaurantes cadastrados no sistema.
# Cada restaurante é representado por um dicionário com:
# - nome: nome do restaurante
# - categoria: tipo de culinária
# - ativo: indica se o restaurante está ativo (True) ou não (False)
restaurantes = [
    {'nome': 'Praça', 'categoria': 'Japonesa', 'ativo': False},
    {'nome': 'Pizza Suprema', 'categoria': 'Pizza', 'ativo': True},
    {'nome': 'Cantina', 'categoria': 'Italiano', 'ativo': False}
]


def exibir_nome_do_programa():
    """
    Exibe o nome do programa em formato de banner ASCII.

    Função apenas visual, usada para deixar o menu inicial mais amigável.
    Não recebe parâmetros e não retorna valores.
    """
    print("""
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░  
""")


def exibir_opcoes():
    """
    Exibe as opções disponíveis no menu principal.

    Função responsável apenas por mostrar as opções ao usuário.
    """
    print('1. Cadastrar restaurante')
    print('2. Listar restaurantes')
    print('3. Alternar estado do restaurante')
    print('4. Sair\n')


def finalizar_app():
    """
    Finaliza o aplicativo.

    Atualmente, apenas exibe um subtítulo informando o encerramento.
    """
    exibir_subtitulo('Finalizar app')


def voltar_ao_menu_principal():
    """
    Pausa a execução até o usuário pressionar uma tecla
    e retorna ao menu principal.
    """
    input('\nDigite uma tecla para voltar ao menu ')
    main()


def opcao_invalida():
    """
    Exibe uma mensagem de erro para opções inválidas
    e retorna ao menu principal.
    """
    print('Opção inválida!\n')
    voltar_ao_menu_principal()


def exibir_subtitulo(texto):
    """
    Exibe um subtítulo formatado no terminal.

    Parâmetros:
    texto (str): Texto que será exibido como subtítulo.
    """
    os.system('clear')
    linha = '*' * len(texto)
    print(linha)
    print(texto)
    print(linha)
    print()


def cadastrar_novo_restaurante():
    """
    Cadastra um novo restaurante na lista global.

    Solicita ao usuário o nome e a categoria do restaurante
    e adiciona um novo dicionário à lista `restaurantes`.
    """
    exibir_subtitulo('Cadastro de novos restaurantes')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria = input(f'Digite o nome da categoria do restaurante {nome_do_restaurante}: ')

    dados_do_restaurante = {
        'nome': nome_do_restaurante,
        'categoria': categoria,
        'ativo': False
    }

    restaurantes.append(dados_do_restaurante)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!')

    voltar_ao_menu_principal()


def listar_restaurantes():
    """
    Lista todos os restaurantes cadastrados.

    Exibe nome, categoria e status (ativado/desativado)
    de cada restaurante.
    """
    exibir_subtitulo('Listando restaurantes')

    print(f"{'Nome do restaurante'.ljust(22)} | {'Categoria'.ljust(20)} | Status")
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'ativado' if restaurante['ativo'] else 'desativado'
        print(f"- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}")

    voltar_ao_menu_principal()


def alternar_estado_restaurante():
    """
    Alterna o estado (ativo/desativado) de um restaurante.

    Busca o restaurante pelo nome informado pelo usuário.
    Caso encontrado, inverte o valor do campo 'ativo'.
    """
    exibir_subtitulo('Alterando estado do restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja alterar o estado: ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']

            if restaurante['ativo']:
                print(f'O restaurante {nome_restaurante} foi ativado com sucesso')
            else:
                print(f'O restaurante {nome_restaurante} foi desativado com sucesso')

    if not restaurante_encontrado:
        print('O restaurante não foi encontrado')

    voltar_ao_menu_principal()


def escolher_opcao():
    """
    Lê a opção escolhida pelo usuário e executa a ação correspondente.

    Trata erros caso o usuário digite algo que não seja um número.
    """
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))

        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            alternar_estado_restaurante()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except ValueError:
        opcao_invalida()


def main():
    """
    Função principal do programa.

    Limpa o terminal, exibe o nome do programa,
    mostra as opções e aguarda a escolha do usuário.
    """
    os.system('clear')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()


# Ponto de entrada do programa
if __name__ == '__main__':
    main()
