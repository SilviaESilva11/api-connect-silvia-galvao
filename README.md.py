# API Connect - Silvia Galvão

API RESTful desenvolvida em Python com Flask para gerenciamento de usuários, oferecendo rotas para criação, listagem e busca individual, além de suporte a validações e tratamento de erros padronizados com códigos HTTP.

---

## 🚀 Objetivo da API

O objetivo desta API é fornecer uma interface leve e intuitiva para operações de CRUD de usuários, demonstrando a aplicação prática dos status HTTP (`200 OK`, `201 Created`, `400 Bad Request` e `404 Not Found`) e validações de dados recebidos via requisições JSON e query parameters.

---

## 🛠️ Tecnologias Utilizadas

* **Linguagem:** Python 3
* **Framework Web:** Flask
* **ORM / Banco de Dados:** Flask-SQLAlchemy (SQLite)
* **Testes Automáticos:** Pytest e Pytest-Cov
* **IDE Recomendada:** PyCharm

---

## ⚙️ Passo a Passo para Execução Local

### Pré-requisitos
* Python 3.10 ou superior instalado.
* Git instalado.

### 1. Clonar o Repositório
```bash
git clone [https://github.com/SilviaESilva11/api-connect-silvia-galvao.git](https://github.com/SilviaESilva11/api-connect-silvia-galvao.git)
cd api-connect-silvia-galvao
```

### 2. Criar e Ativar o Ambiente Virtual (`venv`)
* **Windows (PowerShell):**
  ```powershell
  python -m venv venv
  .\venv\Scripts\Activate.ps1
  ```
* **Linux / macOS:**
  ```bash
  python3 -m venv venv
  source venv/bin/activate
  ```

### 3. Instalar as Dependências
```bash
pip install flask flask-sqlalchemy pytest pytest-cov
```

### 4. Executar a Aplicação
```bash
python app.py
```
A aplicação estará disponível em `http://127.0.0.1:5000/`.

---

## 🧪 Execução dos Testes Automatizados

Para rodar a suíte de testes unitários e verificar a cobertura de código:

```bash
python -m pytest tests/test_users.py -v
```

---

## 📌 Endpoints da API

### 1. Leitura do Recurso Geral
Retorna a lista completa de usuários cadastrados.

* **Método:** `GET`
* **Rota:** `/users/`
* **Status HTTP:** `200 OK`
* **Exemplo de Resposta:**
  ```json
  {
    "status": "success",
    "total": 1,
    "data": [
      {
        "id": 1,
        "name": "Silvia Galvao",
        "email": "silvia@email.com"
      }
    ]
  }
  ```

---

### 2. Busca de Usuário por ID
Busca os detalhes de um usuário pelo seu ID numérico.

* **Método:** `GET`
* **Rota:** `/users/<id>`
* **Status HTTP Sucesso:** `200 OK`
* **Status HTTP Falha (ID inexistente):** `404 Not Found`
* **Exemplo de Resposta (404 Not Found):**
  ```json
  {
    "status": "error",
    "message": "Usuario nao encontrado."
  }
  ```

---

### 3. Criação Bem-sucedida de Usuário
Cria um novo usuário na base de dados (suporta dados via JSON `POST` ou parâmetros na URL `GET /users/create`).

* **Método:** `POST` ou `GET`
* **Rota:** `/users/` (POST) ou `/users/create?name=Ana&email=ana@email.com` (GET)
* **Status HTTP:** `201 Created`
* **Exemplo de Resposta:**
  ```json
  {
    "status": "success",
    "message": "Usuario criado com sucesso.",
    "data": {
      "id": 2,
      "name": "Ana",
      "email": "ana@email.com"
    }
  }
  ```

---

### 4. Falha na Criação (Campo 'email' Ausente)
Ocorre quando o campo obrigatório `email` não é informado na requisição.

* **Método:** `POST` ou `GET`
* **Rota:** `/users/` (POST) ou `/users/create?name=Ana` (GET)
* **Status HTTP:** `400 Bad Request`
* **Exemplo de Resposta:**
  ```json
  {
    "status": "error",
    "message": "O campo email e obrigatorio."
  }
  ```