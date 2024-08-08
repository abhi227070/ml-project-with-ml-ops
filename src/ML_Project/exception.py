import sys
from src.ML_Project.logger import logging

def get_error_message_details(error_message, error_details: sys):
    
    _,_,exc_tb = error_details.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    line_no = exc_tb.tb_lineno
    
    error = f"Error occoured in python script name {file_name} line number {line_no} error message: {str(error_message)}"
    
    return error



class CustomException(Exception):
    
    def __init__(self, error_message, error_details: sys):
        
        super().__init__(error_message)
        self.error_message = get_error_message_details(error_message, error_details)
        
    def __str__(self):
        return self.error_message