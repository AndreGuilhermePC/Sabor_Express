import os

lista_de_restalrante = ['Bom prato', 'Belo prato']

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
    print('3. Ativar restaurante')
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
    exibir_subtitulo('Cadastro de novos restaurantes')

    nome_do_restalrante = input('Digite o nome do restaurante que deseja cadastrar: ')
    lista_de_restalrante.append(nome_do_restalrante)
    print(f'O restaurante {nome_do_restalrante} foi cadastrado com sucesso!\n')
    
    voltar_ao_menu_principal()

def lista_restaurante():
    exibir_subtitulo('Listando os restalrantes')
    for restaurante in lista_de_restalrante:
        print(f'.{restaurante}')
    
    voltar_ao_menu_principal()

def escolher_opcoes():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        if opcao_escolhida == 1:
            cadastrar_novo_restalrante()
        elif opcao_escolhida == 2:
            lista_restaurante()
        elif opcao_escolhida == 3:
            print('Ativar restaurante')
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


