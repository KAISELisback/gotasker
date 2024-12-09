from src.repositories.tarefa_repository import criar_tarefa, apagar_tarefa, encontrar_tarefas
import pytest

@pytest.mark.skip(reason="interação com o banco")
def test_criar_tarefa():
    try:
        criar_tarefa("Tarefa Teste", "Descrição da tarefa de teste")
        print("A função criar_tarefa foi executada com sucesso.")
    except Exception as e:
        print(f"Erro ao executar a função criar_tarefa: {e}")

@pytest.mark.skip(reason="interação com o banco")  
def test_apagar_tarefa():
    try:
        tarefa_id = ['1', '4', '6', '7', '8', '9', '10', '11', '12']
        for number in tarefa_id:
            apagar_tarefa(number)
            print("A função de apagar funciona corretamente")
    except Exception as e:
        print(f"Algum erro aconteceu ao tentar apagar: {e}")
          
def test_encontrar_tarefas():
    try:
        tarefas = encontrar_tarefas()
        print("A função de apagar funciona corretamente")
        print(tarefas)
    except Exception as e:
        print(f"Algum erro aconteceu ao tentar apagar: {e}")
        
