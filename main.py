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
            id_usuario = 1
            nome_usuario = "Lucas"
            email_usuario = "lucas@gmail.com"

            print("--- SISTEMA DE CADASTRO ---")
            print("Status: Processando dados...")
            print(f"Sucesso! O usuário {nome_usuario} foi salvo.")
            print(f"ID gerado: {id_usuario}")
            print("---------------------------")

        elif opcao == 2: 
            print("\n--- ABRIR NOVA SOLICITAÇÃO ---")
            descricao = input("Descreva o problema/solicitação: ")
            
            protocolo = 1024
            print(f"Sucesso! Solicitação '{descricao}' aberta.")
            print(f"Anote seu protocolo: {protocolo}")
            input("\n[Enter] para voltar ao menu...")

        elif opcao == 3: 
            print("\n--- LISTA DE SOLICITAÇÕES ---")
            print("ID: 001 | Status: Aberto     | Assunto: Troca de Monitor")
            print("ID: 002 | Status: Em Análise | Assunto: Acesso ao E-mail")
            print("ID: 003 | Status: Concluído  | Assunto: Instalação de Software")
            input("\nFim da lista. [Enter] para voltar...")

        elif opcao == 4: 
            print("\n--- ATUALIZAR STATUS ---")
            id_chamado = input("Digite o ID do chamado que deseja atualizar: ")
            print(f"\nO chamado {id_chamado} foi encontrado.")

            print("Para qual status deseja alterar?")
            print("- Aberto")
            print("- Em Andamento")
            print("- Resolvido")
            print("- Cancelado")

            novo_status = input("Escolha a opção: ")

            print(f"--- [OK] STATUS ATUALIZADO COM SUCESSO! ---")
            print(f"Chamado: {id_chamado} | Novo Status: {novo_status}")
            input("\n[Enter] para voltar ao menu principal...")

        elif opcao == 5: 
            print("\n--- ESTATÍSTICAS ---")
            total = 15
            resolvidos = 12
            pendentes = 3
            
            print(f"Total de chamados: {total}")
            print(f"Chamados Resolvidos: {resolvidos}")
            print(f"Chamados Pendentes: {pendentes}")
            input("\n[Enter] para fechar o relatório...")
