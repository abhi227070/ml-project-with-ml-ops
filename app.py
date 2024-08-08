from src.ML_Project.logger import logging
from src.ML_Project.exception import CustomException
from src.ML_Project.components.data_ingestion import DataIngestion
import sys

if __name__ == "__main__":
    
    try:
        data_ingestion = DataIngestion()
        data_ingestion.initialize_data_ingestion()
        
    except Exception as e:
        logging.info("Custom Exception occured.")
        raise CustomException(e, sys)