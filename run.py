from app import create_app
import os

app = create_app()

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    print(f'🚀 API de Tarefas rodando em http://0.0.0.0:{port}')
    print('📚 Documentação: http://0.0.0.0:{port}/')
    app.run(debug=False, host='0.0.0.0', port=port)
