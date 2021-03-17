from typing import List

from termcolor import colored

from data_set_info_data_class.data_class.data_set_info import DataSetInfo
from data_sets_reporter.exceptions.register_exeptions import WrongInputFormatError, NonIterableObjectError
from data_sets_reporter import Reporter
from data_sets_reporter.classes.data_class.data_set_info_for_reporter import DataSetInfoForReporter

ERROR_STRING = colored('\n@ERROR ', 'red')
ERROR_RETURN_VALUE = -1


def print_quick_info_of_loaded_data_sets(loaded_data_sets: List[DataSetInfo]):
    data_sets_reporter = Reporter()
    data_sets_information_for_reporter = get_data_for_data_set_reporter(loaded_data_sets)

    try:
        report = data_sets_reporter.get_report_listing_of_data_sets(data_sets_information_for_reporter)
        secondary_menu = ('-----------------------------------------------------\n'
                          '|            List of uploaded data sets             |\n'
                          '-----------------------------------------------------\n')
        print(secondary_menu)
        print(report)
    except WrongInputFormatError:
        print(ERROR_STRING, "Input for data set reporter is invalid!\n")
        return
    except NonIterableObjectError:
        print(ERROR_STRING, "Input for data set reporter is not iterable!\n")
        return


def get_data_for_data_set_reporter(loaded_data_sets):
    data_sets_information_for_reporter: List[DataSetInfoForReporter] = []
    for data_set_info in loaded_data_sets:
        data_set_columns = data_set_info.data_set.columns.tolist()
        data_set_information_for_reporter = DataSetInfoForReporter(data_set_info.data_set_name,
                                                                   data_set_columns)

        data_sets_information_for_reporter.append(data_set_information_for_reporter)
    return data_sets_information_for_reporter
