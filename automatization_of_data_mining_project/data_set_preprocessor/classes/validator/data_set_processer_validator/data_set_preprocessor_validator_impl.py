import pandas

from data_set_preprocessor.classes.validator.data_set_processer_validator.data_set_preprocessor_validator import \
    DataSetPreprocessorValidator
from data_set_preprocessor.exceptions.preprocessor_exceptions import WrongInputFormatError


class DataSetPreprocessorValidatorImpl(DataSetPreprocessorValidator):
    def validate_input(self, data_set: pandas.DataFrame):
        self.check_is_none(data_set)
        self.check_is_instance_of(data_set, pandas.DataFrame)

    def check_is_instance_of(self, object, type):
        if not isinstance(object, type):
            raise WrongInputFormatError

    def check_is_none(self, object):
        if object is None:
            raise WrongInputFormatError
