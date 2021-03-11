from dependency_injector import containers, providers
from data_sets_reporter.classes.data_set_string_reporter.facade_string_data_set_reporter import FacadeStringDataSetReporter
from data_sets_reporter.classes.data_set_string_reporter.report_generator.string_report_generator import StringReportGenerator
from data_sets_reporter.classes.data_set_string_reporter.data_set_validator.data_set_info_validator import \
    DataSetInfoValidator


class Container(containers.DeclarativeContainer):
    data_set_validator = providers.Factory(DataSetInfoValidator)
    report_generator = providers.Factory(StringReportGenerator)
    data_set_reporter = providers.Factory(
        FacadeStringDataSetReporter, report_generator=report_generator, data_set_validator=data_set_validator)
