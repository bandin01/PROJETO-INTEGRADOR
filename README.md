 PROJETO-INTEGRADOR

SCSC - Sistema de Controle de Solicitações Corporativos:

Este é um sistema de chamados internos de TI desenvolvido como parte do Projeto Integrador do 1º Semestre do curso de Sistemas de Informação. O objetivo é gerenciar solicitações de suporte de forma organizada, utilizando uma interface de terminal em Python integrada a um banco de dados relacional MySQL.

O SCSC foi desenvolvido para facilitar o controle de solicitações corporativas dentro de uma empresa, sendo agora possível registrar, acompanhar e atualizar solicitações feitas por usuários da empresa.

O sistema busca aplicar conceitos de:
-Programação em Python.
-Banco de dados relacional.
-Integração entre Python e MySQL.
-CRUD (Create, Read, Update e Delete).
-Organização de sistemas.

FUNCIONALIDADES:

O sistema foi projetado para cobrir o ciclo de vida básico de um chamado de suporte:

  - Cadastrar Usuário: Registro de funcionários com vínculo a departamentos específicos.
  - Abrir Solicitação: Criação de chamados categorizados (Hardware, Software, etc.) com níveis de prioridade.
  - Ver Solicitações: Listagem de chamados para acompanhamento.
  - Atualizar Status: Controle do fluxo de trabalho (Aberto, Em Atendimento, Concluído).
  - Estatísticas: Visão geral de métricas, como total de chamados e volume por categoria.

REGRAS DE PRIORIDADE:

O sistema segue a seguinte ordem de prioridade:
1-Validar os dados informados pelo usuário
2-Garantir a conexão do banco de dados 
3-Executar operações no banco
4-Atualizar informações no sistema 
5-Exibir mensagens de sucesso ou de erro
6-Encerrar conexão corretamente 

DECISÕES DE MODELAGEM:

Banco de dados relacional: Foi utilizado o MySQL para organizar os dados.
Separação de responsabilidades: O projeto foi dividido em arquivos separados para (conexão com o banco de dados, funcionalidades do sistema e execução principal).
Controle de status: Os chamados possuem status padronizados (Aberto, Em atendimento e concluído)
 Tecnologias Utilizadas: Linguagem (Python), banco de dados (MySQL), biblioteca de integração(mysql-connector-python)

ESTRUTURA DO BANCO DE DADOS:

O projeto utiliza um modelo relacional para garantir a integridade dos dados:
  - Usuários: Armazena os dados de quem utiliza o sistema.
  - Solicitações: Registra os detalhes do problema, datas e status.
  - Departamentos: Tabela de referência para organizar a origem dos chamados.
  - Categorias: Classificação técnica dos problemas para geração de estatísticas.

REQUISITOS DE INSTALAÇÃO:
  - Python: 1-Baixar o instalador acessando (Python oficial)
            2-Executar o instalador e marcar a opção (Add Python to PATH)
            3-Fazer a instalação padrão
            4-Abrir o terminal e testar:
              print('hello world')

-MySQL: 1-Acessar o site (MySQL oficial)
        2-Baixar o MySQL server
        3-Durante a instalação:
          -Definir usuário e senha
          -Manter a porta padrão(3306) 
        4-Finalizar a instalação

-Biblioteca necessária: 1-Instalar a biblioteca de conexão:
                          -Abra o terminal e execute: pip install mysql-connector-python
                        2-Crie a pasta do projeto:
                          -Exemplo: PROJETO-INTEGRADOR/
                        3-Montar a estrutura do projeto:
                          -PROJETO-INTEGRADOR/
                          │
                          ├── main.py
                          │
                          ├── database/
                          │   └── conexao.py
                          │
                          └── banco/
                          └── script.sql
                         4-Criar o banco de dados no MySQL:
                           -Abra o MySQL e execute: CREATE DATABASE SCSC; 
                         5-Crie o arquivo de conexão:
                           -Crie: database/conexao.py
                         6-Importar a biblioteca: import mysql.connector
                         7-Faça a conexão:
                           -Adicione: conexao = mysql.connector.connect(
                                          host="localhost",
                                          user="root",
                                          password="SUA_SENHA",
                                          database="scsc"
                                      )
                         8-Adicionar teste de conexão:
                           -Código completo conexão.py:import mysql.connector

                                                       conexao = mysql.connector.connect(
                                                           host="localhost",
                                                           user="root",
                                                           password="SUA_SENHA",
                                                           database="scsc"
                                                       )

                           
                                                       print("Conexão realizada com sucesso!")
                         9-Crie o main.py 
                         10-Importe a conexão:
                            -Dentro do main.py: from database.conexao import conexao

                                                print("Sistema funcionando!")
                         11-Execute o sistema:
                            -Abra o terminal na pasta do projeto e execute: python main.py
                         12- resultado esperado: Conexão realizada com sucesso!
                                                 Sistema funcionando!
                         13-Feche a conexão:
                            -No final do main.py: conexão.close()
                         14-Código final do main.py: from database.conexao import conexao

                                                     print("Sistema funcionando!")

                                                     conexao.close()

ESTRUTURA DE PASTAS E ARQUIVOS: ## Estrutura de Pastas

```
sistema-chamados/
├── main.py          # Ponto de entrada e menu principal
├── usuarios.py      # Cadastro, listagem e seleção de usuários
├── chamados.py      # Abertura, listagem e atualização de chamados
├── database.py      # Conexão com o banco de dados
├── requirements.txt
├── README.md
├── sql/
│   ├── criar_banco.sql   # DDL — criação das tabelas
│   └── dados_exemplo.sql # DML — dados de teste
└── docs/
    └── MER.png           # Modelo Entidade-Relacionamento
```



INTEGRANTES DO GRUPO: Vitor Martins Furlan, Lucas Dos Santos Nascimento, Marcos José Davila Netto, Miguel Trentini Tortella, Davi Silveira Leite Bandin.
