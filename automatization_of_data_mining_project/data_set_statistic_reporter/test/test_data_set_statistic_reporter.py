import unittest

from data_set_statistic_reporter.classes.data_set_statistic_reporter import DataSetStatisticReporter
from data_set_statistic_reporter.classes.statistic_reporter_data_class import StatisticReporterDataClass
from data_set_statistic_reporter.exceptions.reporter_exceptions import WrongInputFormatError, NonIterableObjectError

import pandas as pd


class DataSetStatisticReporterTestBase(unittest.TestCase):
    pass


class DataSetStatisticGeneratorTestErrorCases(DataSetStatisticReporterTestBase):
    def setUp(self):
        self.data_set_statistic_reporter = DataSetStatisticReporter()

    def test_given_none_when_reports_statistics_then_throw_invalid_format_exception(self):
        with self.assertRaises(WrongInputFormatError):
            self.data_set_statistic_reporter.report_data_sets_statistics(None)

    def test_given_non_array_object_when_reports_statistics_then_throw_invalid_format_exception(self):
        non_iterable_object = 1

        with self.assertRaises(NonIterableObjectError):
            self.data_set_statistic_reporter.report_data_sets_statistics(non_iterable_object)

    def test_given_array_object_with_wrong_object_as_array_element_when_reports_statistics_then_throw_invalid_format_exception(
            self):
        array_object = [1, 2, 3]

        with self.assertRaises(WrongInputFormatError):
            self.data_set_statistic_reporter.report_data_sets_statistics(array_object)


