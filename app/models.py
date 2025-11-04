import json
import os
from datetime import datetime

USERS_FILE = 'users.json'
TASKS_FILE = 'tasks.json'

# === FUNÇÕES AUXILIARES ===

def load_json(filename):
    """Carrega dados de um arquivo JSON"""
    if not os.path.exists(filename):
        return []
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            return json.load(f)
    except json.JSONDecodeError:
        return []

def save_json(filename, data):
    """Salva dados em um arquivo JSON"""
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

# === USUÁRIOS ===

def get_all_users():
    """Retorna todos os usuários"""
    return load_json(USERS_FILE)

def get_user_by_email(email):
    """Busca usuário por email"""
    users = get_all_users()
    return next((u for u in users if u['email'] == email), None)

def get_user_by_id(user_id):
    """Busca usuário por ID"""
    users = get_all_users()
    return next((u for u in users if u['id'] == user_id), None)

def create_user(email, password_hash):
    """Cria um novo usuário"""
    users = get_all_users()
    new_user = {
        'id': len(users) + 1,
        'email': email,
        'password': password_hash,
        'created_at': datetime.utcnow().isoformat()
    }
    users.append(new_user)
    save_json(USERS_FILE, users)
    return new_user

# === TAREFAS ===

def get_all_tasks():
    """Retorna todas as tarefas"""
    return load_json(TASKS_FILE)

def get_tasks_by_user(user_id):
    """Retorna tarefas de um usuário específico"""
    tasks = get_all_tasks()
    return [t for t in tasks if t['user_id'] == user_id]

def get_task_by_id(task_id, user_id):
    """Busca uma tarefa específica do usuário"""
    tasks = get_all_tasks()
    return next((t for t in tasks if t['id'] == task_id and t['user_id'] == user_id), None)

def create_task(user_id, title, description=''):
    """Cria uma nova tarefa"""
    tasks = get_all_tasks()
    new_task = {
        'id': len(tasks) + 1,
        'user_id': user_id,
        'title': title,
        'description': description,
        'completed': False,
        'created_at': datetime.utcnow().isoformat()
    }
    tasks.append(new_task)
    save_json(TASKS_FILE, tasks)
    return new_task

def update_task(task_id, user_id, updates):
    """Atualiza uma tarefa existente"""
    tasks = get_all_tasks()
    for task in tasks:
        if task['id'] == task_id and task['user_id'] == user_id:
            task.update(updates)
            task['updated_at'] = datetime.utcnow().isoformat()
            save_json(TASKS_FILE, tasks)
            return task
    return None

def delete_task(task_id, user_id):
    """Deleta uma tarefa"""
    tasks = get_all_tasks()
    updated_tasks = [t for t in tasks if not (t['id'] == task_id and t['user_id'] == user_id)]
    if len(updated_tasks) < len(tasks):
        save_json(TASKS_FILE, updated_tasks)
        return True
    return False
