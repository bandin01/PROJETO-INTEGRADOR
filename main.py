from database import criar_conexao
import usuarios
import chamados

def exibir_menu():
    print("\n" + "="*30)
    print("  SISTEMA DE SUPORTE TI")
    print("="*30)
    print("1 - Cadastrar Usuário")
    print("2 - Ver Usuários Cadastrados")
    print("3 - Abrir Novo Chamado")
    print("4 - Ver Lista de Chamados")
    print("5 - Atualizar Status")
    print("6 - Estatísticas do Sistema")
    print("0 - Sair")

    try:
        opcao = int(input("\nEscolha uma opção: "))
        return opcao
    except ValueError:
        return -1

def main():
    print("Conectando ao banco de dados remoto...")
    db = criar_conexao()

    if db is None:
        print("\nERRO! Não foi possível conectar ao servidor.")
        print("Verifique se a VPN está ativa e se o seu arquivo .env está correto.")
        return

    repetir = True
    while repetir:
        opcao = exibir_menu()

        if opcao == 0:
            repetir = False
            print("\nEncerrando conexão e fechando programa...")

        elif opcao == 1:
            usuarios.cadastrar_usuario(db)

        elif opcao == 2:
            usuarios.exibir_usuarios(db)

        elif opcao == 3:
            chamados.abrir_chamado(db)

        elif opcao == 4:
            chamados.ver_chamados(db)

        elif opcao == 5:
            chamados.atualizar_status(db)

        elif opcao == 6:
            chamados.mostrar_estatisticas(db)

        else:
            print("\nOpção inválida! Tente novamente.")

    if db.is_connected():
        db.close()
        print("Conexão fechada com sucesso. Até logo!")

if __name__ == "__main__":
    main()