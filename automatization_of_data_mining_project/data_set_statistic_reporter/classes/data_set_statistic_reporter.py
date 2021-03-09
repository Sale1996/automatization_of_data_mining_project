from typing import List
import math

from data_set_statistic_reporter.exceptions.reporter_exceptions import WrongInputFormatError, NonIterableObjectError
from data_set_statistic_reporter.classes.statistic_reporter_data_class import StatisticReporterDataClass


class DataSetStatisticReporter(object):
    def report_data_sets_statistics(self, data_sets: List[StatisticReporterDataClass]):
        self.validate_input(data_sets)

        data_sets_statistic = []

        for element in data_sets:
            element_name = element.data_set_name
            data_sets_statistic.append([element_name])

            statistic_column_names = []
            statistic_column_values = []
            '''
                NAPRAVI ABSTRAKCIJU ZA SVE METODE I ONDA SAMO IDI KROZ LISTU TIH METODA
                TAKO DA CE KASNIJE SE MOCI DODATI I NEKI 5. STATISTIC
            '''
            self.add_range_statistics(element, statistic_column_names, statistic_column_values)
            self.add_unique_impression_statistics(element, statistic_column_names, statistic_column_values)
            self.add_variance_statistics(element, statistic_column_names, statistic_column_values)
            self.add_missing_data_statistics(element, statistic_column_names, statistic_column_values)

            data_sets_statistic.append(statistic_column_names)
            data_sets_statistic.append(statistic_column_values)

        return data_sets_statistic

    def add_variance_statistics(self, element, statistic_column_names, statistic_column_values):
        for column_for_variation_report in element.columns_for_variation_report:
            statistic_column_names.append(column_for_variation_report + " - Mean value")
            statistic_column_names.append(column_for_variation_report + " - Standard deviation")
            statistic_column_names.append(column_for_variation_report + " - Variance")

            column_to_investigate = element.data_set[column_for_variation_report]

            n = column_to_investigate.shape[0]
            mean = column_to_investigate.sum() / n
            deviations = [(x - mean) ** 2 for x in column_to_investigate.values]
            variance = sum(deviations) / n
            standard_deviation = math.sqrt(variance)

            statistic_column_values.append(round(mean))
            statistic_column_values.append(round(standard_deviation))
            statistic_column_values.append(round(variance, 2))

    def add_missing_data_statistics(self, element, statistic_column_names, statistic_column_values):
        for column_for_missing_data_report in element.columns_for_missing_data_statistic_report:
            statistic_column_names.append(column_for_missing_data_report + " - Total number of data")
            statistic_column_names.append(column_for_missing_data_report + " - Total number of missing data")
            statistic_column_names.append(column_for_missing_data_report + " - Total percent of missing data")

            total_number_of_data = element.data_set[column_for_missing_data_report].shape[0]
            total_number_of_missing_data = element.data_set[column_for_missing_data_report].isnull().sum()
            percent_of_missing_data = round(total_number_of_missing_data / total_number_of_data * 100, 2)

            statistic_column_values.append(total_number_of_data)
            statistic_column_values.append(total_number_of_missing_data)
            statistic_column_values.append(percent_of_missing_data)

    def add_unique_impression_statistics(self, element, statistic_column_names, statistic_column_values):
        for unique_impression_column in element.columns_for_unique_impression_report:
            statistic_column_names.append(unique_impression_column + ' - Unique impressions')
            unique_values = element.data_set[unique_impression_column].value_counts().size
            statistic_column_values.append(unique_values)

    def validate_input(self, data_sets):
        if data_sets is None:
            raise WrongInputFormatError
        if not isinstance(data_sets, list):
            raise NonIterableObjectError
        for element in data_sets:
            if not isinstance(element, StatisticReporterDataClass):
                raise WrongInputFormatError

    def add_range_statistics(self, element, statistic_column_names, statistic_column_values):
        for range_column in element.columns_for_range_report:
            statistic_column_names.append(range_column + ' - Range')

            data_set_with_range_column = element.data_set[[range_column]]
            min_value = data_set_with_range_column.min().values[0]
            max_value = data_set_with_range_column.max().values[0]
            range_string = str(min_value) + "-" + str(max_value)
            statistic_column_values.append(range_string)
