from typing import List

from data_set_statistic_reporter.classes.data_class.statistic_reporter_data_class import StatisticReporterDataClass
from data_set_statistic_reporter.classes.statistic_reporter_data_set.statistic_reporter_data_set import \
    StatisticReporterDataSet


class DataSetStatisticReporterImpl(StatisticReporterDataSet):
    def get_statistics_as_data_set(self, statistic_objects: List[StatisticReporterDataClass]):
        data_sets_statistic = []

        for element in statistic_objects:
            data_sets_statistic.append([element.data_set_name])

            statistic_column_names, statistic_column_values = self.generate_statistic_column_name_and_value(element)

            data_sets_statistic.append(statistic_column_names)
            data_sets_statistic.append(statistic_column_values)

        return data_sets_statistic

    def generate_statistic_column_name_and_value(self, element):
        statistic_column_names = []
        statistic_column_values = []

        for generator in element.statistic_generators:
            generated_column_names, generated_column_values = generator.generate_statistic(element.data_set)
            statistic_column_names.extend(generated_column_names)
            statistic_column_values.extend(generated_column_values)

        return statistic_column_names, statistic_column_values
