# Criador de portfolio (portfolio-creator)

## Instalação e Execução

Siga os passos abaixo para configurar o projeto:

### 1. Clonar o Repositório
Abra o terminal na pasta onde deseja salvar o projeto e execute o comando abaixo:
```bash
git clone https://github.com/jhonathanemanuel/portfolio-creator.git
```

### 2. Acessar a Pasta do Projeto
Navegue para dentro do diretório que o Git acabou de criar:
```bash
cd portfolio_creator
```

### 3. Ambiente Virtual
```bash
python -m venv venv
```

### 4. Ativação 

Windows:
```bash 
.\venv\Scripts\activate
```
Linux/Mac:
```bash 
source venv/bin/activate
```

### 5. Dependências
```bash 
pip install -r requirements.txt
```

### 6. Banco de Dados
O projeto usa PostgreSQL por padrão. Caso queira usar SQLite, altere o DATABASES no settings.py.

### 7. Migrações e Execução
```bash 
python manage.py migrate
python manage.py runserver
```