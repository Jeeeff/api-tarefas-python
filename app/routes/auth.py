from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token
from app.models import get_user_by_email, create_user
from app.utils import hash_password, verify_password

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['POST'])
def register():
    """Registra um novo usuário"""
    data = request.get_json()
    
    if not data:
        return jsonify({'error': 'Nenhum dado fornecido'}), 400
    
    email = data.get('email')
    password = data.get('password')
    
    # Validações
    if not email or not password:
        return jsonify({'error': 'Email e senha são obrigatórios'}), 400
    
    if len(password) < 6:
        return jsonify({'error': 'A senha deve ter no mínimo 6 caracteres'}), 400
    
    # Verifica se usuário já existe
    if get_user_by_email(email):
        return jsonify({'error': 'Usuário já existe'}), 409
    
    # Cria o usuário
    password_hash = hash_password(password)
    user = create_user(email, password_hash)
    
    return jsonify({
        'message': 'Usuário criado com sucesso',
        'user': {
            'id': user['id'],
            'email': user['email'],
            'created_at': user['created_at']
        }
    }), 201

@auth_bp.route('/login', methods=['POST'])
def login():
    """Realiza login e retorna token JWT"""
    data = request.get_json()
    
    if not data:
        return jsonify({'error': 'Nenhum dado fornecido'}), 400
    
    email = data.get('email')
    password = data.get('password')
    
    if not email or not password:
        return jsonify({'error': 'Email e senha são obrigatórios'}), 400
    
    # Busca usuário
    user = get_user_by_email(email)
    
    if not user or not verify_password(password, user['password']):
        return jsonify({'error': 'Credenciais inválidas'}), 401
    
    # Gera token JWT
    access_token = create_access_token(identity=str(user['id']))
    
    return jsonify({
        'message': 'Login realizado com sucesso',
        'access_token': access_token,
        'user': {
            'id': user['id'],
            'email': user['email']
        }
    }), 200
