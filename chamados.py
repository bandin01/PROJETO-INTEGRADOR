from usuarios import listar_usuarios


#  PRIORIDADE AUTOMÁTICA
#  ─────────────────────
#  Regra: o usuário informa urgencia (1-3) e impacto (1-3)
#  Soma 2-3 = Baixa | Soma 4 = Media | Soma 5-6 = Alta

def calcular_prioridade(urgencia, impacto):
    soma = urgencia + impacto
    if soma <= 3:
        return "baixa"
    elif soma == 4:
        return "media"
    else:
        return "alta"


#  ABRIR CHAMADO
#  ─────────────

def abrir_chamado(conexao):
    print("\n=== ABRIR NOVO CHAMADO ===")

    # Mostra usuários e pede o ID
    usuarios = listar_usuarios(conexao)
    if not usuarios:
        print("ERRO! Nenhum usuário cadastrado. Cadastre um usuário primeiro.")
        return

    print(f"\n{'ID':<5} {'Nome'}")
    print("-" * 30)
    for u in usuarios:
        print(f"{u['id_usuario']:<5} {u['nome']}")

    id_valido = False
    while not id_valido:
        id_solicitante = input("\nDigite seu ID de usuário: ").strip()
        for u in usuarios:
            if str(u['id_usuario']) == id_solicitante:
                id_valido = True
        if not id_valido:
            print("ERRO! ID não encontrado. Tente novamente.")

    # Título (obrigatório)
    titulo_valido = False
    while not titulo_valido:
        titulo = input("Título do problema: ").strip()
        if len(titulo) >= 5:
            titulo_valido = True
        else:
            print("ERRO! Título deve ter ao menos 5 caracteres.")

    # Descrição (obrigatória)
    descricao_valida = False
    while not descricao_valida:
        descricao = input("Descrição detalhada: ").strip()
        if len(descricao) >= 10:
            descricao_valida = True
        else:
            print("ERRO! Descrição deve ter ao menos 10 caracteres.")

    # Urgência e impacto para cálculo automático de prioridade
    print("\nUrgência do problema:")
    print("  1 - Baixa")
    print("  2 - Média")
    print("  3 - Alta")

    urgencia_valida = False
    while not urgencia_valida:
        urg_op = input("Urgência (1-3): ").strip()
        if urg_op in ("1", "2", "3"):
            urgencia = int(urg_op)
            urgencia_valida = True
        else:
            print("ERRO! Digite 1, 2 ou 3.")

    print("\nImpacto do problema:")
    print("  1 - Afeta só você")
    print("  2 - Afeta o setor")
    print("  3 - Afeta a empresa")

    impacto_valido = False
    while not impacto_valido:
        imp_op = input("Impacto (1-3): ").strip()
        if imp_op in ("1", "2", "3"):
            impacto = int(imp_op)
            impacto_valido = True
        else:
            print("ERRO! Digite 1, 2 ou 3.")

    # Prioridade calculada automaticamente
    prioridade = calcular_prioridade(urgencia, impacto)
    print(f"\nPrioridade calculada automaticamente: {prioridade.upper()}")

    cursor = conexao.cursor()
    try:
        sql = """INSERT INTO Chamado (titulo, descricao, prioridade, id_solicitante)
                 VALUES (%s, %s, %s, %s)"""
        cursor.execute(sql, (titulo, descricao, prioridade, int(id_solicitante)))
        conexao.commit()
        print(f"Chamado aberto com sucesso! Protocolo: {cursor.lastrowid}")
    except Exception as e:
        print(f"Erro ao abrir chamado: {e}")
    finally:    
        cursor.close()


#  VER CHAMADOS
#  ─────────────

