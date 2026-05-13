#  VALIDAÇÃO
#  ─────────

def _validar_email(email):
    # Verifica se tem @ e se tem ponto depois do @
    return "@" in email and "." in email.split("@")[-1] # VER SE TEM FORMA MAIS SIMPLES DE VALIDAR E-MAIL

def email_ja_cadastrado(conexao, email):
    # Retorna True se o e-mail já existe no banco
    cursor = conexao.cursor()
    cursor.execute("SELECT id_usuario FROM Usuario WHERE email = %s", (email,))
    existe = cursor.fetchone() is not None
    cursor.close()
    return existe

def usuario_existe(conexao, id_usuario):
    # Retorna True se o ID existe no banco
    cursor = conexao.cursor()
    cursor.execute("SELECT id_usuario FROM Usuario WHERE id_usuario = %s", (id_usuario,))
    existe = cursor.fetchone() is not None
    cursor.close()
    return existe



#  CADASTRO DE USUÁRIO
#  ───────────────────

def cadastrar_usuario(conexao):
    print("\n=== CADASTRO DE USUÁRIO ===")

    # Nome (obrigatório, mínimo 3 caracteres)
    nome_valido = False
    while not nome_valido:
        nome = input("Nome completo: ").strip()
        if len(nome) >= 3:
            nome_valido = True
        else:
            print("ERRO! Nome deve ter ao menos 3 letras e não pode conter algarismos ou caracteres especiais.")

    # E-mail
    email_valido = False
    while not email_valido:
        email = input("E-mail: ").strip().lower()
        if not _validar_email(email):
            print("ERRO! Formato inválido.")
        elif email_ja_cadastrado(conexao, email):
            print("ERRO! E-mail já cadastrado.")
        else:
            email_valido = True
 
    # Senha
    senha_valida = False
    while not senha_valida:
        senha = input("Senha (mínimo 6 caracteres): ").strip()
        if len(senha) >= 6:
            senha_valida = True
        else:
            print("ERRO! A senha deve ter ao menos 6 caracteres.")

    # DEPARTAMENTOS
    print("\nDepartamentos disponíveis:")
    print("  1 - TI")
    print("  2 - RH")
    print("  3 - Financeiro")

    depto_valido = False
    while not depto_valido:
        id_depto = input("ID do Departamento: ").strip()
        if id_depto not in ("1", "2", "3"):
            print("ERRO! Opção inválida. Digite 1, 2 ou 3.")
        else:
            depto_valido = True

    # PERFIL
    print("\nPerfil:")
    print("  1 - Usuário")
    print("  2 - Técnico")

    perfil_valido = False
    while not perfil_valido:
        perfil_op = input("Escolha o perfil: ").strip()
        if perfil_op == "1":
            perfil = "cliente"
            perfil_valido = True
        elif perfil_op == "2":
            perfil = "tecnico"
            perfil_valido = True
        else:   
            print("ERRO! Digite 1 ou 2.")

    cursor = conexao.cursor()
    try:
        sql = "INSERT INTO Usuario (nome, email, senha, id_depto, tipo_perfil) VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(sql, (nome, email, senha, int(id_depto), perfil))
        conexao.commit()
        print(f"\nUsuário '{nome}' cadastrado com sucesso! ID: {cursor.lastrowid}")
    except Exception as e:
        print(f"Erro ao cadastrar: {e}")
    finally:
        cursor.close()

def listar_usuarios(conexao):
    # Retorna lista com todos os usuários cadastrados PARA ABRIR CHAMADOS
    cursor = conexao.cursor(dictionary=True)
    cursor.execute("""
        SELECT u.id_usuario, u.nome, u.email, u.tipo_perfil, d.nome_depto AS departamento
        FROM Usuario u
        LEFT JOIN Departamento d ON u.id_depto = d.id_depto
        ORDER BY u.nome
    """)
    usuarios = cursor.fetchall()
    cursor.close()
    return usuarios

def exibir_usuarios(conexao):
    # Exibe a lista de usuários formatada na tela
    print("\n=== USUÁRIOS CADASTRADOS ===")
    usuarios = listar_usuarios(conexao)

    if not usuarios:
        print("Nenhum usuário cadastrado ainda.")
        input("\n[Enter] para voltar...")
        return

    print(f"{'ID':<5} {'Nome':<25} {'E-mail':<30} {'Perfil':<10} {'Depto'}")
    print("-" * 80)
    for u in usuarios:
        print(f"{u['id_usuario']:<5} {u['nome']:<25} {u['email']:<30} "
              f"{u['tipo_perfil']:<10} {u['departamento'] or '-'}")

    input("\n[Enter] para voltar...")