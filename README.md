🚀 API de Gerenciamento de Tarefas
API RESTful completa para gerenciamento de tarefas com autenticação JWT, desenvolvida com Python + Flask.

Python

Flask

JWT

Status

✨ Funcionalidades
🔐 Autenticação JWT (registro e login)
📝 CRUD completo de tarefas (Create, Read, Update, Delete)
🛡️ Rotas protegidas por token
💾 Persistência de dados em JSON
📱 CORS habilitado para integração com front-end
🧪 Validação de dados e tratamento de erros
🛠️ Tecnologias Utilizadas
Python 3.10+
Flask (framework web)
Flask-JWT-Extended (autenticação JWT)
Flask-CORS (suporte a requisições cross-origin)
python-dotenv (variáveis de ambiente)
🚀 Como Usar
1. Clonar o repositório
bash
Copiar

git clone https://github.com/SEU_USUARIO/api-tarefas-python.git
cd api-tarefas-python
2. Criar ambiente virtual
Windows (CMD):

cmd
Copiar

python -m venv venv
venv\Scripts\activate
Windows (PowerShell):

powershell
Copiar

python -m venv venv
.\venv\Scripts\Activate.ps1
Linux/Mac:

bash
Copiar

python3 -m venv venv
source venv/bin/activate
3. Instalar dependências
bash
Copiar

pip install -r requirements.txt
4. Configurar variáveis de ambiente
Crie um arquivo .env na raiz:

env
Copiar

SECRET_KEY=sua-chave-secreta-super-segura-aqui-123456
JWT_SECRET_KEY=outra-chave-secreta-para-jwt-987654
5. Rodar a API
bash
Copiar

python run.py
A API estará disponível em: http://127.0.0.1:5000

📋 Endpoints
Autenticação
Método	Endpoint	Descrição	Autenticação
POST	/auth/register	Registrar novo usuário	❌
POST	/auth/login	Fazer login e obter token	❌

Exportar

Copiar
Tarefas
Método	Endpoint	Descrição	Autenticação
GET	/tasks/	Listar todas as tarefas	✅
POST	/tasks/	Criar nova tarefa	✅
GET	/tasks/{id}	Buscar tarefa específica	✅
PUT	/tasks/{id}	Atualizar tarefa	✅
DELETE	/tasks/{id}	Deletar tarefa	✅

Exportar

Copiar
🔐 Autenticação
Todos os endpoints de tarefas requerem o header:

Authorization: Bearer SEU_TOKEN_JWT

🧪 Exemplos de Uso (PowerShell)
1. Registrar usuário
powershell
Copiar

Invoke-WebRequest -Uri "http://127.0.0.1:5000/auth/register" `
  -Method POST `
  -Headers @{"Content-Type"="application/json"} `
  -Body '{"email":"user@example.com","password":"senha123"}'
2. Fazer login
powershell
Copiar

$response = Invoke-WebRequest -Uri "http://127.0.0.1:5000/auth/login" `
  -Method POST `
  -Headers @{"Content-Type"="application/json"} `
  -Body '{"email":"user@example.com","password":"senha123"}'
$token = ($response.Content | ConvertFrom-Json).access_token
3. Criar tarefa
powershell
Copiar

Invoke-WebRequest -Uri "http://127.0.0.1:5000/tasks/" `
  -Method POST `
  -Headers @{"Content-Type"="application/json"; "Authorization"="Bearer $token"} `
  -Body '{"title":"Minha tarefa","description":"Descrição"}'
4. Listar tarefas
powershell
Copiar

Invoke-WebRequest -Uri "http://127.0.0.1:5000/tasks/" `
  -Method GET `
  -Headers @{"Authorization"="Bearer $token"}
📁 Estrutura do Projeto
api-tarefas-python/

├── app/

│ ├── init.py # Inicialização do Flask

│ ├── config.py # Configurações

│ ├── models.py # Modelos de dados (JSON)

│ ├── utils.py # Funções auxiliares

│ └── routes/ # Rotas da API

│ ├── init.py

│ ├── auth.py # Rotas de autenticação

│ └── tasks.py # Rotas de tarefas

├── venv/ # Ambiente virtual (não commitado)

├── .env # Variáveis de ambiente (não commitado)

├── .gitignore # Arquivos ignorados pelo Git

├── requirements.txt # Dependências do projeto

├── run.py # Arquivo principal

└── README.md # Documentação

🔮 Próximos Passos
[ ] Migrar para PostgreSQL com SQLAlchemy
[ ] Adicionar validação avançada com Marshmallow
[ ] Implementar paginação e filtros
[ ] Adicionar testes unitários com pytest
[ ] Deploy em Render, Railway ou Heroku
[ ] Documentação Swagger/OpenAPI
📸 Screenshots
Endpoint raiz
API Root

Criação de tarefa
Create Task

Lista de tarefas
List Tasks

📞 Contato
Desenvolvido por Jefferson

📧 Email: jefferson@email.com

💼 LinkedIn: linkedin.com/in/jefferson

🐙 GitHub: github.com/jefferson

⭐ Se este projeto foi útil, deixe uma estrela no GitHub!