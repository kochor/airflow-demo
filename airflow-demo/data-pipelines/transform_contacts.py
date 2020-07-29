# Import modules
from sqlalchemy import create_engine

import pandas as pd
import os


# TRANSFORMED
def main():
    df = pd.read_csv("/root/airflow/demo_etl/people_data.csv", sep="\t")

    # Make sure phone column is string
    if df['Phone'].dtype != object:
        df['Phone'] = df['Phone'].astype(object)

    # Creating new DataFrame with phone and extensions split into columns
    df_ph_ext = df["Phone"].str.split("x", n = 1, expand = True)
    df["Phone"] = df_ph_ext[0]
    df["Extension"] = df_ph_ext[1]

    # Trim whitespace and convert to upper case
    df = df.apply(lambda x: x.str.replace(" ","").str.upper() if x.dtype == "object" else x)

    # Convert alpha characters to numbers
    df['Phone'] = df['Phone']\
        .str.replace(r'[A-C]', "2")\
        .str.replace(r'[D-F]', "3").str.replace(r'[G-I]', "4")\
        .str.replace(r'[J-L]', "5").str.replace(r'[M-O]', "6")\
        .str.replace(r'[P-S]', "7").str.replace(r'[T-V]', "8")\
        .str.replace(r'[W-Z]', "9")

    # Remove everything that's not a number
    df['Phone'] = df['Phone'].str.replace(r'[^0-9]',"")

    # Retrieve db user and password from env
    # Using root user for demo
    db_user = 'root'
    db_pass = os.getenv('MYSQL_ROOT_PASSWORD')
    # Create sqlalchemy engine
    engine = create_engine("mysql+mysqldb://{user}:{pw}@airflow-backend/{db}"
                           .format(user=db_user,
                                   pw=db_pass,
                                   db="contacts_db"))

    # Insert whole DataFrame into MySQL
    df.to_sql('contacts', con = engine, if_exists = 'append', chunksize = 1000, index=False)

if __name__ == '__main__':
    main()

