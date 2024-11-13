
      exibir_subtitulo('Cadastro de Novos Restaurantes')
      nome_do_restaurante = input("\nDigite o nome do restaurante que deseja cadastrar: ")
      #restaurantes.append(nome_do_restaurante['nome'])  ---ESTE CASO EH USADO QUANOD QUERIAMOS ADICIONAR O RESTAURANTE A LISTA--- 
      categoria_restaurante = input(f'Digite o nome da categoria do restaurante {nome_do_restaurante}: ') 
      dados_do_restaurante = {'nome':nome_do_restaurante, 'categoria':categoria_restaurante, 'ativo':False} # ESTA E A FORMA DE ADD EM DICIONARIOS
      restaurantes.append(dados_do_restaurante)

      print(f'Restaurante {nome_do_restaurante} cadastrado com SUCESSO!')

      voltar_menu_principal()

def listar_restaurantes():