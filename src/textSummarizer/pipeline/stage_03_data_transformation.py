from textSummarizer.config.configuration import ConfigurationManager
from textSummarizer.logging import logger
from textSummarizer.components.data_transformation import DataTransformation

class DataTransformationPipeline(DataTransformation):
    def __init__(self):
        pass
    def main(self):
        config=ConfigurationManager()
        data_transformation_config=config.get_data_transformation_config()
        data_transformation=DataTransformation(config=data_transformation_config)
        data_transformation.convert()