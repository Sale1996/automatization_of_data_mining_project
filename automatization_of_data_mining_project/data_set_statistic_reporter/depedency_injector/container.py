from dependency_injector import containers, providers

from data_set_statistic_reporter.classes.facade_statistic_reporter import FacadeStatisticReporter
from data_set_statistic_reporter.classes.input_validator.statistic_data_object_validator import \
    StatisticDataObjectValidator
from data_set_statistic_reporter.classes.statistic_reporter_data_set.statistic_reporter_data_set_impl import \
    DataSetStatisticReporterImpl
from data_set_statistic_reporter.classes.statistics_printer.document_statistics_printer import DocumentStatisticsPrinter


class Container(containers.DeclarativeContainer):
    input_validator = providers.Factory(StatisticDataObjectValidator)
    statistic_reporter_data_set = providers.Factory(DataSetStatisticReporterImpl)
    statistics_printer = providers.Factory(DocumentStatisticsPrinter)

    statistics_reporter = providers.Factory(FacadeStatisticReporter,
                                            input_validator=input_validator,
                                            statistic_reporter_data_set=statistic_reporter_data_set,
                                            statistics_printer=statistics_printer)