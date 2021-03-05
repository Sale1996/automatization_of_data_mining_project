from data_sets_reporter.classes.data_set_string_reporter.data_set_validator.data_set_report_validator import DataSetValidator
from data_sets_reporter.classes.data_set_string_reporter.report_generator.data_set_reporter import DataSetReporter
from data_sets_reporter.classes.report_generator import ReportGenerator


class FacadeStringDataSetReporter(DataSetReporter):

    def __init__(self, report_generator: ReportGenerator, data_set_validator: DataSetValidator):
        self.report_generator = report_generator
        self.data_set_validator = data_set_validator

    def get_report_listing_of_data_sets(self, data_sets):
        self.data_set_validator.validate(data_sets)
        return self.report_generator.generate_report(data_sets)

