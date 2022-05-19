from datetime import timedelta

from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.dummy import DummyOperator
from airflow.utils.dates import days_ago

args = {
    'owner': 'airflow',
    #'email': ['itcast@qq.com'],
    #'email_on_failure': True,
    #'email_on_retry': True,
    #'retries': 1
}

dag = DAG(
    dag_id='first_bash_operator',
    default_args=args,
    schedule_interval='*/1 * * * *',
    start_date=days_ago(2),
    dagrun_timeout=timedelta(minutes=3),
    tags=['itcast'],
    params={"example_key": "example_value"},
)

run_first_bash = DummyOperator(
    task_id='run_first_bash',
    dag=dag,
)

# [START howto_operator_bash]
run_this = BashOperator(
    task_id='echo_first_bash',
    bash_command='echo "hello airflow" >> /root/first_bash_operator.log',
    dag=dag,
)
# [END howto_operator_bash]

run_this >> run_first_bash
