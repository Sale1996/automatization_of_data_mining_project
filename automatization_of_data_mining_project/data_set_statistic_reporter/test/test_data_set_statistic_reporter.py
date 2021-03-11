import unittest

from data_set_statistic_reporter.classes.statistic_generator.implementations.column_names_statistic_generator import \
    ColumnNamesStatisticGenerator
from data_set_statistic_reporter.classes.statistic_generator.implementations.missing_data_statistic_generator import \
    MissingDataStatisticGenerator
from data_set_statistic_reporter.classes.statistic_generator.implementations.range_statistic_generator import \
    RangeStatisticGenerator
from data_set_statistic_reporter.classes.statistic_generator.implementations.unique_impression_statistic_generator import \
    UniqueImpressionStatisticGenerator
from data_set_statistic_reporter.classes.statistic_generator.implementations.variance_statistic_generator import \
    VarianceStatisticGenerator
from data_set_statistic_reporter.classes.data_class.statistic_reporter_data_class import StatisticReporterDataClass
from data_set_statistic_reporter.depedency_injector.container import Container

import pandas as pd


class DataSetStatisticReporterTestBase(unittest.TestCase):
    pass


class DataSetStatisticGeneratorTestDummyCases(DataSetStatisticReporterTestBase):
    def setUp(self):
        self.data_set_statistic_reporter = Container.statistic_reporter_data_set()
        self.columns_statistic_generator = ColumnNamesStatisticGenerator([])
        self.range_statistic_generator = RangeStatisticGenerator(['Year'])
        self.unique_impression_statistic_generator = UniqueImpressionStatisticGenerator(['Country Code'])
        self.variance_statistic_generator = VarianceStatisticGenerator(["Year"])
        self.missing_data_statistic_generator = MissingDataStatisticGenerator(["Test"])

    def test_given_empty_statistic_object_when_get_statistics_as_data_set_then_return_only_data_set_name_with_two_empty_arrays(
            self):
        empty_statistic_object = StatisticReporterDataClass("Test", pd.DataFrame([]), [])
        expected_return_value = [["Test"], [], []]

        self.assertEqual(expected_return_value,
                         self.data_set_statistic_reporter.get_statistics_as_data_set([empty_statistic_object]))

    def test_given_statistic_object_with_range_generator_when_get_statistics_as_data_set_then_return_data_set_name_with_range_statistics(
            self):
        data_frame_columns, data_frame_values = self.get_test_data_frame_values_and_columns()
        data_set_with_range_report = StatisticReporterDataClass(
            "Test", pd.DataFrame(data_frame_values, columns=data_frame_columns),
            [self.columns_statistic_generator, self.range_statistic_generator]
        )

        expected_return_value = [["Test"], ["Columns", "Year - Range"],
                                 ["Year, Country Code, Test", "1900-2020"]]

        self.assertEqual(expected_return_value,
                         self.data_set_statistic_reporter.get_statistics_as_data_set([data_set_with_range_report]))

    def test_given_statistic_object_with_unique_impression_report_array_when_reports_statistic_then_return_data_set_name_with_unique_impression_report(
            self):
        data_frame_columns, data_frame_values = self.get_test_data_frame_values_and_columns()
        data_set_with_unique_impression_report = StatisticReporterDataClass(
            "Test", pd.DataFrame(data_frame_values, columns=data_frame_columns),
            [self.columns_statistic_generator, self.unique_impression_statistic_generator]
        )

        expected_return_value = [["Test"], ["Columns", "Country Code - Unique impressions"],
                                 ["Year, Country Code, Test", 4]]

        self.assertEqual(expected_return_value,
                         self.data_set_statistic_reporter.get_statistics_as_data_set(
                             [data_set_with_unique_impression_report]))

    def test_given_statistic_object_with_missing_data_report_array_when_reports_statistic_then_return_data_set_name_with_missing_data_report(
            self):
        data_frame_columns, data_frame_values = self.get_test_data_frame_values_and_columns()
        data_set_with_missing_data_report = StatisticReporterDataClass(
            "Test", pd.DataFrame(data_frame_values, columns=data_frame_columns),
            [self.columns_statistic_generator, self.missing_data_statistic_generator]
        )

        expected_return_value = [["Test"], ["Columns",
                                            "Test - Total number of data",
                                            "Test - Total number of missing data",
                                            "Test - Total percent of missing data"],
                                 ["Year, Country Code, Test", 6, 1, 16.67]]

        self.assertEqual(expected_return_value,
                         self.data_set_statistic_reporter.get_statistics_as_data_set(
                             [data_set_with_missing_data_report]))

    def test_given_statistic_object_with_variance_report_array_when_reports_statistic_then_return_data_set_name_with_normal_distribution_report(
            self):
        data_frame_columns, data_frame_values = self.get_test_data_frame_values_and_columns()
        data_set_with_variance_report = StatisticReporterDataClass(
            "Test", pd.DataFrame(data_frame_values, columns=data_frame_columns),
            [self.columns_statistic_generator, self.variance_statistic_generator]
        )

        expected_return_value = [["Test"], ["Columns",
                                            "Year - Mean value",
                                            "Year - Standard deviation",
                                            "Year - Variance"],
                                 ["Year, Country Code, Test", 1978, 41, 1687.22]]

        self.assertEqual(expected_return_value,
                         self.data_set_statistic_reporter.get_statistics_as_data_set(
                             [data_set_with_variance_report]))

    def test_given_statistic_object_with_multiple_report_arrays_when_reports_statistic_then_return_data_set_name_with_required_statistics(
            self):
        data_frame_columns, data_frame_values = self.get_test_data_frame_values_and_columns()
        data_set_with_multiple_reports = StatisticReporterDataClass(
            "Test", pd.DataFrame(data_frame_values, columns=data_frame_columns),
            [self.columns_statistic_generator, self.range_statistic_generator,
             self.unique_impression_statistic_generator,
             self.variance_statistic_generator, self.missing_data_statistic_generator]
        )

        expected_return_value = [["Test"], ["Columns", "Year - Range", "Country Code - Unique impressions",
                                            "Year - Mean value", "Year - Standard deviation",
                                            "Year - Variance", "Test - Total number of data",
                                            "Test - Total number of missing data",
                                            "Test - Total percent of missing data"],
                                 ["Year, Country Code, Test", "1900-2020", 4, 1978, 41, 1687.22, 6, 1, 16.67]]

        self.assertEqual(expected_return_value,
                         self.data_set_statistic_reporter.get_statistics_as_data_set(
                             [data_set_with_multiple_reports]))

    def test_given_two_statistic_object_with_multiple_report_arrays_when_reports_statistic_then_return_data_set_name_with_required_statistics(
            self):
        data_frame_1_columns, data_frame_1_values = self.get_test_data_frame_values_and_columns()
        data_frame_2_values = [
            ["SRB", 1], ["JPN", 2], ["RUS", ], ["SRB", 4], ["ESP", 5],
            ["JPN", 6]]
        data_frame_2_columns = ['Country Code', 'Test']
        data_set_1_with_multiple_reports = StatisticReporterDataClass(
            "Test", pd.DataFrame(data_frame_1_values, columns=data_frame_1_columns),
            [self.columns_statistic_generator, self.range_statistic_generator, self.unique_impression_statistic_generator,
             self.variance_statistic_generator, self.missing_data_statistic_generator]
        )
        data_set_2_with_multiple_reports = StatisticReporterDataClass(
            "Test", pd.DataFrame(data_frame_2_values, columns=data_frame_2_columns),
            [self.columns_statistic_generator, self.unique_impression_statistic_generator,
             self.missing_data_statistic_generator]
        )

        expected_return_value = [["Test"], ["Columns", "Year - Range", "Country Code - Unique impressions",
                                            "Year - Mean value", "Year - Standard deviation",
                                            "Year - Variance", "Test - Total number of data",
                                            "Test - Total number of missing data",
                                            "Test - Total percent of missing data"],
                                 ["Year, Country Code, Test", "1900-2020", 4, 1978, 41, 1687.22, 6, 1, 16.67],
                                 ["Test"], ["Columns", "Country Code - Unique impressions",
                                            "Test - Total number of data",
                                            "Test - Total number of missing data",
                                            "Test - Total percent of missing data"],
                                 ["Country Code, Test", 4, 6, 1, 16.67]
                                 ]

        self.assertEqual(expected_return_value,
                         self.data_set_statistic_reporter.get_statistics_as_data_set(
                             [data_set_1_with_multiple_reports, data_set_2_with_multiple_reports]))

    def get_test_data_frame_values_and_columns(self):
        data_frame_values = [
            [1900, "SRB", 1], [1950, "JPN", 2], [1990, "RUS", ], [2010, "SRB", 4], [2020, "ESP", 5], [1996, "JPN", 6]]
        data_frame_columns = ['Year', 'Country Code', 'Test']

        return data_frame_columns, data_frame_values
