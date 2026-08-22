# API Connect - Silvia Galvao

API RESTful para gerenciamento de usuarios construida em Python utilizando o framework Flask, com persistencia na camada de modelo e suite de testes unitarios automatizados com Pytest.

---

## Tecnologias Utilizadas

- Python 3.14+
- Flask (Framework Web)
- Pytest (Testes unitarios)
- Pytest-Cov (Analise de cobertura de testes)

---

## Como Executar o Projeto

### 1. Clonar o repositorio
git clone https://github.com/SilviaESilva11/api-connect-silvia-galvao.git

### 2. Acessar a pasta do projeto
cd api-connect-silvia-galvao

### 3. Criar e ativar o ambiente virtual (venv)
python -m venv venv
.\venv\Scripts\Activate.ps1

### 4. Instalar as dependencias
pip install -r requirements.txt

### 5. Executar a aplicacao Flask
python app.py

---

## Como Rodar os Testes

Para executar a suite completa de testes unitarios:
python -m pytest

Para rodar os testes gerando o relatorio de cobertura:
python -m pytest --cov=src

---

## Endpoints da API (/users)

| Metodo | Endpoint | Descricao | Status Esperado |
| --- | --- | --- | --- |
| GET | /users | Lista todos os usuarios cadastrados | 200 OK |
| POST | /users | Cadastra um novo usuario (name, email) | 201 Created |
| GET | /users/<id> | Busca um usuario especifico pelo ID | 200 OK / 404 Not Found |
| PUT | /users/<id> | Atualiza dados do usuario (name, email) | 200 OK / 400 Bad Request |
| DELETE | /users/<id> | Remove um usuario pelo ID | 200 OK / 404 Not Found |
