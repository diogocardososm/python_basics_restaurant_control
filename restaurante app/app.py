import os

#restaurantes = ['Pizzaria MaQ', 'Sushi mtacomidaPokopinto','mcdogs']  ---- Exemplo de lista usado antes de mudar para dicionario

#Dicionario
restaurantes = [{'nome':'sushi', 'categoria':'Japonesa', 'ativo':False},
                {'nome':'Pizzaria', 'categoria':'Italiana', 'ativo':True},
                {'nome':'mcdonalds', 'categoria':'Fast Food','ativo':False}
                ]
#MAIN 
def main():
    os.system('cls')
    exibir_logo()
    exibir_opcoes()
    escolha_do_usuario()
    

def exibir_logo():
    #fsymbols no google
    print("""

░█████╗░██╗░░░██╗██╗░██████╗██╗███╗░░██╗███████╗░█████╗░░█████╗░███╗░░██╗████████╗██████╗░░█████╗░██╗░░░░░
██╔══██╗██║░░░██║██║██╔════╝██║████╗░██║██╔════╝██╔══██╗██╔══██╗████╗░██║╚══██╔══╝██╔══██╗██╔══██╗██║░░░░░
██║░░╚═╝██║░░░██║██║╚█████╗░██║██╔██╗██║█████╗░░██║░░╚═╝██║░░██║██╔██╗██║░░░██║░░░██████╔╝██║░░██║██║░░░░░
██║░░██╗██║░░░██║██║░╚═══██╗██║██║╚████║██╔══╝░░██║░░██╗██║░░██║██║╚████║░░░██║░░░██╔══██╗██║░░██║██║░░░░░
╚█████╔╝╚██████╔╝██║██████╔╝██║██║░╚███║███████╗╚█████╔╝╚█████╔╝██║░╚███║░░░██║░░░██║░░██║╚█████╔╝███████╗
░╚════╝░░╚═════╝░╚═╝╚═════╝░╚═╝╚═╝░░╚══╝╚══════╝░╚════╝░░╚════╝░╚═╝░░╚══╝░░░╚═╝░░░╚═╝░░╚═╝░╚════╝░╚══════╝
""")

def exibir_opcoes():
    print('1. Cadastrar Restaurante')
    print('2. Listar Restaurante')
    print('3. Ativar/Desativar Restaurante')
    print('4. Sair')

def escolha_do_usuario():
    try:
        escolha_usuario = int(input('\nEscolha uma opcao: '))
        match escolha_usuario:
            case 1:
                    cadastrar_novo_restaurante()
            case 2:
                    listar_restaurantes()
            case 3: 
                    status()
            case 4:
                    finalizar_app()
            case _:
                    opcao_invalida()
    except:
          opcao_invalida()
        
def finalizar_app():
    exibir_subtitulo('Finalizando App')

def opcao_invalida():
      print('\nOpcao Invalida!')

      voltar_menu_principal()

def cadastrar_novo_restaurante():
      exibir_subtitulo('Cadastro de Novos Restaurantes')
      nome_do_restaurante = input("\nDigite o nome do restaurante que deseja cadastrar: ")
      #restaurantes.append(nome_do_restaurante['nome'])  ---ESTE CASO EH USADO QUANOD QUERIAMOS ADICIONAR O RESTAURANTE A LISTA--- 
      categoria_restaurante = input(f'Digite o nome da categoria do restaurante {nome_do_restaurante}: ') 
      dados_do_restaurante = {'nome':nome_do_restaurante, 'categoria':categoria_restaurante, 'ativo':False} # ESTA E A FORMA DE ADD EM DICIONARIOS
      restaurantes.append(dados_do_restaurante)

      print(f'Restaurante {nome_do_restaurante} cadastrado com SUCESSO!')

      voltar_menu_principal()

def listar_restaurantes():
    exibir_subtitulo('Listando Restaurantes')

    print(f'{"Restaurante".ljust(22)} | {"Categoria".ljust(20)} | {"Status"}')

    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria_restaurante = restaurante['categoria']
        atividade = 'ativado' if restaurante['ativo'] else 'desativado'
        print(f'- {nome_restaurante.ljust(20)} | {categoria_restaurante.ljust(20)} | {atividade}')  

    voltar_menu_principal()

def voltar_menu_principal():
    input('\nPressione Enter para voltar ao menu ')
    main()

def exibir_subtitulo(texto):
     os.system('cls')
     linha = '*' * len(texto)
     print(linha)
     print(texto)
     print(linha)
     print()

def status():
        exibir_subtitulo('Alterando status do restaurante')
        nome_restaurante = input('\nDigite o restaurante que deseja ativar: ')
        consulta_de_restaurante = False
        for restaurante in restaurantes:
             if nome_restaurante == restaurante['nome']:
                  consulta_de_restaurante = True
                  restaurante ['ativo'] = not restaurante['ativo']
                  mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'O restaurante foi desativado com sucesso' # CONDICAO CHAMADA TERNARIO 
                  print(mensagem)
        
        if not consulta_de_restaurante:
             print('O restaurante nao foi encontrado')


        voltar_menu_principal()


#CRIAR A MAIN FUNCTION
if __name__ == '__main__':
    main()

