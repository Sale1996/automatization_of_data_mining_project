from data_sets_reporter.classes.report_generator import ReportGenerator


class DefaultReportGenerator(ReportGenerator):

    def get_report_string_for_empty_data_set_list(self):
        return "THERE IS NO DATA SET TO LIST\n\n\n"

    def generate_data_set_title(self, data_set_title):
        return "\n" + data_set_title + "\n\n"

    def generate_columns_string_report(self, data_set_columns):
        report = ""
        report += "Columns:\n\n"

        for column in data_set_columns[:-1]:
            report += column + " || "
        report += data_set_columns[-1] + "\n\n\n==========\n"

        return report
