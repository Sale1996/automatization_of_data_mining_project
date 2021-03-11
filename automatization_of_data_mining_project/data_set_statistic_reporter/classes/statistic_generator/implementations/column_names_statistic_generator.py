from typing import List

from data_set_statistic_reporter.classes.statistic_generator.statistic_generator import StatisticGenerator


class ColumnNamesStatisticGenerator(StatisticGenerator):
    def generate_statistic(self, data_set) -> (List[str], List[str]):
        statistic_column_names = []
        statistic_column_values = []

        data_set_columns = data_set.columns.tolist()
        if len(data_set_columns) > 0:
            statistic_column_names.append("Columns")
            column_names = self.get_column_names_in_one_string(data_set_columns)
            statistic_column_values.append(column_names)

        return statistic_column_names, statistic_column_values

    def get_column_names_in_one_string(self, data_set_columns):
        columns_report = ''
        for column_name in data_set_columns[:-1]:
            columns_report += column_name + ', '
        columns_report += data_set_columns[-1]
        return columns_report
