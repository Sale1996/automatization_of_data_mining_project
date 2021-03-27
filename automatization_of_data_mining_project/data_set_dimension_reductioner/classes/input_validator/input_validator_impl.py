from data_set_dimension_reductioner.classes.input_validator.input_validator import InputValidator
import pandas
from data_set_dimension_reductioner.exceptions.dimension_reduction_exceptions import WrongInputFormatError, \
    NoStringValuesAllowedInDataSetError


class InputValidatorImpl(InputValidator):
    def validate(self, x_data, y_data):
        if x_data is None or y_data is None:
            raise WrongInputFormatError

        if not isinstance(x_data, pandas.DataFrame):
            raise WrongInputFormatError

        if not isinstance(y_data, pandas.DataFrame):
            raise WrongInputFormatError

        non_numerical_column_names = self.get_non_numerical_column_names(x_data)

        if non_numerical_column_names:
            raise NoStringValuesAllowedInDataSetError

    def get_non_numerical_column_names(self, data_set):
        numerics = ['int16', 'int32', 'int64', 'float16', 'float32', 'float64', 'uint8']
        numerical_columns = list(data_set.select_dtypes(include=numerics).columns)
        categorical_columns = list(set(data_set.columns.tolist()) - set(numerical_columns))
        return categorical_columns
