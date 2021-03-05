from dependency_injector import containers, providers
from data_sets_reporter.classes.implementations.default_data_set_reporter import DefaultDataSetReporter
from data_sets_reporter.classes.implementations.default_report_generator import DefaultReportGenerator


class Container(containers.DeclarativeContainer):
    report_generator = providers.Factory(DefaultReportGenerator)
    data_set_reporter = providers.Factory(DefaultDataSetReporter, report_generator=report_generator)
