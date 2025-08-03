import sys
import logging
from logger import logging

def error_message_details(error, error_detail:sys):
    _,_,exc_tb=error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename   # to get a filename
    error_message = "Error occurd in python script name [{0}] line number [{1}] error message [{2}]".format(
    file_name, exc_tb.tb_lineno, str(error))
    return error_message


class customException(Exception):
    def __init__(self, error_message, error_detail:sys):
        super().__init__(error_message)
        self.error_message=error_message_details(error_message, error_detail=error_detail)

    def __str__(self):
        return self.error_message
    
# if __name__=="__main__":
#     try:
#         a=4/0
#     except Exception as e:
#         logging.info("Divide by 0 error")
#         raise customException(e, sys)