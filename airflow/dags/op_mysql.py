from datetime import datetime
from airflow import DAG
from airflow.providers.mysql.operators.mysql import MySqlOperator

with DAG(
    dag_id='op_mysql_example', 
    start_date=datetime(2024, 5, 1),
    catchup=False,
    schedule_interval="@daily"
) as dag:
    create_new_table = MySqlOperator(
        task_id='create_new_table',
        mysql_conn_id='mysql_conn',
        sql="CREATE TABLE IF NOT EXISTS students (student_id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(256));",
    )

    insert_data = MySqlOperator(
        task_id='insert_data',
        mysql_conn_id='mysql_conn',
        sql="INSERT INTO students (name) VALUES ('Alex Jones');",
    )

create_new_table >> insert_data
