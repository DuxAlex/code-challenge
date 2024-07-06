#!/bin/bash

# Atualizar pacotes e instalar dependências
sudo apt-get update
sudo apt-get install -y python3-pip python3-venv docker-compose

# Criar um diretório para o projeto
mkdir /workspaces/code-challenge/airflow_meltano_project
cd /workspaces/code-challenge/airflow_meltano_project

# Configurar ambiente virtual
python3 -m venv venv
source venv/bin/activate

# Instalar Apache Airflow
export AIRFLOW_VERSION=2.4.1
export PYTHON_VERSION="$(python --version | cut -d " " -f 2 | cut -d "." -f 1-2)"
export CONSTRAINT_URL="https://raw.githubusercontent.com/apache/airflow/constraints-${AIRFLOW_VERSION}/constraints-${PYTHON_VERSION}.txt"
pip install "apache-airflow==${AIRFLOW_VERSION}" --constraint "${CONSTRAINT_URL}"

# Inicializar o banco de dados do Airflow
airflow db init

# Criar usuário admin no Airflow
airflow users create --username admin --password admin --firstname Admin --lastname User --role Admin --email admin@example.com

# Iniciar Airflow
airflow webserver -p 8080 &
airflow scheduler &

# Instalar Meltano
pip install meltano

# Iniciar projeto Meltano
meltano init my_meltano_project
cd my_meltano_project

# Adicionar um extractor (por exemplo, tap-csv)
meltano add extractor tap-csv

# Adicionar um loader (por exemplo, target-postgres)
meltano add loader target-postgres

# Copiar o docker-compose.yml para o diretório atual
cp docker-compose.yml .

# Iniciar o container PostgreSQL
docker-compose up -d

# Aguardar o PostgreSQL iniciar (ajustar conforme necessário)
sleep 10

# Carregar dados CSV para o PostgreSQL
docker cp data/northwind.sql db:/northwind.sql
docker-compose exec db psql -U northwind_user -d northwind -f /northwind.sql

# Configurar Meltano para usar PostgreSQL
meltano config target-postgres set host localhost
meltano config target-postgres set port 5432
meltano config target-postgres set dbname northwind
meltano config target-postgres set user northwind_user
meltano config target-postgres set password thewindisblowing

# Configurar Meltano para usar o CSV como extractor
meltano config tap-csv set files '[{"entity": "your_entity", "path": "~data/order_details.csv"}]'
meltano config tap-csv set "delimiter" ","
meltano config tap-csv set "quotechar" "\""

# Executar uma pipeline do Meltano
meltano elt tap-csv target-postgres

echo "Airflow e Meltano foram instalados e configurados com sucesso."
echo "Acesse o Airflow em http://localhost:8080 com usuário 'admin' e senha 'admin'."