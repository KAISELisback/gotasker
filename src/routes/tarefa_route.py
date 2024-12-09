from flask import Blueprint, request, render_template, flash, url_for, redirect
from src.controllers.tarefa_controller import TarefaController

tarefa_bp = Blueprint('tarefa_bp', __name__)

@tarefa_bp.route('/')
def inicio():
    return render_template('inicio.html')

@tarefa_bp.route('/minhas_tarefas')
def minhas_tarefas():
    tarefas = TarefaController.obter_tarefas_existentes()
    return render_template('tarefas.html', tarefas=tarefas)

@tarefa_bp.route('/nova_tarefa', methods=['GET', 'POST'])
def nova_tarefa():
    
    if request.method == 'POST':
        titulo = request.form.get('titulo')
        descricao = request.form.get('descricao')
        
        if titulo.strip() and descricao.strip():
            TarefaController.criar_nova_tarefa(titulo=titulo, descricao=descricao)
            flash("Tarefa adicionada!", "success")  
        else:
            flash("Preencha todos os campos do formulário", "danger")     
            
    return render_template('nova_tarefa.html')

@tarefa_bp.route('/<int:tarefa_id>/apagar_tarefa')
def apagar_tarefa(tarefa_id):
    TarefaController.apagar_tarefa_por_id(tarefa_id)
    return redirect(url_for('tarefa_bp.minhas_tarefas'))

@tarefa_bp.route('/<int:tarefa_id>/editar_tarefa', methods=['GET', 'POST'])
def editar_tarefa(tarefa_id):
    
    if request.method == 'POST':
        titulo = request.form.get('titulo')
        descricao = request.form.get('descricao')
        
        if titulo.strip() and descricao.strip():
            TarefaController.atualizar_tarefa_controller(tarefa_id=tarefa_id, titulo=titulo, descricao=descricao)
            flash("Tarefa atualizada!", "success")  
        else:
            flash("Preencha todos os campos do formulário", "danger") 
            
    tarefa = TarefaController.encontrar_tarefa_por_id_controller(tarefa_id=tarefa_id) 
    return render_template('editar_tarefa.html', tarefa=tarefa)