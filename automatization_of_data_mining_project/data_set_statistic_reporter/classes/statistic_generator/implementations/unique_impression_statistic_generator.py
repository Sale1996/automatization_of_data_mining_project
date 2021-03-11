from typing import List

from data_set_statistic_reporter.classes.statistic_generator.statistic_generator import StatisticGenerator


class UniqueImpressionStatisticGenerator(StatisticGenerator):
    def generate_statistic(self, data_set) -> (List[str], List[str]):
        statistic_column_names = []
        statistic_column_values = []

        for column_name in self.column_names:
            statistic_column_names.append(self.get_column_name(column_name))
            statistic_column_values.append(self.get_column_value(column_name, data_set))

        return statistic_column_names, statistic_column_values

    def get_column_name(self, column_name):
        return column_name + ' - Unique impressions'

    def get_column_value(self, column_name, data_set):
        unique_values = data_set[column_name].value_counts().size
        return unique_values