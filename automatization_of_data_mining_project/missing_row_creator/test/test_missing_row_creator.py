import unittest

import pandas

from missing_row_creator.classes.data_classes.data_set_info import DataSetInfo
from missing_row_creator.classes.missing_row_creator import MissingRowCreator
from missing_row_creator.depedency_injector.container import Container
from missing_row_creator.exceptions.missing_row_creator_exceptions import WrongInputFormatError, NonIterableObjectError, \
    MissingYearColumnError, MissingCountryCodeColumnError


class DataSetsListingTestBase(unittest.TestCase):
    pass


class MissingRowCreatorTestErrorCases(DataSetsListingTestBase):
    def test_given_None_when_create_missing_rows_then_throw_input_format_exception(self):
        missing_row_creator = Container.missing_row_creator()
        with self.assertRaises(WrongInputFormatError):
            missing_row_creator.create_missing_rows(None, None)

    def test_given_non_array_element_create_missing_rows_then_throw_non_iterable_exception(self):
        missing_row_creator = Container.missing_row_creator()
        non_iterable_object = 1

        with self.assertRaises(NonIterableObjectError):
            missing_row_creator.create_missing_rows(non_iterable_object, (1, 2))

    def test_non_tuple_object_for_year_range_when_create_missing_rows_then_throw_wrong_input_format_exception(self):
        missing_row_creator = Container.missing_row_creator()

        with self.assertRaises(WrongInputFormatError):
            missing_row_creator.create_missing_rows([], 1)

    def test_tuple_object_for_year_range_with_length_non_2_when_create_missing_rows_then_throw_wrong_input_format_exception(self):
        missing_row_creator = Container.missing_row_creator()

        with self.assertRaises(WrongInputFormatError):
            missing_row_creator.create_missing_rows([], (1, 2, 3))

    def test_tuple_object_for_year_range_with_non_int_elements_when_create_missing_rows_then_throw_wrong_input_format_exception(self):
        missing_row_creator = Container.missing_row_creator()

        with self.assertRaises(WrongInputFormatError):
            missing_row_creator.create_missing_rows([], ("1", "2"))

    def test_tuple_object_for_year_range_with_year_to_less_than_year_from_when_create_missing_rows_then_throw_wrong_input_format_exception(self):
        missing_row_creator = Container.missing_row_creator()

        with self.assertRaises(WrongInputFormatError):
            missing_row_creator.create_missing_rows([], (2, 1))

    def test_given_array_with_wrong_element_type_when_create_missing_rows_then_throw_wrong_input_format_exception(self):
        missing_row_creator = Container.missing_row_creator()

        with self.assertRaises(WrongInputFormatError):
            missing_row_creator.create_missing_rows([1, 2, 3], (1, 2))

    def test_given_data_set_without_year_column_when_create_missing_rows_then_throw_missing_year_column_exception(self):
        missing_row_creator = Container.missing_row_creator()

        data_frame_values = [["JPN", 1], ["SRB", 2], ["ESP", ], ["JPN", ], ["JPN", ],
                             ["JPN", ]]
        data_frame_1_columns = ['Country Code', 'Test']
        data_set_info1 = DataSetInfo("Test", pandas.DataFrame(data_frame_values, columns=data_frame_1_columns),
                                     ["Country Code"], ["Test"])

        with self.assertRaises(MissingYearColumnError):
            missing_row_creator.create_missing_rows([data_set_info1], (1, 2))

    def test_given_data_set_without_country_code_column_when_create_missing_rows_then_throw_missing_year_column_exception(self):
        missing_row_creator = Container.missing_row_creator()

        data_frame_values = [[1900, 1], [1940, 2], [1940, ], [2010, ], [2020, ],
                             [1996, ]]
        data_frame_1_columns = ['Year', 'Test']
        data_set_info1 = DataSetInfo("Test", pandas.DataFrame(data_frame_values, columns=data_frame_1_columns),
                                     ["Year"], ["Test"])

        with self.assertRaises(MissingCountryCodeColumnError):
            missing_row_creator.create_missing_rows([data_set_info1], (1, 2))
