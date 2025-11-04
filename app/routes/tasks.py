from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.models import (
    get_tasks_by_user, 
    get_task_by_id, 
    create_task, 
    update_task, 
    delete_task
)

tasks_bp = Blueprint('tasks', __name__)

@tasks_bp.route('/', methods=['GET'])
@jwt_required()
def get_tasks():
    """Lista todas as tarefas do usuário autenticado"""
    print("🔵 GET /tasks/ - Iniciando...")
    try:
        user_id = get_jwt_identity()
        print(f"🔵 User ID obtido: {user_id} (tipo: {type(user_id).__name__})")
        tasks = get_tasks_by_user(user_id)
        print(f"🔵 Tarefas encontradas: {len(tasks)}")
        
        return jsonify({
            'total': len(tasks),
            'tasks': tasks
        }), 200
    except Exception as e:
        print(f"❌ Erro em GET /tasks/: {e}")
        return jsonify({'error': str(e)}), 500

@tasks_bp.route('/', methods=['POST'])
@jwt_required()
def add_task():
    """Cria uma nova tarefa"""
    print("🟢 POST /tasks/ - Iniciando...")
    try:
        user_id = get_jwt_identity()
        print(f"🟢 User ID obtido: {user_id} (tipo: {type(user_id).__name__})")
        
        data = request.get_json()
        print(f"🟢 Dados recebidos: {data}")
        
        if not data:
            print("❌ Nenhum dado fornecido")
            return jsonify({'error': 'Nenhum dado fornecido'}), 400
        
        title = data.get('title')
        description = data.get('description', '')
        print(f"🟢 Title: {title}, Description: {description}")
        
        if not title:
            print("❌ Título não fornecido")
            return jsonify({'error': 'Título é obrigatório'}), 400
        
        print(f"🟢 Chamando create_task({user_id}, {title}, {description})")
        task = create_task(user_id, title, description)
        print(f"🟢 Tarefa criada com sucesso: {task}")
        
        return jsonify({
            'message': 'Tarefa criada com sucesso',
            'task': task
        }), 201
    except Exception as e:
        print(f"❌ ERRO CRÍTICO em POST /tasks/: {type(e).__name__}: {e}")
        import traceback
        traceback.print_exc()
        return jsonify({'error': str(e)}), 500

@tasks_bp.route('/<int:task_id>', methods=['GET'])
@jwt_required()
def get_task(task_id):
    """Busca uma tarefa específica"""
    print(f"🔵 GET /tasks/{task_id} - Iniciando...")
    try:
        user_id = get_jwt_identity()
        task = get_task_by_id(task_id, user_id)
        
        if not task:
            return jsonify({'error': 'Tarefa não encontrada'}), 404
        
        return jsonify({'task': task}), 200
    except Exception as e:
        print(f"❌ Erro em GET /tasks/{task_id}: {e}")
        return jsonify({'error': str(e)}), 500

@tasks_bp.route('/<int:task_id>', methods=['PUT'])
@jwt_required()
def edit_task(task_id):
    """Atualiza uma tarefa existente"""
    print(f"🟡 PUT /tasks/{task_id} - Iniciando...")
    try:
        user_id = get_jwt_identity()
        data = request.get_json()
        
        if not data:
            return jsonify({'error': 'Nenhum dado fornecido'}), 400
        
        task = update_task(task_id, user_id, data)
        
        if not task:
            return jsonify({'error': 'Tarefa não encontrada'}), 404
        
        return jsonify({
            'message': 'Tarefa atualizada com sucesso',
            'task': task
        }), 200
    except Exception as e:
        print(f"❌ Erro em PUT /tasks/{task_id}: {e}")
        return jsonify({'error': str(e)}), 500

@tasks_bp.route('/<int:task_id>', methods=['DELETE'])
@jwt_required()
def remove_task(task_id):
    """Deleta uma tarefa"""
    print(f"🔴 DELETE /tasks/{task_id} - Iniciando...")
    try:
        user_id = get_jwt_identity()
        
        if delete_task(task_id, user_id):
            return jsonify({'message': 'Tarefa deletada com sucesso'}), 200
        
        return jsonify({'error': 'Tarefa não encontrada'}), 404
    except Exception as e:
        print(f"❌ Erro em DELETE /tasks/{task_id}: {e}")
        return jsonify({'error': str(e)}), 500
