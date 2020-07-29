FROM python:3.7

WORKDIR /root/airflow/

# Copy all the files
COPY . .

# Install Airflow
RUN pip3 install 'apache-airflow[mysql,crypto]'==1.10.11  --constraint requirements.txt

ENV PYTHONPATH=/root/airflow/data-pipelines/

# Run bootstrap script
RUN chmod +x airflow.sh
CMD ./airflow.sh