def ver_chamados(conexao):
    print("\n=== LISTA DE CHAMADOS ===")

    # Mini-menu de filtro por prioridade
    print("\nFiltrar por prioridade:")
    print("  1 - Todas")
    print("  2 - Baixa")
    print("  3 - Média")
    print("  4 - Alta")

    filtro_valido = False
    while not filtro_valido:
        filtro_op = input("Escolha: ").strip()
        if filtro_op == "1":
            filtro = None
            filtro_valido = True
        elif filtro_op == "2":
            filtro = "baixa"
            filtro_valido = True
        elif filtro_op == "3":
            filtro = "media"
            filtro_valido = True
        elif filtro_op == "4":
            filtro = "alta"
            filtro_valido = True
        else:
            print("ERRO! Digite 1, 2, 3 ou 4.")

    cursor = conexao.cursor(dictionary=True)
    try:
        if filtro:
            query = """
                SELECT c.id_chamado, c.titulo, c.status, c.prioridade, u.nome AS solicitante
                FROM Chamado c
                JOIN Usuario u ON c.id_solicitante = u.id_usuario
                WHERE c.prioridade = %s
                ORDER BY c.id_chamado DESC
            """
            cursor.execute(query, (filtro,))
        else:
            query = """
                SELECT c.id_chamado, c.titulo, c.status, c.prioridade, u.nome AS solicitante
                FROM Chamado c
                JOIN Usuario u ON c.id_solicitante = u.id_usuario
                ORDER BY c.id_chamado DESC
            """
            cursor.execute(query)

        resultados = cursor.fetchall()

        if not resultados:
            print("Nenhum chamado encontrado.")
        else:
            print(f"\n{'ID':<5} {'Status':<15} {'Prioridade':<10} {'Solicitante':<20} Título")
            print("-" * 75)
            for c in resultados:
                print(f"{c['id_chamado']:<5} {c['status']:<15} {c['prioridade']:<10} {c['solicitante']:<20} {c['titulo']}")
    except Exception as e:
        print(f"Erro ao listar chamados: {e}")
    finally:
        cursor.close()

    input("\n[Enter] para voltar...")


#  ATUALIZAR STATUS
#  ─────────────────

def atualizar_status(conexao):
    print("\n=== ATUALIZAR STATUS ===")

    id_chamado = input("ID do Chamado: ").strip()

    # Verifica se o chamado existe e pega o status atual
    cursor = conexao.cursor(dictionary=True)
    try:
        cursor.execute("SELECT status FROM Chamado WHERE id_chamado = %s", (id_chamado,))
        chamado = cursor.fetchone()
    finally:
        cursor.close()

    if not chamado:
        print("ERRO! Chamado não encontrado.")
        return

    status_atual = chamado["status"]
    print(f"Status atual: {status_atual}")

    # Regra de transição: chamado concluído não pode ser reaberto
    if status_atual == "concluido":
        print("ERRO! Chamados concluídos não podem ser reabertos.")
        return

    print("\nNovo status:")
    print("  1 - Aberto")
    print("  2 - Em Atendimento")
    print("  3 - Concluído")

    status_valido = False
    while not status_valido:
        st_op = input("Escolha: ").strip()
        if st_op == "1":
            novo_status = "aberto"
            status_valido = True
        elif st_op == "2":
            novo_status = "em_atendimento"
            status_valido = True
        elif st_op == "3":
            novo_status = "concluido"
            status_valido = True
        else:
            print("ERRO! Digite 1, 2 ou 3.")
            continue

        if status_valido and novo_status == status_atual:
            print(f"AVISO! O chamado já está com o status '{status_atual}'.")
            return

    cursor = conexao.cursor()
    try:
        sql = "UPDATE Chamado SET status = %s WHERE id_chamado = %s"
        cursor.execute(sql, (novo_status, id_chamado))
        conexao.commit()
        if cursor.rowcount > 0:
            print("Status atualizado com sucesso!")
        else:
            print("ERRO! Chamado não encontrado.")
    except Exception as e:
        print(f"Erro ao atualizar status: {e}")
    finally:
        cursor.close()


#  ESTATÍSTICAS
#  ─────────────

def mostrar_estatisticas(conexao):
    print("\n=== ESTATÍSTICAS DO SISTEMA ===")
    cursor = conexao.cursor()
    try:
        # Conta o total geral de chamados
        cursor.execute("SELECT COUNT(*) FROM Chamado")
        total = cursor.fetchone()[0]
        print(f"Total de chamados: {total}")

        # Por status
        print("\n--- Por Status ---")
        cursor.execute("SELECT status, COUNT(*) FROM Chamado GROUP BY status")
        for status, quantidade in cursor.fetchall():
            print(f"  {status:<20} {quantidade}")

        # Por prioridade (usando GROUP BY)
        print("\n--- Por Prioridade ---")
        cursor.execute("SELECT prioridade, COUNT(*) FROM Chamado GROUP BY prioridade")
        for prioridade, quantidade in cursor.fetchall():
            print(f"  {prioridade:<20} {quantidade}")

    except Exception as e:
        print(f"Erro ao gerar estatísticas: {e}")
    finally:
        cursor.close()

    input("\n[Enter] para fechar o relatório...")