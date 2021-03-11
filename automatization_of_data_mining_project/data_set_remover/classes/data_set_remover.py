from typing import List

from data_set_remover.classes.data_class.data_for_criteria_remove import DataForCriteriaRemove
from data_set_remover.exceptions.remover_exceptions import WrongInputFormatError, NonIterableObjectError, \
    NonExistingDataSetWithGivenNameError, ColumnArraysShouldNotBeBothEmpty, ColumnArraysCannotBeBothFilled
from data_set_remover.classes.data_class.data_set_info import DataSetInfo


class DataSetRemover(object):
    # MAIN
    def remove_data_set(self, data_sets_info: List[DataSetInfo], data_set_name: str):
        self.valid_input(data_set_name, data_sets_info)
        self.check_is_there_data_set_with_name(data_set_name, data_sets_info)
        return_data_sets_info = self.remove_data_set_with_name(data_set_name, data_sets_info)

        return return_data_sets_info
    # MAIN
    def remove_by_criteria(self, criteria_remover_data: DataForCriteriaRemove):
        self.valid_criteria_input(criteria_remover_data)

    def valid_criteria_input(self, criteria_remover_data):
        if criteria_remover_data is None:
            raise WrongInputFormatError
        self.is_not_iterable_object(criteria_remover_data.data_sets_info)
        self.is_right_format(criteria_remover_data.criteria_name, str)
        self.is_right_format(criteria_remover_data.criteria_value, int)
        self.is_not_iterable_object(criteria_remover_data.columns_to_exclude)
        self.is_not_iterable_object(criteria_remover_data.columns_to_include)
        if not criteria_remover_data.columns_to_include and not criteria_remover_data.columns_to_exclude:
            raise ColumnArraysShouldNotBeBothEmpty
        if criteria_remover_data.columns_to_include and criteria_remover_data.columns_to_exclude:
            raise ColumnArraysCannotBeBothFilled
        for column_to_include in criteria_remover_data.columns_to_include:
            self.is_right_format(column_to_include, str)
        for column_to_exclude in criteria_remover_data.columns_to_exclude:
            self.is_right_format(column_to_exclude, str)

    def valid_input(self, data_set_name, data_sets_info):
        if data_sets_info is None or data_set_name is None:
            raise WrongInputFormatError
        self.is_not_iterable_object(data_sets_info)
        self.is_right_format(data_set_name, str)
        for data_set_info in data_sets_info:
            self.is_right_format(data_set_info, DataSetInfo)

    def is_right_format(self, object, format):
        if not isinstance(object, format):
            raise WrongInputFormatError

    def is_not_iterable_object(self, object):
        if not isinstance(object, list):
            raise NonIterableObjectError

    def check_is_there_data_set_with_name(self, data_set_name, data_sets_info):
        data_set_name_found = False
        for data_set_info in data_sets_info:
            if data_set_name == data_set_info.data_set_name:
                data_set_name_found = True
        if not data_set_name_found:
            raise NonExistingDataSetWithGivenNameError

    def remove_data_set_with_name(self, data_set_name, data_sets_info):
        return_data_sets_info = []
        for data_set_info in data_sets_info:
            if data_set_name != data_set_info.data_set_name:
                return_data_sets_info.append(data_set_info)
        return return_data_sets_info

