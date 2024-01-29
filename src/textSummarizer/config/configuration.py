from textSummarizer.constants import *
from textSummarizer.utils.common import read_yaml,create_directories

from textSummarizer.entity import DataIngestionConfig
from textSummarizer.entity import DataValidationConfig
from textSummarizer.entity import DataTransformationConfig
from textSummarizer.entity import ModelTrainerConfig

class ConfigurationManager:
    def __init__(
            self,
            config_filepath = CONFIG_FILE_PATH,
            params_filepath = PARAMS_FILE_PATH):
    # Here we are reading the yaml file and we can now use the file paths present inside pararms and config.yaml        
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)

        create_directories([self.config.artifacts_root]) # Here we are calling the artifacts_root key values using '.' , which was the purpose of @ensure_annotations

    def get_data_ingestion_config(self) -> DataIngestionConfig: # Here we are using the entity to specify the return type classes to make sure proper output is returned
        config= self.config.data_ingestion # Calling the data_ingestion dictionary created in config.yaml file

        create_directories([config.root_dir]) # Creating a directory using the root directory

        data_ingestion_config = DataIngestionConfig( # Extracting the values from the config.yaml to here inside data_ingestion_config
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir
        )

        return data_ingestion_config
    
    def get_data_validation_config(self) -> DataValidationConfig: # Here we are using the entity to specify the return type classes to make sure proper output is returned
        config= self.config.data_validation # Calling the data_validation dictionary created in config.yaml file

        create_directories([config.root_dir]) # Creating a directory using the root directory

        data_validation_config = DataValidationConfig( # Extracting the values from the config.yaml to here inside data_ingestion_config
            root_dir=config.root_dir,
            STATUS_FILE=config.STATUS_FILE,
            ALL_REQUIRED_FILES=config.ALL_REQUIRED_FILES
        )

        return data_validation_config
    
    def get_data_transformation_config(self) -> DataTransformationConfig: # Here we are using the entity to specify the return type classes to make sure proper output is returned
        config= self.config.data_transformation # Calling the data_validation dictionary created in config.yaml file

        create_directories([config.root_dir]) # Creating a directory using the root directory

        data_transformation_config = DataTransformationConfig( # Extracting the values from the config.yaml to here inside data_ingestion_config
            root_dir=config.root_dir,
            data_path=config.data_path,
            tokenizer_name=config.tokenizer_name
        )

        return data_transformation_config
    
    def get_model_trainer_config(self) -> ModelTrainerConfig:

        config= self.config.model_trainer # Calling the model_trainer dictionary created in config.yaml file
        params=self.params.TrainingArguments # Calling the TrainingArguments dictionary in params.yaml file

        create_directories([config.root_dir]) # Creating a directory using the root directory

        model_trainer_config = ModelTrainerConfig( # Extracting the values from the config.yaml to here inside data_ingestion_config
            root_dir=config.root_dir,
            data_path=config.data_path,
            model_ckpt=config.model_ckpt,
            num_train_epochs=params.num_train_epochs,
            warmup_steps=params.warmup_steps,
            per_device_train_batch_size=params.per_device_train_batch_size,
            per_device_eval_batch_size= params.per_device_eval_batch_size,
            weight_decay=params.weight_decay,
            logging_steps=params.logging_steps,
            evaluation_strategy=params.evaluation_strategy,
            eval_steps=params.eval_steps,
            save_steps=params.save_steps,
            gradient_accumulation_steps=params.gradient_accumulation_steps
        )

        return model_trainer_config