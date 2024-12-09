from src.models.tarefa_model import AtributosTarefa
from src.repositories.tarefa_repository import encontrar_tarefas, criar_tarefa, atualizar_tarefa, apagar_tarefa, encontrar_tarefa_por_id

class TarefaController:
    
    @staticmethod
    def criar_nova_tarefa(titulo: str, descricao: str):
            try:
                tarefa = AtributosTarefa(titulo=titulo, descricao=descricao)
                criar_tarefa(tarefa.titulo, tarefa.descricao)
            except Exception as exception:
                print(f"Ocorreu um erro ao validar os dados da tarefas: {exception}")

    @staticmethod
    def apagar_tarefa_por_id(tarefa_id: int):
        apagar_tarefa(tarefa_id)
        
    @staticmethod
    def atualizar_tarefa_controller(tarefa_id: int, titulo: str, descricao: str):
        try:
            tarefa = AtributosTarefa(titulo=titulo, descricao=descricao)
            atualizar_tarefa(tarefa_id=tarefa_id, titulo=tarefa.titulo, descricao=tarefa.descricao)
        except Exception as exception:
            print(f"Ocorreu um erro ao validar os dados da tarefas: {exception}")
            
    def encontrar_tarefa_por_id_controller(tarefa_id):
        tarefa = encontrar_tarefa_por_id(tarefa_id=tarefa_id)
        return tarefa
    
    @staticmethod
    def obter_tarefas_existentes():
            tarefas_db = encontrar_tarefas()
            tarefas = [AtributosTarefa(**tarefa) for tarefa in tarefas_db]
            return tarefas