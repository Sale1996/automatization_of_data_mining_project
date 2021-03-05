from data_sets_reporter.classes.data_set_reporter import DataSetReporter
from data_sets_reporter.exceptions.register_exeptions import WrongInputFormatError, NonIterableObjectError


class DefaultDataSetReporter(DataSetReporter):
    def get_report_listing_of_data_sets(self, data_sets):
        self.__check_validation_of_data_sets(data_sets)

        if data_sets.__len__() == 0:
            return self.get_report_string_for_empty_data_set_list()

        return self.__generate_report(data_sets)

    def get_report_string_for_empty_data_set_list(self):
        return self.report_generator.get_report_string_for_empty_data_set_list()

    def __check_validation_of_data_sets(self, data_sets):
        self.__check_is_none(data_sets)
        self.__check_is_not_an_array(data_sets)
        self.__check_elements_of_array(data_sets)

    def __check_is_none(self, data_sets):
        if data_sets is None:
            raise WrongInputFormatError

    def __check_is_not_an_array(self, data_sets):
        if not isinstance(data_sets, list):
            raise NonIterableObjectError

    def __check_elements_of_array(self, array):
        for element in array:
            self.__check_has_element_correct_length(element)
            self.__check_is_first_element_typeof_string(element)
            self.__check_if_second_element_typeof_list(element)
            self.__check_if_list_elements_are_typeof_string(element)

    def __check_has_element_correct_length(self, element):
        if element.__len__() != 2:
            raise WrongInputFormatError

    def __check_is_first_element_typeof_string(self, element):
        if not isinstance(element[0], str):
            raise WrongInputFormatError

    def __check_if_second_element_typeof_list(self, element):
        if not isinstance(element[1], list):
            raise WrongInputFormatError

    def __check_if_list_elements_are_typeof_string(self, element):
        if element[1].__len__() > 0:
            for column_name in element[1]:
                if not isinstance(column_name, str):
                    raise WrongInputFormatError

    def __generate_report(self, data_sets):
        report = ""

        for data_set in data_sets:
            report += self.report_generator.generate_data_set_title(data_set[0])
            report += self.report_generator.generate_columns_string_report(data_set[1])

        return report


