import os
import sys
from src.ML_Project.logger import logging
from src.ML_Project.exception import CustomException
from dataclasses import dataclass
from src.ML_Project.utils import read_sql_data
from sklearn.model_selection import train_test_split

@dataclass
class DataIngestionConfig:
    
    train_data_path: str = os.path.join('artifacts', 'train_data.csv')
    test_data_path: str = os.path.join('artifacts', 'test_data.csv')
    raw_data_path: str = os.path.join('artifacts', 'raw_data.csv')
    
class DataIngestion:
    
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()
        
    def initialize_data_ingestion(self):
        
        try:
            logging.info("Reading data from MySQL")
            
            df = read_sql_data()
            train_data, test_data = train_test_split(df, test_size = 0.2, random_state = 42)
            
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)
            
            df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)
            train_data.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
            test_data.to_csv(self.ingestion_config.test_data_path, index=False, header=True)
            
            logging.info("Data Ingestion Completed.")
            
        except Exception as e:
            
            logging.info("Exception occoured in Data Ingestion.")
            CustomException(e, sys)
            
    

    
    
    