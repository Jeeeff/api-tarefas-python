from flask import Flask
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from app.config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    # Inicializar extensões
    JWTManager(app)
    CORS(app)
    
    # Registrar rotas
    from app.routes.auth import auth_bp
    from app.routes.tasks import tasks_bp
    
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(tasks_bp, url_prefix='/tasks')
    
    # Rota raiz
    @app.route('/')
    def index():
        return {
            'message': 'API de Gerenciamento de Tarefas',
            'version': '1.0',
            'endpoints': {
                'auth': '/auth/register, /auth/login',
                'tasks': '/tasks/ (GET, POST, PUT, DELETE)'
            }
        }
    
    return app
