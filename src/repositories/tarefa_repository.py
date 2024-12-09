from src.database.db import conectar_banco_de_dados
from src.models.tarefa_model import AtributosTarefa

# CRIAR
def criar_tarefa(titulo ,descricao):
    db = conectar_banco_de_dados()
    cursor = db.cursor()
    cursor.execute("INSERT INTO tarefas (titulo, descricao) VALUES (%s, %s)", (titulo, descricao))
    db.commit()
    cursor.close()
    db.close()
    
# APAGAR
def apagar_tarefa(tarefa_id):
    db = conectar_banco_de_dados()
    cursor = db.cursor()
    cursor.execute("DELETE FROM tarefas WHERE tarefa_id = %s", (tarefa_id,))
    db.commit()
    cursor.close()
    db.close()
    
# ATUALIZAR
def atualizar_tarefa(tarefa_id, titulo, descricao):
    db = conectar_banco_de_dados()
    cursor = db.cursor()
    cursor.execute("UPDATE tarefas SET titulo = %s, descricao = %s WHERE tarefa_id = %s", (titulo, descricao, tarefa_id))
    db.commit()
    cursor.close()
    db.close()

# LER
def encontrar_tarefas():
    db = conectar_banco_de_dados()
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT tarefa_id, titulo, descricao FROM tarefas")
    tarefas_db = cursor.fetchall()
    cursor.close()
    db.close()
    
    return tarefas_db

def encontrar_tarefa_por_id(tarefa_id):
    db = conectar_banco_de_dados()
    cursor = db.cursor(dictionary=True)
    
    # Consulta filtrando pelo ID da tarefa
    cursor.execute("SELECT tarefa_id, titulo, descricao FROM tarefas WHERE tarefa_id = %s", (tarefa_id,))
    tarefa_db = cursor.fetchone()  # Usando fetchone para retornar uma única tarefa
    
    cursor.close()
    db.close()
    
    return tarefa_db
   

    
