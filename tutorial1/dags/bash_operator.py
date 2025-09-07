from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG(
    dag_id='simple_bash_example',
    start_date=datetime(2023, 1, 1),
    schedule=None,  # Set to None for manual triggering or define a schedule
    catchup=False,
    tags=['example'],
) as dag:
    # Define a BashOperator task
    hello_bash_task = BashOperator(
        task_id='hello_bash',
        bash_command='echo "Hello, BashOperator!" > hello_bash.out',
    )