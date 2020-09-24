## 1. Acquire customer_id, monthly_charges, tenure, and total_charges 
## from telco_churn database for all customers with a 2 year contract.

from env import user, password, host
import os
import pandas as pd

def get_connection(db, user=user, host=host, password=password):
    return f'mysql+pymysql://{user}:{password}@{host}/{db}'

def wrangle_telco():
    sql_query = 'SELECT customer_id, monthly_charges, tenure, total_charges FROM customers WHERE contract_type_id = 3'
    df = pd.read_sql(sql_query, get_connection('telco_churn'))
    df['total_charges'] = df.total_charges.replace(" ", 0)
    df['total_charges'] = pd.to_numeric(df.total_charges)
    return df