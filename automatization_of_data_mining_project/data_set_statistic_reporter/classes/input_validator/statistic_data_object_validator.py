from typing import List

from data_set_statistic_reporter.classes.data_class.statistic_reporter_data_class import StatisticReporterDataClass
from data_set_statistic_reporter.classes.input_validator.input_validator import InputValidator
from data_set_statistic_reporter.exceptions.reporter_exceptions import WrongInputFormatError, NonIterableObjectError


class StatisticDataObjectValidator(InputValidator):
    def validate(self, input: List[StatisticReporterDataClass]):
        self.check_if_input_is_none(input)
        self.check_if_input_is_not_array(input)
        self.check_are_elements_valid_type(input)

    def check_are_elements_valid_type(self, input):
        for element in input:
            if not isinstance(element, StatisticReporterDataClass):
                raise WrongInputFormatError

    def check_if_input_is_not_array(self, input):
        if not isinstance(input, list):
            raise NonIterableObjectError

    def check_if_input_is_none(self, input):
        if input is None:
            raise WrongInputFormatError
