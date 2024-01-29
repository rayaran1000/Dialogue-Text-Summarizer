from textSummarizer.config.configuration import ConfigurationManager
from textSummarizer.components.model_evaluator import ModelEvaluator
from textSummarizer.logging import logger


class ModelEvaluationPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            config = ConfigurationManager()
            model_evaluation_config = config.get_model_evaluator_config()
            model_evaluation_config = ModelEvaluator(config=model_evaluation_config)
            model_evaluation_config.evaluate()
        except Exception as e:
            raise e