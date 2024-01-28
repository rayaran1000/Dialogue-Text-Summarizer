import os
from textSummarizer.logging import logger
from textSummarizer.entity import DataValidationConfig


class DataValidation:
    def __init__(self,config:DataValidationConfig): # It will take the configuration from DataIngestionConfig defined earlier , which will in turn use Configuration Manager to take data from config.yaml
        self.config = config

    def validation_all_files_exist(self) -> bool:

        try:
            validation_status = None # Validation status counter for checking all files exists or not

            all_files = os.listdir(os.path.join('artifacts','data_ingestion','samsum_dataset')) # going to the directory where the files are present

            for file in self.config.ALL_REQUIRED_FILES:
                if file not in all_files: # checking whether all the files mentioned in ALL_REQUIRED_FILES is present or not in the dataset file
                    validation_status = False
                    with open(self.config.STATUS_FILE,'a') as f:
                        f.write(f"Validation Status : {validation_status} - file : {file}\n")
                else:
                    validation_status = True
                    with open(self.config.STATUS_FILE,'a') as f:
                        f.write(f"Validation Status : {validation_status} - file : {file}\n")
                
            return validation_status
        
        except Exception as e:
            raise e