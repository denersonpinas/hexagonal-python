# hexagonal-python

## Instruções para Configuração e Execução do Aplicativo

### Configuração do Ambiente Virtual

Crie um ambiente virtual utilizando o comando: 
   
```shell
python3 -m venv venv
```

### Ativação do Ambiente Virtual

Ative o ambiente virtual (se criado) usando o comando: 

```shell
source venv/bin/activate
```

### Desativação do Ambiente Virtual

Desative o ambiente virtual (se criado) usando o comando:
```bash
deactivate
```

### Instalação das Dependências

Instale as bibliotecas necessárias executando o comando: 

```shell
python3 -m pip install -r requirements.txt
```

### Inicialização Docker

#### pofile: local

```shell
sudo docker compose up
```

#### pofile: prod

```shell
sudo docker compose --profile prod up
```

### Criação do Banco de Dados

```shell
python3
from src.infra.config import *
db_conn = DBConnectionHandler()
engine = db_conn.get_engine()
Base.metadata.create_all(engine)
```

