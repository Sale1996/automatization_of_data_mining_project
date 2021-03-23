import pandas

from data_set_preprocessor.classes.validator.data_set_spliter.data_set_splitter_validator import \
    DataSetSplitterValidator
from data_set_preprocessor.exceptions.preprocessor_exceptions import WrongInputFormatError


class DataSetSplitterValidatorImpl(DataSetSplitterValidator):
    def validate_input(self, x_data, y_data):
        self.check_is_none(x_data)
        self.check_is_none(y_data)
        self.check_is_instance_of(x_data, pandas.DataFrame)
        self.check_is_instance_of(y_data, pandas.DataFrame)

    def check_is_instance_of(self, object, type):
        if not isinstance(object, type):
            raise WrongInputFormatError

    def check_is_none(self, object):
        if object is None:
            raise WrongInputFormatError