import unittest

import numpy
import pandas
from pandas._testing import assert_frame_equal

from data_set_joiner.classes.data_set_joiner import DataSetsJoiner
from data_set_joiner.depedency_injector.container import Container
from data_set_joiner.exceptions.joiner_exceptions import WrongInputFormatError, NonIterableObjectError, \
    MissingJoinerColumnError


class DataSetsJoinerTestBase(unittest.TestCase):
    pass


class DataSetsJoinerTestErrorCases(DataSetsJoinerTestBase):
    def setUp(self):
        self.data_set_joiner = Container.data_sets_joiner()

    def test_given_nones_when_joining_data_sets_then_throw_input_format_exception(self):
        with self.assertRaises(WrongInputFormatError):
            self.data_set_joiner.join_data_sets(None, None)

    def test_given_non_array_data_sets_element_when_joining_data_sets_then_throw_non_iterable_exception(self):
        non_iterable_object = 1

        with self.assertRaises(NonIterableObjectError):
            self.data_set_joiner.join_data_sets(non_iterable_object, [])

    def test_given_non_array_joining_columns_element_when_joining_data_sets_then_throw_non_iterable_exception(self):
        non_iterable_object = 1

        with self.assertRaises(NonIterableObjectError):
            self.data_set_joiner.join_data_sets([], non_iterable_object)

    def test_given_joining_columns_array_with_non_str_element_type_when_joining_data_sets_then_throw_wrong_input_format_error(
            self):
        with self.assertRaises(WrongInputFormatError):
            self.data_set_joiner.join_data_sets([], [1, 2, 3])

    def test_given_data_sets_with_non_data_framer_element_type_when_joining_data_sets_then_throw_wrong_input_format_error(
            self):
        with self.assertRaises(WrongInputFormatError):
            self.data_set_joiner.join_data_sets([1, 2, 3], ["Test"])

    def test_given_data_sets_which_misses_one_of_joiner_columns_when_joining_data_sets_then_throw_missing_joiner_column_error(
            self):
        data_frame_values = [[1900, "JPN", 3], [1900, "SRB", 2], [2000, "JPN", 2], [2000, "SRB", 2]]

        data_frame_2_values = [[1900, "JPN", 4], [1900, "SRB", 6], [2000, "JPN", 3], [2000, "SRB", 2]]

        data_frame_1_columns = ['Year', 'Country Code', 'Test']
        data_frame_2_columns = ['Year', 'Error', 'Test2']

        df_1 = pandas.DataFrame(data_frame_values, columns=data_frame_1_columns)
        df_2 = pandas.DataFrame(data_frame_2_values, columns=data_frame_2_columns)

        with self.assertRaises(MissingJoinerColumnError):
            self.data_set_joiner.join_data_sets([df_1, df_2], ["Year", "Country Code"])


class DataSetsJoinerTestDummyCases(DataSetsJoinerTestBase):
    def setUp(self):
        self.data_set_joiner = Container.data_sets_joiner()

    def test_given_data_sets_with_no_missing_data_when_joining_data_sets_then_return_joined_data_set_without_missing_values(
            self):
        data_frame_values = [[1900, "JPN", 3], [1900, "SRB", 2], [2000, "JPN", 2], [2000, "SRB", 2]]

        data_frame_2_values = [[1900, "JPN", 4], [1900, "SRB", 6], [2000, "JPN", 3], [2000, "SRB", 2]]

        data_frame_1_columns = ['Year', 'Country Code', 'Test']
        data_frame_2_columns = ['Year', 'Country Code', 'Test2']

        df_1 = pandas.DataFrame(data_frame_values, columns=data_frame_1_columns)
        df_2 = pandas.DataFrame(data_frame_2_values, columns=data_frame_2_columns)

        expected_data_frame_values = [[1900, "JPN", 3, 4], [1900, "SRB", 2, 6], [2000, "JPN", 2, 3],
                                      [2000, "SRB", 2, 2]]

        expected_data_frame_columns = ['Year', 'Country Code', 'Test', 'Test2']

        expected_joined_data_frame = pandas.DataFrame(expected_data_frame_values, columns=expected_data_frame_columns)

        joined_data_frame = self.data_set_joiner.join_data_sets([df_1, df_2], ['Year', 'Country Code'])

        assert_frame_equal(expected_joined_data_frame.reset_index(drop=True),
                           joined_data_frame.reset_index(drop=True))

    def test_given_data_sets_with_missing_data_when_joining_data_sets_then_return_joined_data_set_without_missing_values(
            self):
        data_frame_values = [[1901, "JPN", 3], [1900, "SRB", 2], [2000, "JPN", 2], [2000, "SRB", 2]]

        data_frame_2_values = [[1900, "JPN", 4], [1901, "SRB", 6], [2000, "JPN", 3], [2000, "SRB", 2]]

        data_frame_1_columns = ['Year', 'Country Code', 'Test']
        data_frame_2_columns = ['Year', 'Country Code', 'Test2']

        df_1 = pandas.DataFrame(data_frame_values, columns=data_frame_1_columns)
        df_2 = pandas.DataFrame(data_frame_2_values, columns=data_frame_2_columns)

        expected_data_frame_values = [[1901, "JPN", 3, numpy.nan], [1900, "SRB", 2, numpy.nan],
                                      [2000, "JPN", 2, 3], [2000, "SRB", 2, 2],
                                      [1900, "JPN", numpy.nan, 4], [1901, "SRB", numpy.nan, 6]]

        expected_data_frame_columns = ['Year', 'Country Code', 'Test', 'Test2']

        expected_joined_data_frame = pandas.DataFrame(expected_data_frame_values, columns=expected_data_frame_columns)

        joined_data_frame = self.data_set_joiner.join_data_sets([df_1, df_2], ['Year', 'Country Code'])

        assert_frame_equal(expected_joined_data_frame.reset_index(drop=True),
                           joined_data_frame.reset_index(drop=True))