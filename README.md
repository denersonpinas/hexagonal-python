# hexagonal-python

## Instruções para Configuração e Execução do Aplicativo

### Configuração do Ambiente Virtual

Crie um ambiente virtual utilizando o comando: 
   
```bash
python3 -m venv venv
```

### Ativação do Ambiente Virtual

Ative o ambiente virtual (se criado) usando o comando: 

```bash
source venv/bin/activate
```

### Desativação do Ambiente Virtual

Desative o ambiente virtual (se criado) usando o comando:

```bash
deactivate
```

### Instalação das Dependências

Instale as bibliotecas necessárias executando o comando: 

```bash
python3 -m pip install -r requirements.txt
pre-commit install
```

### Inicialização Docker

#### pofile: local

```bash
sudo docker compose up
```

#### pofile: prod

```bash
sudo docker compose --profile prod up
```

### Dados de conexão com o Postgress
```bash
DB_USER = "postgres"
DB_PASSWORD = "postgres"
DB_HOST = "localhost"
DB_PORT = "3006"
DB_NAME = "app_bank"
```

### Criação do Banco de Dados

```bash
python3
from src.infra.config import *
db_conn = DBConnectionHandler()
engine = db_conn.get_engine()
Base.metadata.create_all(engine)
```

