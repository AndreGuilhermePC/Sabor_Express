import os

lista_de_restalrante = [{'nome': 'Bom prato', 'categoria':'comida brasileira', 'status':'ativo'},
                        {'nome': 'Bar dos irmãos', 'categoria':'bar', 'status':'inativo'},
                        {'nome': 'Bela Pizza', 'categoria':'comida italiana', 'status':'ativo'}]

def exibir_nome_do_programa():
    print("""
    ░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
    ██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
    ╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
    ░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
    ██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
    ╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░  
    """)

def exibir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Alternar estado do restaurante')
    print('4. Sair\n')

def voltar_ao_menu_principal():
    input('\nDigite um tecla para voltrar para o menu princital ')
    main()

def exibir_subtitulo(texto):
    os.system('cls')
    print(texto)
    print()

def finalizar_app():
    exibir_subtitulo('Finalizar app')

def opcao_invalida():
    print('\nOpçao invalida\n')
    
    voltar_ao_menu_principal()

def cadastrar_novo_restalrante():
    '''Essa função é responsavel por cadastrar um novo restaurante
    Inputs:
    - Nome do restaurante
    - Categoria
    Output:
    - Adiciona um novo restaurante a lista de restaurantes
    '''
    exibir_subtitulo('Cadastro de novos restaurantes')
    
    nome_do_restalrante = input('Digite o nome do restaurante que deseja cadastrar: ')
    solicita_categoria = input(f'Digite o nome da categoria do restaurante {nome_do_restalrante}: ')
    dados_do_restaurante = {'nome':nome_do_restalrante, 'categoria':solicita_categoria, 'status':False}
    lista_de_restalrante.append(dados_do_restaurante)
    print(f'O restaurante {nome_do_restalrante} foi cadastrado com sucesso!\n')
    
    voltar_ao_menu_principal()

def lista_restaurante():
    exibir_subtitulo('Listando os restalrantes')
    for restaurante in lista_de_restalrante:
        #nome_restaurante = 
        print(f'- {restaurante['nome']} | {restaurante['categoria']} | {restaurante['status']}')
    
    voltar_ao_menu_principal()

def alternar_estado_do_restaurante():
    '''Essa função é responsavel por alterar o estado do restaurante
    Inputs:
    - Nome do restaurante
    Outout:
    - A confirmação de que foi ativo, se foi desativado e se esta na lista       
    '''
    exibir_nome_do_programa('Alternar estado do restaurante')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja alterar o estado: ')
    restaurante_encontrado = False
    for restaurante in lista_restaurante:
        if nome_do_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_do_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'O restaurante {nome_do_restaurante} foi desativado com sucesso'
            print(mensagem)
    if not restaurante_encontrado:
        print('O restaurante não foi encontrado')   
    voltar_ao_menu_principal()

def escolher_opcoes():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        if opcao_escolhida == 1:
            cadastrar_novo_restalrante()
        elif opcao_escolhida == 2:
            lista_restaurante()
        elif opcao_escolhida == 3:
            alternar_estado_do_restaurante()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()
        

    

def main():
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcoes()

if __name__ == '__main__':
    main()


