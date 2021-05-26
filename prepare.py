import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer


###################### Prep Telco Churn Data ######################

def prep_telco_churn(df):
    '''
    This function takes in the telco_churn df acquired by get_telco_churn_data
    Returns the telco_churn df.
    '''
    # drop and rename columns
    # df = df.drop(columns=['customer_id', 'internet_service_id', 'contract_type_id', 'payment_type_id'])
    
    # change data types
    df.total_charges = df.total_charges.str.replace(' ', '0').astype(float)
    df.telco.replace({'churn': {'No':0, 'Yes':1}}, inplace=True)
    
    return df

###################### Test Train Split Telco Churn Data ######################

def train_validate_test_split(df):
    '''
    This function take in the telco_churn data from aquire.py, get_telco_churn_data(),
    performs a split, stratifies by churn.
    Returns train, validate, and test dfs.
    '''
    train_validate, test = train_test_split(df, test_size=.2, 
                                        random_state=123, 
                                        stratify=df.churn)
    train, validate = train_test_split(train_validate, test_size=.3, 
                                   random_state=123, 
                                   stratify=train_validate.churn)
    return train, validate, test