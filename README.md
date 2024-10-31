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

### Inicialização do banco de dados

```shell
# Enquando o projeto está em fase de desenvolvimento
# OBS: Feche todas as conexões antes (local server, dbeaver, etc...)
sudo find ./nu_connect_api/migrations/. ! -name '__init__.py' -type f -exec rm -vf {} + && \

# Drop database: requer a instalação do postgresql-client
# Debian/Ubuntu: sudo apt install postgresql-client
# Fedora 40: sudo dnf install postgresql

function nu_connect_recrate_db {
  for v in $(< ./setup/.env); do eval $v; done;
  PGPASSWORD=$DATABASE_PASSWORD \
  psql -U $DATABASE_USER -h localhost -p $DATABASE_PORT template1 \
    -c "DROP DATABASE IF EXISTS $DATABASE_NAME" \
    -c "CREATE DATABASE $DATABASE_NAME TEMPLATE template1 OWNER $DATABASE_USER"
} && nu_connect_recrate_db && unset nu_connect_recrate_db && \
###
python3 manage.py makemigrations && \
python3 manage.py migrate && \
python3 manage.py loaddata \
tipo_arquivo \
tipo_categorizacao_beneficiario \
beneficiario_categorizacao \
abordagem_investimento \
lei \
tipo_projeto \
AbgInvest_TpProj_Lei \
categoria_contrapartida \
contrapartida \
relacao_contrapartida_categoria \
AbgInvest_TpProj_Lei_ContrPart \
tematica \
municipio
```

### Execução do Projeto

Inicie o aplicativo com o comando: 

```shell
python3 manage.py runserver
```

###  Gerar arquivo da documentação open-api

```shell
python3 manage.py generateschema --file doc/api/openapi-schema.yml
```

### Principais comandos do Django CLI

Links úteis: 
   
- [Principais comandos](https://www.treinaweb.com.br/blog/principais-comandos-do-django-cli)

### django-rest-framework

[Documentação oficial](https://www.django-rest-framework.org/)
