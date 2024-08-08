import os
import sys
from src.ML_Project.logger import logging
from src.ML_Project.exception import CustomException
from dotenv import load_dotenv
from sqlalchemy import create_engine
import pandas as pd

load_dotenv()

host = os.getenv("host")
user = os.getenv("user")
password = os.getenv("password")
db = os.getenv("db")
port = '3306'


def read_sql_data():
    
    logging.info("Reading SQL database started...")
    
    try:
        
        connection_string = f'mysql+pymysql://{user}:{password}@{host}:{port}/{db}'
        engine = create_engine(connection_string)
        query = "SELECT * FROM car_dataset"
        
        logging.info("Connection established.")
        
        
        df = pd.read_sql(query, engine)
        
        return df
    
    except Exception as e:
        logging.info("Exception occoured in SQL database.")
        raise CustomException(e, sys)