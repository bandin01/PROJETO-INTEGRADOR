-- ===========================================
--  DADOS DE EXEMPLO — Sistema de Chamados
--  Execute após criar_banco.sql
-- ===========================================

USE SuporteTI;

-- -------------------------------------------
--  Departamentos
-- -------------------------------------------
INSERT INTO Departamento (nome_depto) VALUES
    ('TI'),
    ('RH'),
    ('Financeiro');

-- -------------------------------------------
--  Usuários
-- -------------------------------------------
INSERT INTO Usuario (nome, email, senha, id_depto, tipo_perfil) VALUES
    ('Carlos Silva',   'carlos@empresa.com',  'senha123', 1, 'tecnico'),
    ('Ana Souza',      'ana@empresa.com',     'senha123', 2, 'cliente'),
    ('Pedro Lima',     'pedro@empresa.com',   'senha123', 3, 'cliente'),
    ('Julia Mendes',   'julia@empresa.com',   'senha123', 1, 'tecnico'),
    ('Roberto Costa',  'roberto@empresa.com', 'senha123', 2, 'cliente');

-- -------------------------------------------
--  Chamados
-- -------------------------------------------
INSERT INTO Chamado (titulo, descricao, prioridade, status, id_solicitante, id_tecnico) VALUES
    (
        'Computador não liga',
        'O computador do setor financeiro não está ligando desde ontem de manhã.',
        'alta',
        'aberto',
        2,
        NULL
    ),
    (
        'Sem acesso ao sistema',
        'Não consigo acessar o sistema de RH após troca de senha.',
        'media',
        'em_atendimento',
        3,
        1
    ),
    (
        'Impressora offline',
        'A impressora do corredor está aparecendo como offline para todos do setor.',
        'media',
        'em_atendimento',
        5,
        4
    ),
    (
        'Atualização de cadastro',
        'Preciso atualizar meu e-mail no sistema interno.',
        'baixa',
        'concluido',
        2,
        1
    ),
    (
        'Internet lenta',
        'A conexão com a internet está muito lenta no setor financeiro desde esta manhã.',
        'alta',
        'aberto',
        3,
        NULL
    );
