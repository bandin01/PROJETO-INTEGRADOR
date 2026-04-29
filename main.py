# Então, de início precisamos de listas. 3 listas.
usuarios = []
solicitacoes = []
contador_protocolo = 0

# Depois precisamos criar as funções antes do código principal, primeiro a def do menu
def exibir_menu():
    print("=== SISTEMA DE CHAMADO INTERNO ===") 
    print("1 - Cadastrar Usuário") 
    print("2 - Abrir Solicitação") 
    print("3 - Ver Solicitações") 
    print("4 - Atualizar Status") 
    print("5 - Estatísticas") 
    print("0 - Sair")

    # Agora tornar anti-anta
    try:
        opcao = int(input("\nEscolha uma opção: "))
        return opcao    # Manda a opcao escolhida para o menu, caso dê tudo certo
    except ValueError:
        return -1       # Retorna -1 para forçar o aviso de "Opção inválida" lá no Main

def cadastrar_usuario():
    print("\n=== SISTEMA DE CADASTRO ===")
    nome = input("Nome do usuário: ").strip()
    email = input("E-mail do usuário: ").strip()

    # len(usuarios) conta quantos itens existem dentro da lista, cria um usuário posterior ao último cadastrado
    id_usuario = len(usuarios) + 1

    # Salva os dados do usuário dentro da lista
    usuarios.append({
        "id": id_usuario, 
        "nome": nome, 
        "email": email
    }) 
    
    print(f"Sucesso! O usuário {nome} foi salvo.")
    print(f"ID gerado: {id_usuario}")
    input("[Enter] para voltar...\n")

def abrir_solicitacao(protocolo_atual):
    print("\n=== ABRIR NOVA SOLICITAÇÃO ===")

    descricao_valida = False
    while not descricao_valida:
        descricao = input("Descreva o problema (mín. 10 caracteres): ").strip()
        if len(descricao) >= 10:
            descricao_valida = True
        else:
            print("Descrição muito curta! Por favor, detalhe mais o problema.\n")

    novo_protocolo = protocolo_atual + 1
    solicitacoes.append({
        "protocolo": novo_protocolo,
        "descricao": descricao,
        "status": "Aberto"
    })

    print(f"Sucesso! Solicitação aberta com protocolo: {novo_protocolo}\n")
    
    return novo_protocolo

def ver_solicitacoes():
    print("\n=== LISTA DE SOLICITAÇÕES ===")
    if len(solicitacoes) == 0:
        print("Nenhuma solicitação cadastrada ainda.")

    else:
        for sol in solicitacoes:
            # Formatação para manter a tabela alinhada
            print(f"Protocolo: {sol['protocolo']} | Status: {sol['status']:<12} | Assunto: {sol['descricao']}")
            
    input("\nFim da lista. [Enter] para voltar...")

def atualizar_status():
    print("\n=== ATUALIZAR STATUS ===")

    # Verifica se a lista está vazia
    if not solicitacoes:
        print("Não há chamados abertos para atualizar.")
        input("\n[Enter] para voltar ao menu principal...")
        return
    
    verificar_erro = True
    while verificar_erro:
        try:
            id_chamado = int(input("Digite o Protocolo do chamado que deseja atualizar: "))

            # Se chegou aqui, é porque o número é válido!
            # Então mudamos a variável para sair do loop
            verificar_erro = False

        except ValueError:
            print("Formato de protocolo inválido!")

    # Busca o chamado na lista
    chamado_encontrado = None
    for sol in solicitacoes:
        if sol['protocolo'] == id_chamado:
            chamado_encontrado = sol
            break # tirar esse break ---------------------------------------------------------

    if chamado_encontrado:
        print(f"\nO chamado {id_chamado} foi encontrado.\n")
        print("Para qual status deseja alterar?")
        print("1 - Aberto")
        print("2 - Em Andamento")
        print("3 - Resolvido")

        opcoes = {"1": "Aberto", "2": "Em Andamento", "3": "Resolvido"}
        escolha = input("\nEscolha a opção (1-3): ")

        if escolha in opcoes:
            novo_status = opcoes[escolha]
            chamado_encontrado['status'] = novo_status
            print(f"\nSTATUS ATUALIZADO COM SUCESSO!")
            print(f"Chamado: {id_chamado} | Novo Status: {novo_status}")
        else:
            print("Opção de status inválida.")
    else:
        print("Chamado não encontrado no sistema.")
        
    input("\n[Enter] para voltar ao menu principal...")

def mostrar_estatisticas():
    print("\n=== ESTATÍSTICAS ===")
    total = len(solicitacoes)
    
    # Conta os status
    resolvidos = sum(1 for sol in solicitacoes if sol['status'] == "Resolvido")
    pendentes = total - resolvidos
    
    print(f"Total de chamados: {total}")
    print(f"Chamados Resolvidos: {resolvidos}")
    print(f"Chamados Pendentes/Em Andamento: {pendentes}")
    input("\n[Enter] para fechar o relatório...")

def main():
    # Iniciamos o contador aqui dentro para podermos controlar o fluxo dele
    protocolo_do_sistema = 0

    repetir = True
    while repetir:
        opcao = exibir_menu()
        
        if opcao == 0: 
            repetir = False
            print("\nPROGRAMA ENCERRADO!")   
        elif opcao == 1: 
            cadastrar_usuario()
        elif opcao == 2: 
            protocolo_do_sistema = abrir_solicitacao(protocolo_do_sistema)
        elif opcao == 3: 
            ver_solicitacoes()
        elif opcao == 4: 
            atualizar_status()
        elif opcao == 5: 
            mostrar_estatisticas()
        else:
            print("\nOpção inválida! Tente novamente.")

# Ponto de entrada do programa
if __name__ == "__main__":
    main()