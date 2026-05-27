Sistema de Chamados — Projeto Integrador I

Sistema interno de controle de chamados de suporte de TI, desenvolvido em Python com banco de dados MySQL. Permite registrar usuários, abrir chamados, acompanhar status e visualizar estatísticas.


INTEGRANTES

Davi Bandin — github.com/bandin01
Lucas Nascimento — github.com/lucass-nasc
Miguel Trentini — github.com/MiguelTTortella
Vitor Furlan — github.com/vtr1812


REQUISITOS

- Python 3.10 ou superior
- MySQL 8.x
- VPN Fortinet da faculdade ativa
- Bibliotecas Python: mysql-connector-python e python-dotenv


CONEXÃO VPN

O banco de dados está hospedado no servidor da faculdade. É obrigatório estar conectado à VPN Fortinet antes de executar o sistema.

Como conectar:
1. Abra o cliente FortiClient VPN
2. Insira o endereço do servidor VPN fornecido pela faculdade
3. Digite seu usuário e senha institucionais
4. Clique em Conectar e aguarde a confirmação

Após conectado, o servidor do banco estará acessível no endereço 172.16.12.14.


INSTALAÇÃO

1. Clone o repositório

    git clone https://github.com/seu-repositorio/sistema-chamados.git
    cd sistema-chamados

2. Instale as dependências

    pip install mysql-connector-python python-dotenv

3. Configure o arquivo .env

Crie um arquivo .env na raiz do projeto com as credenciais do banco:

    DB_HOST=172.16.12.14
    DB_USER=seu-usuario
    DB_PASS=sua-senha
    DB_NAME=SuporteTI

O arquivo .env não é enviado ao GitHub por segurança. Solicite as credenciais com o docente ou com o responsável pelo banco.

4. Crie o banco de dados

Com a VPN ativa, execute o script SQL:

    mysql -h 172.16.12.14 -u seu-usuario -p < sql/criar_banco.sql

Ou abra o arquivo sql/criar_banco.sql diretamente no MySQL Workbench e execute.


COMO EXECUTAR

Com a VPN ativa, rode:

    python main.py

O menu principal será exibido no terminal com as opções disponíveis.


FUNCIONALIDADES

- Cadastro de usuários com validação de e-mail único
- Listagem de usuários cadastrados
- Abertura de chamados com prioridade calculada automaticamente
- Listagem de chamados
- Atualização de status com regra de integridade
- Estatísticas por status e por prioridade


REGRA DE PRIORIDADE

A prioridade é calculada automaticamente no momento da abertura do chamado, com base em dois fatores informados pelo usuário:

- Urgência — nível de urgência do problema (1 a 3)
- Impacto — abrangência do impacto (1 a 3)

Soma (urgência + impacto) | Prioridade
2 ou 3                    | Baixa
4                         | Média
5 ou 6                    | Alta

A regra é determinística: as mesmas entradas sempre resultam na mesma prioridade.


REGRA DE TRANSIÇÃO DE STATUS

Os status válidos são: aberto, em atendimento e concluido.


MODELAGEM DO BANCO DE DADOS

O banco possui três tabelas:

- Departamento — armazena os departamentos da organização.
- Usuario — armazena os usuários do sistema (clientes e técnicos), vinculados a um departamento.
- Chamado — armazena os chamados abertos pelos clientes, com prioridade calculada automaticamente e status atualizado pelos técnicos.

Relacionamentos:
- Usuario referencia Departamento (cada usuário pertence a um departamento)
- Chamado referencia Usuario duas vezes: uma para o solicitante e outra para o técnico responsável

O MER completo está disponível em docs/MER.png.


ESTRUTURA DE PASTAS

sistema-chamados/
    main.py            Ponto de entrada e menu principal
    usuarios.py        Cadastro, listagem e seleção de usuários
    chamados.py        Abertura, listagem e atualização de chamados
    database.py        Conexão com o banco de dados
    .env               Credenciais do banco — NÃO sobe ao GitHub, deve ser criado manualmente
    .gitignore         Impede o .env de ser enviado ao GitHub
    requirements.txt
    README.md
    sql/
        criar_banco.sql
        dados_exemplo.sql
    docs/
        MER.png        Modelo Entidade-Relacionamento


OBSERVAÇÕES

- A interface é via terminal (CLI)
- O sistema foi desenvolvido e testado no Windows com Python 3.11
- É necessário que a VPN da faculdade esteja ativa antes de executar o programa
