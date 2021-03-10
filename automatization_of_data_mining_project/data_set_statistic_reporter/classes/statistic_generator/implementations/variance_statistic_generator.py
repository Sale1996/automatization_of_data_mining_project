import math

from data_set_statistic_reporter.classes.statistic_generator.statistic_generator import StatisticGenerator


class VarianceStatisticGenerator(StatisticGenerator):
    def generate_statistic(self, data_set):
        statistic_column_names = []
        statistic_column_values = []

        for column_name in self.column_names:
            statistic_column_names.extend(self.get_column_names(column_name))
            statistic_column_values.extend(self.get_column_values(column_name, data_set))

        return statistic_column_names, statistic_column_values

    def get_column_names(self, column_name):
        column_names = []
        column_names.append(column_name + " - Mean value")
        column_names.append(column_name + " - Standard deviation")
        column_names.append(column_name + " - Variance")
        return column_names

    def get_column_values(self, column_name, data_set):
        column_values = []

        mean, standard_deviation, variance = self.get_variance_data(column_name, data_set)

        column_values.append(round(mean))
        column_values.append(round(standard_deviation))
        column_values.append(round(variance, 2))

        return column_values

    def get_variance_data(self, column_name, data_set):
        data_set_column_rows = data_set[column_name]

        n = data_set_column_rows.shape[0]
        mean = data_set_column_rows.sum() / n

        variance = self.calculate_variance(data_set_column_rows, mean, n)

        standard_deviation = math.sqrt(variance)

        return mean, standard_deviation, variance

    def calculate_variance(self, data_set_column_rows, mean, n):
        deviations = [(x - mean) ** 2 for x in data_set_column_rows.values]
        variance = sum(deviations) / n
        return variance
