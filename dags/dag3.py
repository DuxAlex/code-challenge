from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago

default_args = {
    'owner': 'airflow',
    'start_date': days_ago(1),
}

dag = DAG(
    'data_pipeline3',
    default_args=default_args,
    description='A simple data pipeline',
    schedule_interval='@daily',
)

# Função para a task de confirmação
def confirm_task():
    print("A task de confirmação foi executada com sucesso!")

# Task de confirmação
confirmation_task = PythonOperator(
    task_id='confirmation_task',
    python_callable=confirm_task,
    dag=dag,
)

# Etapa 1: Extração dos dados
extract_orders = BashOperator(
    task_id='extract_orders',
    bash_command='mkdir -p /data/postgres/orders/{{ ds }} && meltano run tap-postgres target-jsonl --output /data/postgres/orders/{{ ds }}/orders.json',
    dag=dag,
)

extract_order_details = BashOperator(
    task_id='extract_order_details',
    bash_command='mkdir -p /data/csv/{{ ds }} && cp /opt/airflow/etl_meltano/data/order_details.csv /data/csv/{{ ds }}/order_details.csv',
    dag=dag,
)

# Etapa 2: Carga no PostgreSQL
load_to_postgres = BashOperator(
    task_id='load_to_postgres',
    bash_command='meltano run target-postgres --input /data/csv/{{ ds }}/order_details.csv',
    dag=dag,
)

# Definindo a ordem das tasks
confirmation_task >> extract_orders >> extract_order_details >> load_to_postgres
