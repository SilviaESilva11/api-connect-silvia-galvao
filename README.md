# API Connect - Silvia Galvão

API RESTful desenvolvida em Python com Flask para gerenciamento completo de usuários (CRUD), oferecendo rotas modulares via Blueprint, suporte a persistência com Flask-SQLAlchemy e validações estritas de integridade com respostas padronizadas em códigos HTTP.

## ?? Objetivo da API

O objetivo desta API é fornecer uma interface leve, previsível e intuitiva para operações de CRUD de usuários, demonstrando a aplicação prática dos status HTTP (200 OK, 201 Created, 400 Bad Request e 404 Not Found) e validações essenciais no ciclo de vida dos dados (como verificação de e-mail único e dados obrigatórios).

## ??? Tecnologias Utilizadas

* **Linguagem:** Python 3.10+
* **Framework Web:** Flask
* **ORM / Banco de Dados:** Flask-SQLAlchemy (SQLite)
* **Testes Automáticos:** Pytest e Pytest-Cov
* **IDE Recomendada:** PyCharm

## ?? Passo a Passo para Execução Local

### Pré-requisitos

* Python 3.10 ou superior instalado.
* Git instalado.

### 1. Clonar o Repositório

```bash
git clone https://github.com/SilviaESilva11/api-connect-silvia-galvao.git
cd api-connect-silvia-galvao
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
python app.py
pytest
pytest --cov=app
```
