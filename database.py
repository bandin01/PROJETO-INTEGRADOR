import mysql.connector
import os
from dotenv import load_dotenv

# Carrega as variáveis do arquivo .env [cite: 180]
load_dotenv()

def criar_conexao():
    try:
        # Busca as informações de forma segura 
        conexao = mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASS"),
            database=os.getenv("DB_NAME")
        )
        if conexao.is_connected():
            print("Conexão ao MySQL realizada com sucesso!")
            return conexao
    except Exception as e:
        print(f"Erro ao conectar: {e}")
        return None

# Teste rápido
if __name__ == "__main__":  
    criar_conexao()