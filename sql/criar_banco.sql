CREATE DATABASE SuporteTI;
USE SuporteTI;

CREATE TABLE Departamento (
    id_depto INT AUTO_INCREMENT PRIMARY KEY,
    nome_depto VARCHAR(100) NOT NULL
);

CREATE TABLE Usuario (
    id_usuario INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(150) NOT NULL,
    email VARCHAR(150) UNIQUE NOT NULL,
    senha VARCHAR(255) NOT NULL,
    id_depto INT,
    tipo_perfil ENUM('cliente', 'tecnico') NOT NULL,
    CONSTRAINT fk_usuario_depto FOREIGN KEY (id_depto) REFERENCES Departamento(id_depto)
);

CREATE TABLE Chamado (
    id_chamado INT AUTO_INCREMENT PRIMARY KEY,
    titulo VARCHAR(200) NOT NULL,
    descricao TEXT NOT NULL,
    data_abertura DATETIME DEFAULT CURRENT_TIMESTAMP,
    prioridade ENUM('baixa', 'media', 'alta') NOT NULL,
    status ENUM('aberto', 'em_atendimento', 'concluido') DEFAULT 'aberto',
    id_solicitante INT NOT NULL,
    id_tecnico INT NULL,
    CONSTRAINT fk_chamado_solicitante FOREIGN KEY (id_solicitante) REFERENCES Usuario(id_usuario),
    CONSTRAINT fk_chamado_tecnico FOREIGN KEY (id_tecnico) REFERENCES Usuario(id_usuario)
);
