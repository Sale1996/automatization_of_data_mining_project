from data_sets_reporter.classes.report_generator import ReportGenerator


class StringReportGenerator(ReportGenerator):

    def generate_report(self, data_sets):
        if data_sets.__len__() == 0:
            return self.__get_report_string_for_empty_data_set_list()

        report = ""

        for data_set in data_sets:
            report += self.__generate_data_set_title(data_set[0])
            report += self.__generate_columns_string_report(data_set[1])

        return report

    def __get_report_string_for_empty_data_set_list(self):
        return "THERE IS NO DATA SET TO LIST\n\n\n"

    def __generate_data_set_title(self, data_set_title):
        return "\n" + data_set_title + "\n\n"

    def __generate_columns_string_report(self, data_set_columns):
        report = ""
        report += "Columns:\n\n"

        for column in data_set_columns[:-1]:
            report += column + " || "
        report += data_set_columns[-1] + "\n\n\n==========\n"

        return report
