from data_set_info_data_class.data_class.data_set_info import DataSetInfo
from nan_value_filler.classes.input_validator.input_validator import InputValidator
from nan_value_filler.exceptions.nan_value_filler_exceptions import WrongInputFormatError


class InputValidatorImpl(InputValidator):
    def validate(self, data_set_info, filling_method, filling_column_name):
        if data_set_info is None or filling_method is None or filling_column_name is None:
            raise WrongInputFormatError

        if not isinstance(filling_method, str):
            raise WrongInputFormatError

        if not isinstance(filling_column_name, str):
            raise WrongInputFormatError

        if not isinstance(data_set_info, DataSetInfo):
            raise WrongInputFormatError
