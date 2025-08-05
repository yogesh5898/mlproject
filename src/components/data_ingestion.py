import os
import sys
from src.exception import customException
from src.logger import logging
from src.components.data_transformation import DataTransformation, DataTransformationConfig
from src.components.model_trainer import modelTrainerConfig, modelTrainer

import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass


@dataclass
class DataIngestionConfig:
    """ If any input is required I will give here """    

    """ This @dataclass - Inside a class if we want to define class variable we use init 
    but if we use this we can directly define class variable """

    train_data_path: str=os.path.join('artifacts', "train.csv")
    test_data_path: str=os.path.join('artifacts', "test.csv")
    raw_data_path: str=os.path.join('artifacts', "data.csv")

    """ These are the inputs we given to DataIngestion component. 
    Now it knows where to save this train, test, raw files """

class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionConfig()

    """ When we call this class this will call DataIngestionConfig and save this 3 paths """

    def initiate_data_ingestion(self):
        logging.info("Entered the data ingestion method or component")
        try:
            df = pd.read_csv('notebook/data/stud.csv')
            logging.info("Read the dataset as a dataframe")

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)
            """ exist_ok=True if the folder already there keep it dont delete and create it again """

            df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)

            logging.info("Train test split Initiated")
            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)

            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)

            logging.info("Ingestion of data is completed")

            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )
        except Exception as e:
            raise customException(e, sys)
            
if __name__ == "__main__":
    obj = DataIngestion()
    train_data, test_data = obj.initiate_data_ingestion()
        
    data_transformation = DataTransformation()
    train_arr, test_arr, _ = data_transformation.initiate_data_transformation(train_data, test_data)

    modeltrainer = modelTrainer()
    print(modeltrainer.initiate_model_trainer(train_arr, test_arr))
