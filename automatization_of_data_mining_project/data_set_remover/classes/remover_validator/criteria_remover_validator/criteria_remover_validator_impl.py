from data_set_remover.classes.data_class.data_for_criteria_remove import DataForCriteriaRemove
from data_set_remover.classes.remover_validator.criteria_remover_validator.criteria_remover_validator import \
    CriteriaRemoverValidator
from data_set_remover.exceptions.remover_exceptions import WrongInputFormatError, ColumnArraysShouldNotBeBothEmpty, \
    ColumnArraysShouldNotBeBothFilled, WrongCriteriaNameError, MissingColumnToIncludeError, NonIterableObjectError


class CriteriaRemoverValidatorImpl(CriteriaRemoverValidator):
    def validate(self, criteria_remover_data: DataForCriteriaRemove):
        self.__valid_criteria_input(criteria_remover_data, self.criteria_column_validators)

    def __valid_criteria_input(self, criteria_remover_data, criteria_column_validators):
        self.__check_input_format(criteria_remover_data)
        self.__check_column_inclusion_exclusion_arrays(criteria_remover_data.columns_to_include,
                                                     criteria_remover_data.columns_to_exclude)
        self.__check_is_criteria_validator_with_given_name_contained(criteria_remover_data.criteria_name, criteria_column_validators)
        self.__check_if_there_is_missing_one_of_elements_from_inclusion_column_array_in_data_sets(criteria_remover_data.data_sets_info,
                                                                                                criteria_remover_data.columns_to_include)
        self.__check_criteria_value(criteria_remover_data.criteria_name, criteria_remover_data.criteria_value,
                                  criteria_column_validators)

    def __check_column_inclusion_exclusion_arrays(self, columns_to_include, columns_to_exclude):
        if not columns_to_include and not columns_to_exclude:
            raise ColumnArraysShouldNotBeBothEmpty
        if columns_to_include and columns_to_exclude:
            raise ColumnArraysShouldNotBeBothFilled

    def __check_criteria_value(self, criteria_name, criteria_value, criteria_column_validators):
        for criteria_value_validator in criteria_column_validators:
            if criteria_value_validator.criteria_name == criteria_name:
                criteria_value_validator.is_criteria_value_valid(criteria_value)

    def __check_if_there_is_missing_one_of_elements_from_inclusion_column_array_in_data_sets(self, data_sets_info, columns_to_include):
        for data_set_info in data_sets_info:
            data_set_columns = data_set_info.data_set.columns.tolist()
            for column_to_include in columns_to_include:
                if column_to_include not in data_set_columns:
                    raise MissingColumnToIncludeError

    def __check_is_criteria_validator_with_given_name_contained(self, criteria_name, criteria_column_validators):
        is_criteria_name_contained = False
        for criteria_value_validator in criteria_column_validators:
            if criteria_value_validator.criteria_name == criteria_name:
                is_criteria_name_contained = True
        if not is_criteria_name_contained:
            raise WrongCriteriaNameError

    def __check_input_format(self, criteria_remover_data):
        self.__check_is_none(criteria_remover_data)
        self.__check_if_not_iterable(criteria_remover_data)
        self.__is_right_format(criteria_remover_data.criteria_name, str)
        self.__is_right_format(criteria_remover_data.criteria_value, int)
        self.__check_right_format_of_list_elements(criteria_remover_data.columns_to_include, str)
        self.__check_right_format_of_list_elements(criteria_remover_data.columns_to_exclude, str)

    def __check_right_format_of_list_elements(self, list_to_check, format):
        for element in list_to_check:
            self.__is_right_format(element, format)

    def __check_if_not_iterable(self, criteria_remover_data):
        self.__is_not_iterable_object(criteria_remover_data.data_sets_info)
        self.__is_not_iterable_object(criteria_remover_data.columns_to_exclude)
        self.__is_not_iterable_object(criteria_remover_data.columns_to_include)

    def __check_is_none(self, object):
        if object is None:
            raise WrongInputFormatError

    def __is_right_format(self, object, format):
        if not isinstance(object, format):
            raise WrongInputFormatError

    def __is_not_iterable_object(self, object):
        if not isinstance(object, list):
            raise NonIterableObjectError
