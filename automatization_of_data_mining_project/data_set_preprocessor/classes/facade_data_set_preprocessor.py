from typing import List

from data_set_preprocessor.classes.data_set_preprocessor import DataSetPreprocessor
from data_set_preprocessor.classes.data_set_splitter.data_set_splitter import DataSetSplitter
from data_set_preprocessor.classes.processing_method.processing_method import ProcessingMethod
from data_set_preprocessor.classes.validator.data_set_processer_validator.data_set_preprocessor_validator import \
    DataSetPreprocessorValidator
from data_set_preprocessor.classes.validator.data_set_spliter.data_set_splitter_validator import \
    DataSetSplitterValidator


class FacadeDataSetPreprocessor(DataSetPreprocessor):
    def __init__(self, data_set_preprocessor_validator: DataSetPreprocessorValidator,
                 data_set_splitter_validator: DataSetSplitterValidator,
                 data_set_splitter: DataSetSplitter,
                 processing_methods: List[ProcessingMethod]):
        self.data_set_preprocessor_validator = data_set_preprocessor_validator
        self.data_set_splitter_validator = data_set_splitter_validator
        self.data_set_splitter = data_set_splitter
        self.processing_methods = processing_methods

    def get_preprocessed_data(self, data):
        self.data_set_preprocessor_validator.validate_input(data)
        processed_data = data.copy(deep=True)
        for processing_method in self.processing_methods:
            processed_data = processing_method.process_data_set(processed_data)

        return processed_data

    def get_train_validation_test_split_of_data_set(self, x_data, y_data, test_data_percentage):
        self.data_set_splitter_validator.validate_input(x_data, y_data)

        return self.data_set_splitter.split_data_set_into_train_validation_test(x_data, y_data, test_data_percentage)
