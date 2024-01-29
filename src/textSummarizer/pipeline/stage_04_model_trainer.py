from textSummarizer.config.configuration import ConfigurationManager
from textSummarizer.components.model_trainer import ModelTrainer
from textSummarizer.logging import logger


class ModelTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            config = ConfigurationManager()
            model_trainer_config = config.get_model_trainer_config() # Storing the configuration
            model_training = ModelTrainer(config=model_trainer_config) # Using the configuration saved earlier to call model_training
            model_training.train()
        except Exception as e:
            raise e