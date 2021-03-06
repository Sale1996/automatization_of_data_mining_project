from typing import List

from data_set_info_data_class.data_class.data_set_info import DataSetInfo
from data_set_remover.classes.remover_validator.manually_remover_validator.manually_remover_validator import \
    ManuallyRemoverValidator
from data_set_remover.exceptions.remover_exceptions import WrongInputFormatError, NonExistingDataSetWithGivenNameError, \
    NonIterableObjectError


class DeleteByNameRemoverValidator(ManuallyRemoverValidator):
    def validate(self, data_sets_info: List[DataSetInfo], data_set_name: str):
        self.__check_input_format(data_set_name, data_sets_info)
        self.__check_is_there_data_set_with_name(data_set_name, data_sets_info)

    def __check_input_format(self, data_set_name, data_sets_info):
        self.__check_if_inputs_are_none(data_set_name, data_sets_info)
        self.__is_not_iterable_object(data_sets_info)
        self.__is_right_format(data_set_name, str)
        for data_set_info in data_sets_info:
            self.__is_right_format(data_set_info, DataSetInfo)

    def __check_if_inputs_are_none(self, data_set_name, data_sets_info):
        if data_sets_info is None or data_set_name is None:
            raise WrongInputFormatError

    def __is_not_iterable_object(self, object):
        if not isinstance(object, list):
            raise NonIterableObjectError

    def __is_right_format(self, object, format):
        if not isinstance(object, format):
            raise WrongInputFormatError

    def __check_is_there_data_set_with_name(self, data_set_name, data_sets_info):
        data_set_name_found = False
        for data_set_info in data_sets_info:
            if data_set_name == data_set_info.data_set_name:
                data_set_name_found = True
        if not data_set_name_found:
            raise NonExistingDataSetWithGivenNameError