## 1. Acquire customer_id, monthly_charges, tenure, and total_charges 
## from telco_churn database for all customers with a 2 year contract.

from env import user, password, host
import os
import pandas as pd

def get_connection(db, user=user, host=host, password=password):
    '''
    This function creates the url needed to connect to the Codeup SQL database
    using the information stored in env.py

    Parameters - (db, user=user, host=host, password=password)
    db = name of the database you wish to access
    '''
    return f'mysql+pymysql://{user}:{password}@{host}/{db}'

def wrangle_telco():
    '''
    This function will select customer_id, monthly_charges, tenure, and total_charges from
    the customer table of the telco_churn database using the get_connection function 
    (and credentials in env.py). Only customers with a 2 year contract are selected.

    Blank values in 'total_charges' (made up of the character " ") are replaced with 0
    The 'total_charges' column is converted to numeric data type

    Parameters - None 
    '''
    sql_query = 'SELECT customer_id, monthly_charges, tenure, total_charges FROM customers WHERE contract_type_id = 3'
    df = pd.read_sql(sql_query, get_connection('telco_churn'))
    df['total_charges'] = df.total_charges.replace(" ", 0)
    df['total_charges'] = pd.to_numeric(df.total_charges)
    return df