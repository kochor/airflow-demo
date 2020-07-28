## Description
Apache Airflow with MySQL backend (database) in docker. Demo pipeline is included as well.


## Apache Airflow
[Apache Airflow](https://airflow.apache.org/docs/stable/) (or simply Airflow) is a platform to programmatically author, schedule, and monitor workflows.

When workflows are defined as code, they become more maintainable, versionable, testable, and collaborative.

Use Airflow to author workflows as directed acyclic graphs (DAGs) of tasks. The Airflow scheduler executes your tasks on an array of workers while following the specified dependencies. Rich command line utilities make performing complex surgeries on DAGs a snap. The rich user interface makes it easy to visualize pipelines running in production, monitor progress, and troubleshoot issues when needed.

Official [GitHub](https://github.com/apache/airflow/blob/master/README.md) page.


## Pre-requisites
- people_data.csv file must exist with data in it under airflow-demo/demo_etl/ folder
- docker installed
- docker-compose installed (https://docs.docker.com/compose/install/)
- Port 8080 accessible on the host to access Airflow Webserver

*It is recommended that you have at least 6GB of RAM, and 2 CPUs.*

## Automated Setup
If you are running macOS, Ubuntu or CentOS, you can clone the repository, add appropriate airflow-demo/demo_etl/people_data.csv and run the following commands:
```
docker-compose up -d  # build airflow image and start
```

## To stop
```
docker-compose down
```
## How to access Apache Airflow on browser
```
http://IP_address:8080
```
