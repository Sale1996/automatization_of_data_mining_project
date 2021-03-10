from data_set_statistic_reporter.classes.statistic_generator.statistic_generator import StatisticGenerator


class MissingDataStatisticGenerator(StatisticGenerator):
    def generate_statistic(self, data_set):
        statistic_column_names = []
        statistic_column_values = []

        for column_name in self.column_names:
            statistic_column_names.extend(self.get_column_names(column_name))
            statistic_column_values.extend(self.get_column_values(column_name, data_set))

        return statistic_column_names, statistic_column_values

    def get_column_names(self, column_name):
        column_names = []

        column_names.append(column_name + " - Total number of data")
        column_names.append(column_name + " - Total number of missing data")
        column_names.append(column_name + " - Total percent of missing data")

        return column_names

    def get_column_values(self, column_name, data_set):
        column_values = []

        percent_of_missing_data, total_number_of_data, total_number_of_missing_data = self.calculate_data_statistics(
            column_name, data_set)

        column_values.append(total_number_of_data)
        column_values.append(total_number_of_missing_data)
        column_values.append(percent_of_missing_data)

        return column_values

    def calculate_data_statistics(self, column_name, data_set):
        total_number_of_data = data_set[column_name].shape[0]
        total_number_of_missing_data = data_set[column_name].isnull().sum()
        percent_of_missing_data = round(total_number_of_missing_data / total_number_of_data * 100, 2)
        return percent_of_missing_data, total_number_of_data, total_number_of_missing_data
