import unittest

import pandas
from pandas._testing import assert_frame_equal

from data_set_info_data_class.data_class.data_set_info import DataSetInfo
from nan_value_filler.depedency_injector.container import Container
from nan_value_filler.exceptions.nan_value_filler_exceptions import WrongInputFormatError


class NanValueFillerTestBase(unittest.TestCase):
    pass


class NanValueFillerTestErrorCases(NanValueFillerTestBase):
    def setUp(self):
        self.nan_value_filler = Container.nan_value_filler()

    def test_given_None_when_fill_nan_values_then_throw_input_format_error(self):
        with self.assertRaises(WrongInputFormatError):
            self.nan_value_filler.fill_nan_values(None, None, None)

    def test_given_non_str_filling_method_name_when_fill_nan_values_then_throw_input_format_error(self):
        with self.assertRaises(WrongInputFormatError):
            self.nan_value_filler.fill_nan_values(1, "dwadaw", 'name')

    def test_given_non_data_set_info_object_when_fill_nan_values_then_throw_input_format_error(self):
        with self.assertRaises(WrongInputFormatError):
            self.nan_value_filler.fill_nan_values(1, "something", 'name')


class NanValueFillerTestDummyCases(NanValueFillerTestBase):
    def setUp(self):
        self.nan_value_filler = Container.nan_value_filler()

    def test_given_data_set_info_and_fill_with_0_method_when_fill_nan_values_then_throw_input_format_error(self):
        data_set_info = self.get_test_data_set_info()

        filled_data_set_info: DataSetInfo = self.nan_value_filler.fill_nan_values(data_set_info, "fill_with_zero",
                                                                                  'Test')

        expected_data_frame_values = [[1990, "SRB", 1.0], [1991, "JPN", 2.0], [1992, "JPN", 0.0], [1993, "SRB", 0.0],
                                      [1994, "JPN", 3.0],
                                      [2000, "SRB", 2.0]]

        expected_data_frame = pandas.DataFrame(expected_data_frame_values, columns=['Year', 'Country Code', 'Test'])

        assert_frame_equal(expected_data_frame.reset_index(drop=True),
                           filled_data_set_info.data_set.reset_index(drop=True))

    def test_given_data_set_info_and_fill_with_max_value_method_when_fill_nan_values_then_throw_input_format_error(
            self):
        data_set_info = self.get_test_data_set_info()

        filled_data_set_info: DataSetInfo = self.nan_value_filler.fill_nan_values(data_set_info, "fill_with_max_value",
                                                                                  'Test')

        expected_data_frame_values = [[1990, "SRB", 1.0], [1991, "JPN", 2.0], [1992, "JPN", 3.0], [1993, "SRB", 3.0],
                                      [1994, "JPN", 3.0],
                                      [2000, "SRB", 2.0]]

        expected_data_frame = pandas.DataFrame(expected_data_frame_values, columns=['Year', 'Country Code', 'Test'])

        assert_frame_equal(expected_data_frame.reset_index(drop=True),
                           filled_data_set_info.data_set.reset_index(drop=True))

    def test_given_data_set_info_and_fill_with_min_value_method_when_fill_nan_values_then_throw_input_format_error(
            self):
        data_set_info = self.get_test_data_set_info()

        filled_data_set_info: DataSetInfo = self.nan_value_filler.fill_nan_values(data_set_info, "fill_with_min_value",
                                                                                  'Test')

        expected_data_frame_values = [[1990, "SRB", 1.0], [1991, "JPN", 2.0], [1992, "JPN", 1.0], [1993, "SRB", 1.0],
                                      [1994, "JPN", 3.0],
                                      [2000, "SRB", 2.0]]

        expected_data_frame = pandas.DataFrame(expected_data_frame_values, columns=['Year', 'Country Code', 'Test'])

        assert_frame_equal(expected_data_frame.reset_index(drop=True),
                           filled_data_set_info.data_set.reset_index(drop=True))

    def test_given_data_set_info_and_fill_with_mean_value_method_when_fill_nan_values_then_throw_input_format_error(
            self):
        data_set_info = self.get_test_data_set_info()

        filled_data_set_info: DataSetInfo = self.nan_value_filler.fill_nan_values(data_set_info, "fill_with_mean_value",
                                                                                  'Test')

        expected_data_frame_values = [[1990, "SRB", 1.0], [1991, "JPN", 2.0], [1992, "JPN", 2.0], [1993, "SRB", 2.0],
                                      [1994, "JPN", 3.0],
                                      [2000, "SRB", 2.0]]

        expected_data_frame = pandas.DataFrame(expected_data_frame_values, columns=['Year', 'Country Code', 'Test'])

        assert_frame_equal(expected_data_frame.reset_index(drop=True),
                           filled_data_set_info.data_set.reset_index(drop=True))

    def test_given_data_set_info_and_fill_with_missing_category_value_value_method_when_fill_nan_values_then_throw_input_format_error(
            self):
        data_set_info = self.get_test_data_set_info()

        filled_data_set_info: DataSetInfo = self.nan_value_filler.fill_nan_values(data_set_info,
                                                                                  "fill_with_missing_value_category",
                                                                                  'Test')

        expected_data_frame_values = [[1990, "SRB", 1.0], [1991, "JPN", 2.0], [1992, "JPN", "missing column value"],
                                      [1993, "SRB", "missing column value"],
                                      [1994, "JPN", 3.0],
                                      [2000, "SRB", 2.0]]

        expected_data_frame = pandas.DataFrame(expected_data_frame_values, columns=['Year', 'Country Code', 'Test'])

        assert_frame_equal(expected_data_frame.reset_index(drop=True),
                           filled_data_set_info.data_set.reset_index(drop=True))

    def test_given_data_set_info_and_fill_with_linear_regression_when_fill_nan_values_then_return_data_set_without_nan_values(
            self):
        data_set_info = self.get_test_data_set_info()

        filled_data_set_info: DataSetInfo = self.nan_value_filler.fill_nan_values(data_set_info,
                                                                                  "fill_with_multiple_linear_regression",
                                                                                  'Test')

        self.assertFalse(data_set_info.data_set['Test'].isnull().values.any())
        self.assertEqual(data_set_info.data_set.shape, filled_data_set_info.data_set.shape)

    def test_given_data_set_info_and_fill_with_logistic_regression_when_fill_nan_values_then_return_data_set_without_nan_values(
            self):
        data_set_info = self.get_larger_test_data_set_info()

        filled_data_set_info: DataSetInfo = self.nan_value_filler.fill_nan_values(data_set_info,
                                                                                  "fill_with_logistic_regression",
                                                                                  'Test')

        self.assertFalse(data_set_info.data_set['Test'].isnull().values.any())
        self.assertEqual(data_set_info.data_set.shape, filled_data_set_info.data_set.shape)

    def test_given_data_set_info_and_fill_with_knn_when_fill_nan_values_then_return_data_set_without_nan_values(
            self):
        data_set_info = self.get_larger_test_data_set_info()

        filled_data_set_info: DataSetInfo = self.nan_value_filler.fill_nan_values(data_set_info,
                                                                                  "fill_with_knn",
                                                                                  'Test')

        self.assertFalse(data_set_info.data_set['Test'].isnull().values.any())
        self.assertEqual(data_set_info.data_set.shape, filled_data_set_info.data_set.shape)

    def get_test_data_set_info(self):
        data_frame_values = [[1990, "SRB", 1], [1991, "JPN", 2], [1992, "JPN", ], [1993, "SRB", ], [1994, "JPN", 3],
                             [2000, "SRB", 2]]
        data_frame_columns = ['Year', 'Country Code', 'Test']
        data_set_info = DataSetInfo("Test", pandas.DataFrame(data_frame_values, columns=data_frame_columns),
                                    ["Year", "Country Code"], ["Test"])
        return data_set_info

    def get_larger_test_data_set_info(self):
        data_frame_values = [[1990, "SRB", 1], [1991, "JPN", 2], [1992, "JPN", ], [1993, "SRB", ], [1994, "JPN", 3],
                             [2000, "SRB", 2], [1990, "SRB", 1], [1991, "JPN", 2], [1992, "JPN", ], [1993, "SRB", ],
                             [1994, "JPN", 3],
                             [2000, "SRB", 2], [1990, "SRB", 1], [1991, "JPN", 2], [1992, "JPN", ], [1993, "SRB", ],
                             [1994, "JPN", 3],
                             [2000, "SRB", 2], [1990, "SRB", 1], [1991, "JPN", 2], [1992, "JPN", ], [1993, "SRB", ],
                             [1994, "JPN", 3],
                             [2000, "SRB", 2], [1990, "SRB", 1], [1991, "JPN", 2], [1992, "JPN", ], [1993, "SRB", ],
                             [1994, "JPN", 3],
                             [2000, "SRB", 2], [1990, "SRB", 1], [1991, "JPN", 2], [1992, "JPN", ], [1993, "SRB", ],
                             [1994, "JPN", 3],
                             [2000, "SRB", 2], [1990, "SRB", 1], [1991, "JPN", 2], [1992, "JPN", ], [1993, "SRB", ],
                             [1994, "JPN", 3],
                             [2000, "SRB", 2], [1990, "SRB", 1], [1991, "JPN", 2], [1992, "JPN", ], [1993, "SRB", ],
                             [1994, "JPN", 3],
                             [2000, "SRB", 2]]
        data_frame_columns = ['Year', 'Country Code', 'Test']
        data_set_info = DataSetInfo("Test", pandas.DataFrame(data_frame_values, columns=data_frame_columns),
                                    ["Year", "Country Code"], ["Test"])
        return data_set_info
