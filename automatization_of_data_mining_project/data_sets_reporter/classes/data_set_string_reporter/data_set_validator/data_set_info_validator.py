from typing import List

from data_sets_reporter.classes.data_class.data_set_info_for_reporter import DataSetInfoForReporter
from data_sets_reporter.classes.data_set_string_reporter.data_set_validator.data_set_report_validator import DataSetValidator
from data_sets_reporter.exceptions.register_exeptions import WrongInputFormatError, NonIterableObjectError


class DataSetInfoValidator(DataSetValidator):
    def validate(self, data_sets_info: List[DataSetInfoForReporter]):
        self.__check_is_none(data_sets_info)
        self.__check_is_not_an_array(data_sets_info)
        self.__check_elements_of_array(data_sets_info)

    def __check_is_none(self, data_sets):
        if data_sets is None:
            raise WrongInputFormatError

    def __check_is_not_an_array(self, data_sets):
        if not isinstance(data_sets, list):
            raise NonIterableObjectError

    def __check_elements_of_array(self, array):
        for element in array:
            self.__check_if_element_is_instance_of_data_set_info_class(element)
            self.__check_is_first_element_typeof_string(element)
            self.__check_if_second_element_typeof_list(element)
            self.__check_if_list_elements_are_typeof_string(element)

    def __check_if_element_is_instance_of_data_set_info_class(self, element):
        if not isinstance(element, DataSetInfoForReporter):
            raise WrongInputFormatError

    def __check_is_first_element_typeof_string(self, element):
        if not isinstance(element.data_set_name, str):
            raise WrongInputFormatError

    def __check_if_second_element_typeof_list(self, element):
        if not isinstance(element.data_set_columns, list):
            raise WrongInputFormatError

    def __check_if_list_elements_are_typeof_string(self, element):
        if element.data_set_columns.__len__() > 0:
            for column_name in element.data_set_columns:
                if not isinstance(column_name, str):
                    raise WrongInputFormatError
