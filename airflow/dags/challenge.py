from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago
from datetime import datetime, timedelta
from sqlalchemy import create_engine
import pandas as pd

# --- Database Connection ---
# Replace with your actual database credentials
db_conn_str = "postgresql://northwind_user:thewindisblowing@postgres:5432/northwind"
engine = create_engine(db_conn_str)

# --- Data Extraction Functions ---

def extract_postgres_data(execution_date):
    # Replace with your actual SQL query
    sql_query = "SELECT * FROM your_table"  
    df = pd.read_sql(sql_query, engine)
    df.to_csv(f'/data/postgres/{execution_date.strftime("%Y-%m-%d")}/postgres_data.csv', index=False)

def extract_csv_data(execution_date):
    csv_file_path = '/path/to/your/order_details.csv'  # Replace with your actual file path
    df = pd.read_csv(csv_file_path)
    df.to_csv(f'/data/csv/{execution_date.strftime("%Y-%m-%d")}/csv_data.csv', index=False)

# --- Data Loading Functions ---

def load_postgres_data(execution_date):
    csv_file_path = f'/data/postgres/{execution_date.strftime("%Y-%m-%d")}/postgres_data.csv'
    df = pd.read_csv(csv_file_path)
    df.to_sql('your_table', engine, if_exists='append', index=False)

def load_csv_data(execution_date):
    csv_file_path = f'/data/csv/{execution_date.strftime("%Y-%m-%d")}/csv_data.csv'
    df = pd.read_csv(csv_file_path)
    df.to_sql('your_table', engine, if_exists='append', index=False)

# --- Define the DAG ---
with DAG(
    dag_id='challenge_dag',
    default_args={
        'owner': 'airflow',
        'start_date': days_ago(1),
        'retries': 1,
        'retry_delay': timedelta(minutes=5),
    },
    schedule_interval='@daily',  # Run daily
    catchup=True,               # Catch up on past days
    tags=['challenge', 'data-pipeline'],
) as dag:

    # Define tasks
    extract_postgres = PythonOperator(
        task_id='extract_postgres_data',
        python_callable=extract_postgres_data,
        provide_context=True,
    )

    extract_csv = PythonOperator(
        task_id='extract_csv_data',
        python_callable=extract_csv_data,
        provide_context=True,
    )

    load_postgres = PythonOperator(
        task_id='load_postgres_data',
        python_callable=load_postgres_data,
        provide_context=True,
    )

    load_csv = PythonOperator(
        task_id='load_csv_data',
        python_callable=load_csv_data,
        provide_context=True,
    )

    # Set task dependencies
    extract_postgres >> load_postgres
    extract_csv >> load_csv