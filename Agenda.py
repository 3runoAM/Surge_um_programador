nomes_inseridos = []
mensagem = 'Bem vindo ao Agenda 0.1 - Desenvolvido por Alphonse'
print(mensagem)
while True:
    menu = input('1. Cadastrar \n2. Exibir \n3. Apagar \n4. Buscar\n5. Atualizar\n6. Apagar todos \n7. Sair \n')
    if menu == '1':
        nome = input('Insira o nome do contato a ser cadastrado: ')
        if nome in nomes_inseridos:
            print(f'Você digitou "{nome.capitalize()}". Esse contato já foi cadastrado, tente outro.')
        else:
            nomes_inseridos.append(nome)
            contatos = len(nomes_inseridos)
            print(f'Contato cadastrado. Você possui {contatos} contatos cadastrados.')
    elif menu == '2':
        if len(nomes_inseridos) == 0:
            print('Nenhum contato cadastrado.')
        else:
            print(nomes_inseridos)
    elif menu == '3':
        cont_del = input('Qual contato deseja remover? ')
        if cont_del in nomes_inseridos:
            nomes_inseridos.remove(cont_del)
            cont_atu = len(nomes_inseridos)
            print(f'Contato removido. Você possui {cont_atu} contatos.')
        else:
            print(f'{cont_del} não existe nos contatos cadastrados. Tente outro contato.')
    elif menu == '4':
        busca = input('Busca: ')
        for nome in nomes_inseridos:
            if busca in nome:
                print(nome)
    elif menu == '5':
        atualizado = input('Qual contato deseja atualizar? ')
        if atualizado in nomes_inseridos:
            nomes_inseridos.remove(atualizado)
            novo_cont = input(f'Cadastre novo nome: ')
            nomes_inseridos.append(novo_cont)
            print(f'O contato {atualizado} foi atualizado para {novo_cont}')
        else:
            print(f'{atualizado} não está entre os contatos cadastrados. Tente outro contato.')
    elif menu == '6':
        nomes_inseridos.clear()
        print(f'Todos os contatos foram apagados.')
    elif menu == '7':
        break
    else:
        print('Digite uma opção válida.')
