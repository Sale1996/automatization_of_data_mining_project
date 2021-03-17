from missing_row_creator.classes.data_classes.data_set_info import DataSetInfo
from missing_row_creator.classes.missing_row_validator.missing_row_validator import MissingRowValidator
from missing_row_creator.exceptions.missing_row_creator_exceptions import WrongInputFormatError, NonIterableObjectError, \
    MissingFirstColumnPairError, MissingSecondColumnPairError


class MissingRowValidatorImpl(MissingRowValidator):
    def validate(self, data_sets_info, first_column_pair_name,
                 second_column_pair_name, second_column_values_to_match):
        self.check_is_input_none(data_sets_info, first_column_pair_name, second_column_pair_name,
                                 second_column_values_to_match)
        self.check_is_iterable(data_sets_info, second_column_values_to_match)
        self.check_are_column_names_type_of_string(first_column_pair_name, second_column_pair_name)
        self.check_data_sets_info(data_sets_info, first_column_pair_name, second_column_pair_name)

    def check_is_input_none(self, data_sets_info, first_column_pair_name, second_column_pair_name,
                            second_column_values_to_match):
        if data_sets_info is None or first_column_pair_name is None \
                or second_column_pair_name is None or second_column_values_to_match is None:
            raise WrongInputFormatError

    def check_is_iterable(self, data_sets_info, second_column_values_to_match):
        if not isinstance(data_sets_info, list):
            raise NonIterableObjectError
        if not isinstance(second_column_values_to_match, list):
            raise NonIterableObjectError

    def check_are_column_names_type_of_string(self, first_column_pair_name, second_column_pair_name):
        if not isinstance(first_column_pair_name, str):
            raise WrongInputFormatError
        if not isinstance(second_column_pair_name, str):
            raise WrongInputFormatError

    def check_data_sets_info(self, data_sets_info, first_column_pair_name, second_column_pair_name):
        for data_set_info in data_sets_info:
            if not isinstance(data_set_info, DataSetInfo):
                raise WrongInputFormatError
            data_set_columns = data_set_info.data_set.columns.tolist()
            if second_column_pair_name not in data_set_columns:
                raise MissingFirstColumnPairError
            if first_column_pair_name not in data_set_columns:
                raise MissingSecondColumnPairError