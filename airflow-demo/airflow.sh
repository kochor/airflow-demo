#!/usr/bin/env bash

INIT_FILE=.airflowinitialized
if [[ ! -f "$INIT_FILE" ]]; then
    # Create all Airflow configuration files
    airflow initdb
    rm /root/airflow/airflow.db

    sed -i "s|sql_alchemy_conn = sqlite:////root/airflow/airflow.db|sql_alchemy_conn = mysql+mysqldb://${MYSQL_USER}:${MYSQL_PASSWORD}@airflow-backend:3306/${MYSQL_DATABASE}|g;s|load_examples = True|load_examples = False|g" /root/airflow/airflow.cfg

    # Wait until the DB is ready
    apt update && apt install -y netcat
    while ! nc -z airflow-backend 3306; do
        sleep 1
    done
    apt remove -y netcat

    # Setup DB
    airflow initdb

    # Setup DB for transform_contacts
    python /root/airflow/demo_etl/create_db_schema.py

    # This configuration is done only the first time
    touch "$INIT_FILE"
fi

# Run the Airflow webserver and scheduler
airflow scheduler &
airflow webserver &
wait
