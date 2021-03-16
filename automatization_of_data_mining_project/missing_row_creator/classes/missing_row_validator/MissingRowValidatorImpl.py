from missing_row_creator.classes.data_classes.data_set_info import DataSetInfo
from missing_row_creator.classes.missing_row_validator.missing_row_validator import MissingRowValidator
from missing_row_creator.exceptions.missing_row_creator_exceptions import WrongInputFormatError, NonIterableObjectError, \
    MissingYearColumnError, MissingCountryCodeColumnError


class MissingRowValidatorImpl(MissingRowValidator):
    def validate(self, data_sets_info, year_range):
        if data_sets_info is None or year_range is None:
            raise WrongInputFormatError
        if not isinstance(data_sets_info, list):
            raise NonIterableObjectError

        if not isinstance(year_range, tuple):
            raise WrongInputFormatError

        if len(year_range) != 2:
            raise WrongInputFormatError

        if not isinstance(year_range[0], int) or not isinstance(year_range[1], int):
            raise WrongInputFormatError

        if year_range[0] > year_range[1]:
            raise WrongInputFormatError

        for data_set_info in data_sets_info:
            if not isinstance(data_set_info, DataSetInfo):
                raise WrongInputFormatError
            data_set_columns = data_set_info.data_set.columns.tolist()
            if "Year" not in data_set_columns:
                raise MissingYearColumnError
            if "Country Code" not in data_set_columns:
                raise MissingCountryCodeColumnError