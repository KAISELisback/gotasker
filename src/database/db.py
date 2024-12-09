import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

def conectar_banco_de_dados():
    conexao = mysql.connector.connect(
        host=os.getenv('DB_HOST'),
        user=os.getenv('DB_USERNAME'),
        password=os.getenv('DB_PASSWORD'),
        database=os.getenv('DB_NAME'),
    )
    return conexao

def iniciar_banco_de_dados():
    db = conectar_banco_de_dados()
    cursor = db.cursor()
    cursor.execute("""
                   CREATE TABLE IF NOT EXISTS tarefas (
                       tarefa_id INT AUTO_INCREMENT PRIMARY KEY,
                       titulo VARCHAR(80) NOT NULL,
                       descricao VARCHAR(250) NOT NULL
                    )""")
    db.commit()
    cursor.close()
    db.close()