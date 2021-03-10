from typing import List

from data_set_statistic_reporter.classes.input_validator.input_validator import InputValidator
from data_set_statistic_reporter.classes.statistic_reporter import StatisticReporter
from data_set_statistic_reporter.classes.data_class.statistic_reporter_data_class import StatisticReporterDataClass
from data_set_statistic_reporter.classes.statistic_reporter_data_set.statistic_reporter_data_set import \
    StatisticReporterDataSet
from data_set_statistic_reporter.classes.statistics_printer.statistics_printer import StatisticsPrinter


class FacadeStatisticReporter(StatisticReporter):
    def __init__(self, input_validator: InputValidator, statistic_reporter_data_set: StatisticReporterDataSet, statistics_printer: StatisticsPrinter):
        self.input_validator = input_validator
        self.statistic_reporter_data_set = statistic_reporter_data_set
        self.statistics_printer = statistics_printer

    def print_statistic(self, data_sets_info: List[StatisticReporterDataClass]):
        self.input_validator.validate(data_sets_info)
        statistic_report_as_data_set = self.statistic_reporter_data_set.get_statistics_as_data_set(data_sets_info)
        self.statistics_printer.print_statistics(statistic_report_as_data_set)