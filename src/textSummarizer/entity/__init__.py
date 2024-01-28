from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class DataIngestionConfig: # defined for the config components present in artifacts for data ingestion
    # Below are the return types for the components (root_dir is Path format , URL is string etc)
    root_dir : Path 
    source_URL : str
    local_data_file : Path
    unzip_dir : Path

@dataclass(frozen=True)
class DataValidationConfig: # defined for the config components present in artifacts for data validation
    # Below are the return types for the components (root_dir is Path format , Status File is string etc)
    root_dir : Path 
    STATUS_FILE : str
    ALL_REQUIRED_FILES : list

@dataclass(frozen=True)
class DataTransformationConfig: # defined for the config components present in artifacts for data transformation
    root_dir : Path 
    data_path : Path
    tokenizer_name : Path