import unittest

import pandas
from pandas._testing import assert_frame_equal

from data_set_info_data_class.data_class.data_set_info import DataSetInfo
from missing_row_creator.depedency_injector.container import Container
from missing_row_creator.exceptions.missing_row_creator_exceptions import WrongInputFormatError, NonIterableObjectError, \
    MissingFirstColumnPairError, MissingSecondColumnPairError


class MissingRowCreatorTestBase(unittest.TestCase):
    pass


class MissingRowCreatorTestErrorCases(MissingRowCreatorTestBase):
    def test_given_None_when_create_missing_rows_then_throw_input_format_exception(self):
        missing_row_creator = Container.missing_row_creator()
        with self.assertRaises(WrongInputFormatError):
            missing_row_creator.create_missing_rows(None, None, None, None)

    def test_given_non_array_element_create_missing_rows_then_throw_non_iterable_exception(self):
        missing_row_creator = Container.missing_row_creator()
        non_iterable_object = 1

        with self.assertRaises(NonIterableObjectError):
            missing_row_creator.create_missing_rows(non_iterable_object, "", "", [])

    def test_given_non_string_fist_column_name_when_create_missing_rows_then_throw_input_format_exception(self):
        missing_row_creator = Container.missing_row_creator()

        with self.assertRaises(WrongInputFormatError):
            missing_row_creator.create_missing_rows([], 1, "", [])

    def test_given_non_string_second_column_name_when_create_missing_rows_then_throw_input_format_exception(self):
        missing_row_creator = Container.missing_row_creator()

        with self.assertRaises(WrongInputFormatError):
            missing_row_creator.create_missing_rows([], "", 1, [])

    def test_given_non_array_object_for_second_column_values_when_create_missing_rows_then_throw_non_iterable_object_exception(
            self):
        missing_row_creator = Container.missing_row_creator()

        with self.assertRaises(NonIterableObjectError):
            missing_row_creator.create_missing_rows([], "", "", "")

    def test_given_data_set_without_second_column_name_when_create_missing_rows_then_throw_missing_year_column_exception(self):
        missing_row_creator = Container.missing_row_creator()

        data_frame_values = [["JPN", 1], ["SRB", 2], ["ESP", ], ["JPN", ], ["JPN", ],
                             ["JPN", ]]
        data_frame_1_columns = ['Country Code', 'Test']
        data_set_info1 = DataSetInfo("Test", pandas.DataFrame(data_frame_values, columns=data_frame_1_columns),
                                     ["Country Code"], ["Test"])

        with self.assertRaises(MissingFirstColumnPairError):
            missing_row_creator.create_missing_rows([data_set_info1], "Country Code", "Year", [1, 2, 3, 4])

    def test_given_data_set_without_first_column_name_when_create_missing_rows_then_throw_missing_year_column_exception(
            self):
        missing_row_creator = Container.missing_row_creator()

        data_frame_values = [[1900, 1], [1940, 2], [1940, ], [2010, ], [2020, ],
                             [1996, ]]
        data_frame_1_columns = ['Year', 'Test']
        data_set_info1 = DataSetInfo("Test", pandas.DataFrame(data_frame_values, columns=data_frame_1_columns),
                                     ["Year"], ["Test"])

        with self.assertRaises(MissingSecondColumnPairError):
            missing_row_creator.create_missing_rows([data_set_info1], "Country Code", "Year", [1, 2, 3, 4])


class MissingRowCreatorDummyCasesTest(DataSetsListingTestBase):
    def test_given_data_sets_with_missing_country_code_year_pair_when_create_missing_rows_then_return_data_sets_with_all_pairs_in_year_range(
            self):
        missing_row_creator = Container.missing_row_creator()

        data_frame_values = [
            [1990, "SRB", 1], [1991, "JPN", 2], [1992, "JPN", ], [1993, "SRB", ], [1994, "JPN", 3]]
        data_frame_values2 = [
            [1991, "SRB", 1], [1992, "JPN", 2], [1990, "SRB", ], [1994, "SRB", ], [1990, "JPN", 6]]
        data_frame_columns = ['Year', 'Country Code', 'Test']
        data_frame_2_columns = ['Year', 'Country Code', 'Test2']

        data_set_info1 = DataSetInfo("Test", pandas.DataFrame(data_frame_values, columns=data_frame_columns),
                                     ["Year"], ["Test"])
        data_set_info2 = DataSetInfo("Test2", pandas.DataFrame(data_frame_values2, columns=data_frame_2_columns),
                                     ["Year"], ["Test2"])

        expected_data_frame_1_values = [
            [1990, "SRB", 1], [1991, "JPN", 2], [1992, "JPN", ], [1993, "SRB", ], [1994, "JPN", 3],
            [1991, "SRB", ], [1992, "SRB", ], [1994, "SRB", ], [1990, "JPN", ], [1993, "JPN", ]]

        expected_data_frame_2_values = [
            [1991, "SRB", 1], [1992, "JPN", 2], [1990, "SRB", ], [1994, "SRB", ], [1990, "JPN", 6],
            [1992, "SRB", ], [1993, "SRB", ], [1991, "JPN", ], [1993, "JPN", ], [1994, "JPN", ]]

        expected_data_frame_1 = pandas.DataFrame(expected_data_frame_1_values, columns=data_frame_columns)
        expected_data_frame_2 = pandas.DataFrame(expected_data_frame_2_values, columns=data_frame_2_columns)

        actual_data_sets_info = missing_row_creator.create_missing_rows([data_set_info1, data_set_info2], "Country Code", "Year",
                                                                        [1990, 1991, 1992, 1993, 1994])

        assert_frame_equal(expected_data_frame_1.reset_index(drop=True),
                           actual_data_sets_info[0].data_set.reset_index(drop=True))
        assert_frame_equal(expected_data_frame_2.reset_index(drop=True),
                           actual_data_sets_info[1].data_set.reset_index(drop=True))
