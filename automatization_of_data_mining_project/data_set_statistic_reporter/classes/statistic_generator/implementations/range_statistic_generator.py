from data_set_statistic_reporter.classes.statistic_generator.statistic_generator import StatisticGenerator


class RangeStatisticGenerator(StatisticGenerator):
    def generate_statistic(self, data_set):
        statistic_column_names = []
        statistic_column_values = []

        for column_name in self.column_names:
            statistic_column_names.append(self.get_column_name(column_name))
            statistic_column_values.append(self.get_column_value(column_name, data_set))

        return statistic_column_names, statistic_column_values

    def get_column_name(self, column_name):
        return column_name + ' - Range'

    def get_column_value(self, column_name, data_set):
        max_value, min_value = self.get_min_and_max_value(column_name, data_set)
        return str(min_value) + "-" + str(max_value)

    def get_min_and_max_value(self, column_name, data_set):
        data_set_with_range_column = data_set[[column_name]]
        min_value = data_set_with_range_column.min().values[0]
        max_value = data_set_with_range_column.max().values[0]
        return max_value, min_value