class DataSetStatisticGeneratorTestDummyCases(DataSetStatisticReporterTestBase):
    def setUp(self):
        self.data_set_statistic_reporter = DataSetStatisticReporter()

    def test_given_empty_statistic_object_when_reports_statistic_then_return_only_data_set_name(self):
        empty_statistic_object = StatisticReporterDataClass(
            "Test", pd.DataFrame([]), [], [], [], [])

        expected_return_value = [["Test"], [], []]
        self.assertEqual(expected_return_value,
                         self.data_set_statistic_reporter.report_data_sets_statistics([empty_statistic_object]))

    def test_given_statistic_object_with_range_report_array_when_reports_statistic_then_return_data_set_name_with_range_report(
            self):
        data_frame_values = [[1, 1], [2, 2], [3, 3], [10, 10]]
        data_frame_columns = ['Test', 'Test2']

        data_set_with_range_report = StatisticReporterDataClass(
            "Test", pd.DataFrame(data_frame_values, columns=data_frame_columns),
            ['Test'], [], [], []
        )

        expected_return_value = [["Test"], ["Test - Range"], ["1-10"]]
        self.assertEqual(expected_return_value,
                         self.data_set_statistic_reporter.report_data_sets_statistics([data_set_with_range_report]))

    def test_given_statistic_object_with_unique_impression_report_array_when_reports_statistic_then_return_data_set_name_with_unique_impression_report(self):
        data_frame_values = [["SRB", 1], ["SPA", 2], ["SRB", 3], ["JPA", 4], ["JPA", 5], ["SRB", 10]]
        data_frame_columns = ['Country Code', 'Test']

        data_set_with_unique_impression_report = StatisticReporterDataClass(
            "Test", pd.DataFrame(data_frame_values, columns=data_frame_columns),
            [], ['Country Code'], [], []
        )

        expected_return_value = [["Test"], ["Country Code - Unique impressions"], [3]]

        self.assertEqual(expected_return_value,
                         self.data_set_statistic_reporter.report_data_sets_statistics([data_set_with_unique_impression_report]))

    def test_given_statistic_object_with_missing_data_report_array_when_reports_statistic_then_return_data_set_name_with_missing_data_report(self):
        data_frame_values = [["SRB", 1], ["SPA", 2], ["SRB", ], ["JPA", 4], ["JPA", ], ["SRB", 10]]
        data_frame_columns = ['Country Code', 'Test']

        data_set_with_missing_data_report = StatisticReporterDataClass(
            "Test", pd.DataFrame(data_frame_values, columns=data_frame_columns),
            [], [], [], ["Test"]
        )

        expected_return_value = [["Test"], ["Test - Total number of data", "Test - Total number of missing data", "Test - Total percent of missing data"],
                                 [6, 2, 33.33]]

        self.assertEqual(expected_return_value,
                         self.data_set_statistic_reporter.report_data_sets_statistics(
                             [data_set_with_missing_data_report]))

    def test_given_statistic_object_with_variance_report_array_when_reports_statistic_then_return_data_set_name_with_normal_distribution_report(self):
        data_frame_values = [[1900, 1], [1950, 2], [1990, 3], [2010, 4], [2020, 5], [1996, 6]]
        data_frame_columns = ['Year', 'Test']

        data_set_with_variance_report = StatisticReporterDataClass(
            "Test", pd.DataFrame(data_frame_values, columns=data_frame_columns),
            [], [], ["Year"], []
        )

        expected_return_value = [["Test"], ["Year - Mean value", "Year - Standard deviation", "Year - Variance"],
                                 [1978, 41, 1687.22]]

        self.assertEqual(expected_return_value,
                         self.data_set_statistic_reporter.report_data_sets_statistics(
                             [data_set_with_variance_report]))

    def test_given_statistic_object_with_multiple_report_arrays_when_reports_statistic_then_return_data_set_name_with_required_statistics(self):
        data_frame_values = [
            [1900, "SRB", 1], [1950, "JPN", 2], [1990, "RUS", ], [2010, "SRB", 4], [2020, "ESP", 5], [1996, "JPN", 6]]

        data_frame_columns = ['Year', 'Country Code', 'Test']

        data_set_with_multiple_reports = StatisticReporterDataClass(
            "Test", pd.DataFrame(data_frame_values, columns=data_frame_columns),
            ['Year'], ['Country Code'], ['Year'],  ['Test']
        )

        expected_return_value = [["Test"], ["Year - Range", "Country Code - Unique impressions",
                                            "Year - Mean value", "Year - Standard deviation",
                                            "Year - Variance", "Test - Total number of data",
                                            "Test - Total number of missing data",
                                            "Test - Total percent of missing data"],
                                 ["1900-2020", 4, 1978, 41, 1687.22, 6, 1, 16.67]]

        self.assertEqual(expected_return_value,
                         self.data_set_statistic_reporter.report_data_sets_statistics(
                             [data_set_with_multiple_reports]))

    def test_given_statistic_object_with_multiple_report_arrays_when_reports_statistic_then_return_data_set_name_with_required_statistics(
            self):
        data_frame_1_values = [
            [1900, "SRB", 1], [1950, "JPN", 2], [1990, "RUS", ], [2010, "SRB", 4], [2020, "ESP", 5],
            [1996, "JPN", 6]]

        data_frame_2_values = [
            ["SRB", 1], ["JPN", 2], ["RUS", ], ["SRB", 4], ["ESP", 5],
            ["JPN", 6]]

        data_frame_1_columns = ['Year', 'Country Code', 'Test']
        data_frame_2_columns = ['Country Code', 'Test']

        data_set_1_with_multiple_reports = StatisticReporterDataClass(
            "Test", pd.DataFrame(data_frame_1_values, columns=data_frame_1_columns),
            ['Year'], ['Country Code'], ['Year'], ['Test']
        )

        data_set_2_with_multiple_reports = StatisticReporterDataClass(
            "Test", pd.DataFrame(data_frame_2_values, columns=data_frame_2_columns),
            [], ['Country Code'], [], ['Test']
        )

        expected_return_value = [["Test"], ["Year - Range", "Country Code - Unique impressions",
                                            "Year - Mean value", "Year - Standard deviation",
                                            "Year - Variance", "Test - Total number of data",
                                            "Test - Total number of missing data",
                                            "Test - Total percent of missing data"],
                                 ["1900-2020", 4, 1978, 41, 1687.22, 6, 1, 16.67],
                                 ["Test"], ["Country Code - Unique impressions",
                                            "Test - Total number of data",
                                            "Test - Total number of missing data",
                                            "Test - Total percent of missing data"],
                                 [4, 6, 1, 16.67]
                                 ]

        self.assertEqual(expected_return_value,
                         self.data_set_statistic_reporter.report_data_sets_statistics(
                             [data_set_1_with_multiple_reports, data_set_2_with_multiple_reports]))