
# Text-Summarizer

![image](https://github.com/rayaran1000/Text-Summarizer/assets/122597408/a82ddb83-5c34-4466-a2c3-193efebb0fac)


This project aims to implement text summarization using the Google pegasus-cnn_dailymail model from Hugging Face, fine-tuned on the SamSum dataset. Text summarization is the process of condensing a piece of text into a shorter version while retaining its key information. The Pegasus model, based on transformer architecture, has shown promising results in various natural language processing tasks, including summarization.

By fine-tuning Pegasus on the SamSum dataset, which consists of conversational summaries, we aim to create a model that can generate concise and accurate summaries of conversational text. The project involves data preprocessing, model fine-tuning, evaluation, and potentially deployment for real-world applications.


## Directory Structure

```plaintext
/project
│   README.md
│   requirements.txt
|   application.py
|   setup.py
|   template.py
|   Dockerfile
|   params.yaml
└───.github/workflows
|   └───main.yaml
└───research
|   └───Text_Summarization.ipynb
|   └───01_data_ingestion.ipynb
|   └───02_data_validation.ipynb
|   └───03_data_transformation.ipynb
|   └───04_model_trainer.ipynb 
|   └───05_model_evaluator.ipynb
|   └───trials.ipynb 
└───src/textSummarizer
|   └───components
|       └───data_ingestion.py
|       └───data_transformation.py
|       └───data_validation.py
|       └───model_evaluator.py
|       └───model_trainer.py
|   └───config
|       └───configuration.py
|   └───config
|       └───configuration.py
|   └───constants
|   └───entity
|   └───logging
|   └───utils
|   └───pipeline
|       └───prediction.py
|       └───stage_01_data_ingestion.py
|       └───stage_02_data_validation.py
|       └───stage_03_data_transformation.py
|       └───stage_04_model_trainer.py
|       └───stage_05_model_evaluator.py

```

# Installation
### STEPS:

Clone the repository

```bash
https://github.com/rayaran1000/Text-Summarizer
```
### STEP 01- Create a conda environment after opening the repository

```bash
conda create -n textS python=3.8 -y
```

```bash
conda activate textS
```


### STEP 02- Install the requirements
```bash
pip install -r requirements.txt
```

### STEP 03- Finally run the following command
```bash
python app.py
```

Now,
```bash
open up you local host and port 

URL -> localhost:8080
```


```bash
Author: Aranya Ray
Data Scientist
Email: aranya.ray1998@gmail.com

```




    
# Deployment Steps done :

1. Created IAM user for deployment.
2. Created ECR repo to store/save docker image.
3. Created EC2 instance (Ubuntu) and installed docker in EC2 Machine.
4. Github Actions CI/CD pipeline created. 
5. Setup Github secrets completed.

## Dataset and Model Specifications

### Dataset 
Samsum dataset : https://github.com/rayaran1000/Datasets/raw/main/Samsum%20data.zip

Documentation : https://huggingface.co/datasets/samsum

### Model
Model used -> pegasus-cnn_dailymail.

Documentation : https://huggingface.co/google/pegasus-cnn_dailymail
## Acknowledgements

I gratefully acknowledge the contributions of the developers and researchers behind the Hugging Face Transformers library, which provides access to state-of-the-art NLP models like Pegasus. 

Additionally, we extend our appreciation to the creators of the SamSum dataset, whose efforts in compiling and curating the dataset have been invaluable to our research. 

Special thanks to the open-source community for their continuous support and valuable feedback.

