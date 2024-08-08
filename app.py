from src.ML_Project.logger import logging
from src.ML_Project.exception import CustomException
import sys

if __name__ == "__main__":
    
    logging.info("Execution has been started.")
    
    try:
        a = 1/0
        logging.info("Exection successful.")
    except Exception as e:
        logging.info("Custom Exception occured.")
        raise CustomException(e, sys)