from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.empty import EmptyOperator

def hello_airflow():
    print("AirFlow Is Running")

with DAG(
    dag_id='op_python_example', 
    start_date=datetime(2023, 8, 1),
    catchup=False, 
    schedule_interval="@daily"
) as dag:
    task1 = PythonOperator(
        task_id='hello_airflow_task',
        python_callable=hello_airflow
    )
    first_task = EmptyOperator(task_id='start')
    last_task = EmptyOperator(task_id='end')

    first_task >> task1 >> last_task
