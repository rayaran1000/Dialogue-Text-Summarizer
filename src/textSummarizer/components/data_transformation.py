import os
from textSummarizer.logging import logger
from transformers import AutoTokenizer
from datasets import load_dataset,load_from_disk

from textSummarizer.entity import DataTransformationConfig

class DataTransformation:
    def __init__(self,config:DataTransformationConfig): # It will take the configuration from DataIngestionConfig defined earlier , which will in turn use Configuration Manager to take data from config.yaml
        self.config = config
        self.tokenizer = AutoTokenizer.from_pretrained(self.config.tokenizer_name)

    def convert_examples_to_features(self,example_batch): # Used for tokenization of input and target

        #Tokenizing the 'dialogue' sequences of the dataset
        input_encodings = self.tokenizer(example_batch['dialogue'] , max_length = 1024, truncation = True )

        #Tokenizing the 'summary' sequences of the dataset using the target tokenizer
        with self.tokenizer.as_target_tokenizer():
            target_encodings = self.tokenizer(example_batch['summary'], max_length = 128, truncation = True )

        #Returning the input and target encodings done
        return {
            'input_ids' : input_encodings['input_ids'],
            'attention_mask': input_encodings['attention_mask'],
            'labels': target_encodings['input_ids']
        }
    
    def convert(self):
        dataset_samsum = load_from_disk(self.config.data_path)
        dataset_samsum_pt = dataset_samsum.map(self.convert_examples_to_features, batched = True) # Tokenizing the dataset
        dataset_samsum_pt.save_to_disk(os.path.join(self.config.root_dir,"samsum_dataset_tokenized"))