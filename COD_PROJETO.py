repetir = True 
while repetir:
    print("====== SCSC: Sistema de Controle de Solicitações Corporativos ======") 
    print("1 - Cadastrar Usuário") 
    print("2 - Abrir Solicitação") 
    print("3 - Ver Solicitações") 
    print("4 - Atualizar Status") 
    print("5 - Estatísticas") 
    print("0 - Sair\n") 
    
    try:
        opcao = int(input("\nEscolha uma opção: "))
    except ValueError:
        print("Opcao invalida!")
    else:
        if opcao == 0: # Sair do Programa
            repetir = False
            print("\nPROGRAMA ENCERRADO!")   

        elif opcao < 0 or opcao > 5:
            print("Opcao invalida!")

        elif opcao == 1: 
            # Cadastrar usuário
            teste = 1
        elif opcao == 2: 
            # Abrir solicitação
            teste = 1
        elif opcao == 3: 
            # Ver Solicitações
            teste = 1
        elif opcao == 4: 
            # Atualizar Status
            teste = 1
        elif opcao == 5: 
            # Estatísticas
            teste = 1
