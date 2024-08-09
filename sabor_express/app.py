import os

restaurantes = [{'nome':'Praça', 'categoria': 'Japonesa', 'ativo':      False},
                {'nome':'Pizza Suprema', 'categoria': 'Pizza', 'ativo': True},
                {'nome':'Cantina', 'categoria': 'Italiano', 'ativo': False}]

#_____________________________________________________________________________

def exibir_nome_do_programa():
    print("""
    𝙎𝙖𝙗𝙤𝙧 𝙚𝙭𝙥𝙧𝙚𝙨𝙨
          """)
    
def exibir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Alternar estado do restaurante')
    print('4. Sair\n')
    
def finalizar_app():
    exibir_subtitulo('Finalizando o app\n')

def voltar_ao_menu_principal():
    input('\nDigite uma tecla para voltar ao menu principal')
    main()
    
def opcao_invalida():
    print('Opção inválida!\n')
    voltar_ao_menu_principal()

def exibir_subtitulo(texto):
    os.system('cls')
    linha = '*' * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()

def main():
    """
    Função principal que inicia o programa
          """
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()

if __name__ == '__main__':
    main()

#____________________________________________________________________

def cadastrar_novo_restaurante():
    """
    Função para cadastrar um novo restaurante

    Inputs: 
    - Nome do restaurante
    - Categoria

    Outputs:
    - Adiciona um novo restaurante à lista de restaurantes
    """

    exibir_subtitulo('Cadastro de novos restaurantes\n')
    nome_do_restaurante = input(f'Digite o nome do restaurangte que deseja cadastrar: ')
    categoria = input(f'Digite a categoria do restaurante que deseja cadastrar {nome_do_restaurante}: ')
    dados_do_restaurante = {'nome':nome_do_restaurante, 'categoria':categoria, 'ativo':False}
    restaurantes.append(dados_do_restaurante)
    print(f'Orestaurante {nome_do_restaurante} foi cadastrado com sucesso!')

    voltar_ao_menu_principal()

#____________________________________________________________________

def alternar_estado_do_restaurante():
    """
    Função para ativar ou desativar um novo restaurante
    """
    exibir_subtitulo('Alternando estado do restaurante\n')
    nome_restaurante = input(f'Digite o nome do restaurante que deseja alterar o estado: ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso!' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso!'
            print(mensagem)

        if not restaurante_encontrado:
            print(f'O restaurante não foi encontrado!')

voltar_ao_menu_principal()

#___________________________________________________________________

def listar_restaurantes():
    """
    Função para listar todos os restaurantes cadastrados
    """
    exibir_subtitulo('Listando os restaurante\n')

    print(f'{'nome_restaurante'.ljust(21)} | {'categoria'.ljust(20)} | Status')

    for restaurante in restaurantes:
            nome_restaurante = restaurante['nome']:
            categoria = restaurante['categoria']
            ativo = 'ativado' if restaurante['ativo'] else 'desativado'
            print(f'-{nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')

voltar_ao_menu_principal()

#_______________________________________________________________

def escolher_opcao():
    """
    Função para processar a escolha do usuário no menu principal
    """
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))

        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            alterar_estado_restaurante()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()


voltar_ao_menu_principal()



