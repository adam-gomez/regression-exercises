## 1. Acquire customer_id, monthly_charges, tenure, and total_charges 
## from telco_churn database for all customers with a 2 year contract.

from env import user, password, host
import os
import pandas as pd
import numpy as np

def get_connection(db, user=user, host=host, password=password):
    '''
    This function creates the url needed to connect to the Codeup SQL database
    using the information stored in env.py

    Parameters - (db, user=user, host=host, password=password)
    db = name of the database you wish to access

    Returns a formatted address string
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

    Returns a dataframe
    '''
    sql_query = 'SELECT customer_id, monthly_charges, tenure, total_charges FROM customers WHERE contract_type_id = 3'
    df = pd.read_sql(sql_query, get_connection('telco_churn'))
    df['total_charges'] = df.total_charges.replace(" ", 0)
    df['total_charges'] = pd.to_numeric(df.total_charges)
    return df

def wrangle_grades():
    grades = pd.read_csv("student_grades.csv")
    grades.drop(columns="student_id", inplace=True)
    grades.replace(r"^\s*$", np.nan, regex=True, inplace=True)
    df = grades.dropna().astype("int")
    return df

def wrangle_country():
    sql_query = 'SELECT SurfaceArea, Population, GNP, LifeExpectancy FROM country WHERE (SurfaceArea IS NOT NULL AND Population IS NOT NULL AND GNP IS NOT NULL AND LifeExpectancy IS NOT NULL)'
    df = pd.read_sql(sql_query, get_connection('world'))
    return df