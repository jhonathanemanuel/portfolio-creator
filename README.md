# Criador de portfolio (portfolio-creator)

## Instalação e Execução

Siga os passos abaixo para configurar o projeto:

### 1. Ambiente Virtual
```bash
python -m venv venv
```

### 2. Ativação 

Windows:
```bash 
.\venv\Scripts\activate
```
Linux/Mac:
```bash 
source venv/bin/activate
```

### 3. Dependências
```bash 
pip install -r requirements.txt
```

### 4. Banco de Dados
O projeto usa PostgreSQL por padrão. Caso queira usar SQLite, altere o DATABASES no settings.py.

### 5. Migrações e Execução
```bash 
python manage.py migrate
python manage.py runserver
```