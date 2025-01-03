from dataclasses import dataclass,field
from pathlib import Path
from typing import List

@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir:Path
    source_URL:str
    local_data_file:Path
    unzip_dir:Path


@dataclass(frozen=True)
class DataValidationConfig: 
    root_dir: Path
    STATUS_FILE: str
    ALL_REQUIRED_FILES: List[str] = field(default_factory=list)  # Correctly defined with field
@dataclass(frozen=True)
class DataTransformationConfig:
    root_dir: Path
    data_path: Path
    tokenizer_name: Path