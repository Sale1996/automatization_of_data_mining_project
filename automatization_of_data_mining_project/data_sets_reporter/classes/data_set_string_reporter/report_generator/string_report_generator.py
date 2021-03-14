from typing import List

from data_sets_reporter.classes.data_class.data_set_info_for_reporter import DataSetInfoForReporter
from data_sets_reporter.classes.data_set_string_reporter.report_generator.report_generator import ReportGenerator


class StringReportGenerator(ReportGenerator):

    def generate_report(self, data_sets_info: List[DataSetInfoForReporter]) -> str:
        if data_sets_info.__len__() == 0:
            return self.__get_report_string_for_empty_data_set_list()

        report = ""

        for data_set in data_sets_info:
            report += self.__generate_data_set_title(data_set.data_set_name)
            report += self.__generate_columns_string_report(data_set.data_set_columns)

        return report

    def __get_report_string_for_empty_data_set_list(self):
        return "THERE IS NO DATA SET TO LIST\n\n\n"

    def __generate_data_set_title(self, data_set_title):
        return "Data set name: " + data_set_title + "\n"

    def __generate_columns_string_report(self, data_set_columns):
        report = ""
        report += "Columns: "

        for column in data_set_columns[:-1]:
            report += column + " || "
        report += data_set_columns[-1] + "\n\n==========\n\n"

        return report
