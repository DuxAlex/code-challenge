from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

# Configurações
DEFAULT_ARGS = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 1, 1),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

with DAG('northwind_dag',
         default_args=DEFAULT_ARGS,
         schedule_interval='@daily',  # Executa diariamente
         catchup=False) as dag:

    # Extração e carga do PostgreSQL
    extract_postgres = BashOperator(
        task_id='extract_postgres',
        bash_command='meltano elt tap-postgres target-postgres --ignore-initial-state'
    )

    # Extração e carga do arquivo CSV
    extract_csv = BashOperator(
        task_id='extract_csv',
        bash_command='meltano elt tap-csv target-postgres --ignore-initial-state'
    )

    # Carregar dados no banco de dados PostgreSQL
    load_data = BashOperator(
        task_id='load_data',
        bash_command='meltano elt tap-postgres target-postgres && meltano elt tap-csv target-postgres'
    )

    # Dependências das tarefas
    extract_postgres >> extract_csv >> load_data
