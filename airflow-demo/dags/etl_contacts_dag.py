# Import modules
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime

import transform_contacts

default_args = {
        "start_date": datetime(2020, 1, 1),
        "owner": "airflow"
}

with DAG(dag_id="etl_contacts_dag", schedule_interval="@once", default_args=default_args) as dag:
    etl_contacts = PythonOperator(task_id="etl_contacts", python_callable=transform_contacts.main)
