# Import modules
from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy import Table
from sqlalchemy import Column
from sqlalchemy import String
import os


# Retrieve DB user and password from env
# Using root user for demo
db_user = 'root'
db_pass = os.getenv('MYSQL_ROOT_PASSWORD')

# Create sqlalchemy engine
engine = create_engine("mysql+mysqldb://{user}:{pw}@airflow-backend"
                       .format(user=db_user,
                               pw=db_pass))

# Create db
engine.execute('CREATE DATABASE contacts_db')
engine.execute('USE contacts_db')

# Create a metadata instance
metadata = MetaData(engine)

# Declare a table
contacts = Table('contacts', metadata,
        Column('Prefix', String(5)),
        Column('FirstName', String(30)),
        Column('Middle Name', String(30)),
        Column('LastName', String(30)),
        Column('Suffix', String(30)),
        Column('Phone', String(15)),
        Column('Address', String(100)),
        Column('Email', String(50)),
        Column('Extension', String(10)),
)

# Create a table
metadata.create_all()
