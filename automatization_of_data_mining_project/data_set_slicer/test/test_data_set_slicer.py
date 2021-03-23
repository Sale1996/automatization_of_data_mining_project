import unittest

import pandas
from pandas.util.testing import assert_frame_equal

from data_set_info_data_class.data_class.data_set_info import DataSetInfo
from data_set_slicer.classes.data_frame_slicer.column_value_range_data_frame_slicer import \
    ColumnValueRangeDataFrameSlicer
from data_set_slicer.classes.data_frame_slicer.cross_section_data_frame_slicer import CrossSectionDataFrameSlicer
from data_set_slicer.classes.data_frame_slicer.data_frame_slicer import DataFrameSlicer
from data_set_slicer.depedency_injector.container import Container
from data_set_slicer.exceptions.slicer_exceptions import WrongInputFormatError, NonIterableObjectError, \
    NonExistingSlicingMethodError, EmptyResultsError, WrongRangeObjectFormatError


class DataSetsSlicerTestBase(unittest.TestCase):
    pass


class DataSetsSlicerTestErrorCases(DataSetsSlicerTestBase):
    def setUp(self):
        pass

    def test_given_nones_when_slicing_data_sets_then_throw_input_format_exception(self):
        data_set_slicer = Container.data_set_slicer([])

        with self.assertRaises(WrongInputFormatError):
            data_set_slicer.slice_data_sets(None)

    def test_given_non_array_data_sets_element_when_slicing_data_sets_then_throw_non_iterable_exception(self):
        non_iterable_object = 1
        data_set_slicer = Container.data_set_slicer([])

        with self.assertRaises(NonIterableObjectError):
            data_set_slicer.slice_data_sets(non_iterable_object)

    def test_given_non_existing_slicing_method_when_slicing_data_sets_then_throw_non_existing_slicing_method_error(
            self):
        data_set_slicer = Container.data_set_slicer([])

        with self.assertRaises(NonExistingSlicingMethodError):
            data_set_slicer.slice_data_sets([])

    def test_given_wrong_data_set_element_type_when_slicing_data_sets_then_throw_wrong_input_format_error(self):
        data_set_slicer = get_country_code_cross_section_slicer()

        with self.assertRaises(WrongInputFormatError):
            data_set_slicer.slice_data_sets([1, 2, 3])

    def test_given_non_array_range_object_when_slice_data_sets_throw_non_array_range_object(self):
        with self.assertRaises(WrongRangeObjectFormatError):
            ColumnValueRangeDataFrameSlicer("Year", "Test")

    def test_given_wrong_column_range_array_object_with_more_than_two_element_when_slice_data_sets_throw_wrong_input_format_error(
            self):
        with self.assertRaises(WrongRangeObjectFormatError):
            ColumnValueRangeDataFrameSlicer("Year", (1, 2, 3))

    def test_given_wrong_column_range_array_element_types_when_slice_data_sets_throw_wrong_input_format_error(self):
        with self.assertRaises(WrongRangeObjectFormatError):
            ColumnValueRangeDataFrameSlicer("Year", ("1", "2"))


class DataSetsSlicerCrossSectionByColumnValuesDummyCases(DataSetsSlicerTestBase):

    def test_given_data_sets_with_all_elements_contained_in_cross_section_when_slice_data_sets_return_same_data_sets(
            self):
        data_set_slicer = get_country_code_cross_section_slicer()

        data_frame_values = [[1900, "JPN", 1], [1950, "SRB", 2], [1990, "JPN", ], [2010, "JPN", ], [2020, "JPN", ],
                             [1996, "JPN", ]]
        data_frame_values2 = [[1900, "JPN", 1], [1950, "SRB", 2], [1990, "SRB", ], [2010, "SRB", ], [2020, "SRB", 5],
                              [1996, "SRB", 6]]

        data_frame_1_columns = ['Year', 'Country Code', 'Test']
        data_frame_2_columns = ['Year', 'Country Code', 'Test2']

        data_set_info_1, data_set_info_2 = get_data_set_info_object("Test", data_frame_values,
                                                                    data_frame_1_columns,
                                                                    "Test2", data_frame_values2,
                                                                    data_frame_2_columns,
                                                                    ["Year", "Country Code"], ["Test"], ["Test2"])

        sliced_data_sets = data_set_slicer.slice_data_sets([data_set_info_1, data_set_info_2])

        assert_equality_of_pair_of_data_frames(data_set_info_1.data_set, data_set_info_2.data_set,
                                               sliced_data_sets[0].data_set, sliced_data_sets[1].data_set)

    def test_given_data_sets_with_non_all_elements_contained_in_cross_section_when_slice_data_sets_return_data_sets_with_only_cross_data(
            self):
        data_set_slicer = get_country_code_cross_section_slicer()

        data_set_info_1, data_set_info_2 = get_test_data_set_infos()

        sliced_data_sets = data_set_slicer.slice_data_sets([data_set_info_1, data_set_info_2])

        expected_data_frame_value_1 = [[1900, "JPN", 1], [1940, "SRB", 2], [2010, "JPN", ], [2020, "JPN", ],
                                       [1996, "JPN", ]]
        expected_data_frame_value_2 = [[2000, "JPN", 1], [1950, "SRB", 2], [1990, "SRB", ], [2020, "SRB", 5],
                                       [1996, "SRB", 6]]
        data_frame_1_columns = ['Year', 'Country Code', 'Test']
        data_frame_2_columns = ['Year', 'Country Code', 'Test2']

        expected_data_frame_1 = pandas.DataFrame(expected_data_frame_value_1, columns=data_frame_1_columns)
        expected_data_frame_2 = pandas.DataFrame(expected_data_frame_value_2, columns=data_frame_2_columns)

        assert_equality_of_pair_of_data_frames(expected_data_frame_1, expected_data_frame_2,
                                               sliced_data_sets[0].data_set, sliced_data_sets[1].data_set)


class DataSetsSliceByColumnValueRangeDummyCases(DataSetsSlicerTestBase):
    def test_given_multiple_data_sets_in_wanted_range_when_slice_data_sets_then_return_same_data_sets(self):
        data_set_slicer = get_year_column_range_data_frame_slicer(1800, 2100)

        data_set_info_1, data_set_info_2 = get_test_data_set_infos()

        sliced_data_sets = data_set_slicer.slice_data_sets([data_set_info_1, data_set_info_2])

        assert_equality_of_pair_of_data_frames(data_set_info_1.data_set, data_set_info_2.data_set,
                                               sliced_data_sets[0].data_set, sliced_data_sets[1].data_set)

    def test_given_multiple_data_sets_that_some_of_the_elements_contain_wanted_range_when_slice_data_sets_then_return_data_sets_with_rows_only_in_range(
            self):
        data_set_slicer = get_year_column_range_data_frame_slicer(1900, 1990)

        data_set_info_1, data_set_info_2 = get_test_data_set_infos()

        sliced_data_sets = data_set_slicer.slice_data_sets([data_set_info_1, data_set_info_2])

        expected_data_frame_value_1 = [[1900, "JPN", 1], [1940, "SRB", 2], [1940, "ESP", ]]
        expected_data_frame_value_2 = [[1950, "SRB", 2], [1990, "SRB", ]]

        data_frame_1_columns = ['Year', 'Country Code', 'Test']
        data_frame_2_columns = ['Year', 'Country Code', 'Test2']

        expected_data_frame_1 = pandas.DataFrame(expected_data_frame_value_1, columns=data_frame_1_columns)
        expected_data_frame_2 = pandas.DataFrame(expected_data_frame_value_2, columns=data_frame_2_columns)

        assert_equality_of_pair_of_data_frames(expected_data_frame_1, expected_data_frame_2,
                                               sliced_data_sets[0].data_set, sliced_data_sets[1].data_set)

    def test_given_multiple_data_sets_that_one_of_them_don_t_contain_any_of_wanted_range_when_slice_data_sets_then_return_data_sets_with_one_empty(
            self):
        data_set_slicer = get_year_column_range_data_frame_slicer(1900, 1940)

        data_set_info_1, data_set_info_2 = get_test_data_set_infos()

        sliced_data_sets = data_set_slicer.slice_data_sets([data_set_info_1, data_set_info_2])

        expected_data_frame_value_1 = [[1900, "JPN", 1.0], [1940, "SRB", 2.0], [1940, "ESP"]]
        data_frame_1_columns = ['Year', 'Country Code', 'Test']

        expected_data_frame_1 = pandas.DataFrame(expected_data_frame_value_1, columns=data_frame_1_columns)
        # empty data frame
        expected_data_frame_2 = pandas.DataFrame({'Year': pandas.Series([], dtype='int64'),
                                                  'Country Code': pandas.Series([], dtype='str'),
                                                  'Test2': pandas.Series([], dtype='float')})

        assert_equality_of_pair_of_data_frames(expected_data_frame_1, expected_data_frame_2,
                                               sliced_data_sets[0].data_set, sliced_data_sets[1].data_set)

    def test_given_multiple_data_sets_which_passes_both_slicer_criteria_when_slice_datasets_return_the_same_datasets(
            self):
        data_set_slicer = get_data_frame_slicer_with_country_code_cross_section_and_year_range(1800, 2100)

        data_frame_values = [[1900, "JPN", 1], [1950, "SRB", 2], [1990, "JPN", ], [2010, "JPN", ], [2020, "JPN", ],
                             [1996, "JPN", ]]
        data_frame_values2 = [[1900, "JPN", 1], [1950, "SRB", 2], [1990, "SRB", ], [2010, "SRB", ], [2020, "SRB", 5],
                              [1996, "SRB", 6]]

        data_frame_1_columns = ['Year', 'Country Code', 'Test']
        data_frame_2_columns = ['Year', 'Country Code', 'Test2']

        data_set_info_1, data_set_info_2 = get_data_set_info_object("Test", data_frame_values,
                                                                    data_frame_1_columns,
                                                                    "Test2", data_frame_values2,
                                                                    data_frame_2_columns,
                                                                    ["Year", "Country Code"], ["Test"], ["Test2"])

        sliced_data_sets = data_set_slicer.slice_data_sets([data_set_info_1, data_set_info_2])

        assert_equality_of_pair_of_data_frames(data_set_info_1.data_set, data_set_info_2.data_set,
                                               sliced_data_sets[0].data_set, sliced_data_sets[1].data_set)

    def test_given_multiple_data_sets_that_some_of_the_elements_don_t_pass_none_of_slicer_criteria_when_slice_datasets_return_the_same_datasets_without_these_rows(
            self):
        data_set_slicer = get_data_frame_slicer_with_country_code_cross_section_and_year_range(1900, 1990)

        data_set_info_1, data_set_info_2 = get_test_data_set_infos()

        sliced_data_sets = data_set_slicer.slice_data_sets([data_set_info_1, data_set_info_2])

        expected_data_frame_value_1 = [[1900, "JPN", 1.0], [1940, "SRB", 2.0]]
        expected_data_frame_value_2 = [[1950, "SRB", 2.0], [1990, "SRB", ]]

        data_frame_1_columns = ['Year', 'Country Code', 'Test']
        data_frame_2_columns = ['Year', 'Country Code', 'Test2']

        expected_data_frame_1 = pandas.DataFrame(expected_data_frame_value_1, columns=data_frame_1_columns)
        expected_data_frame_2 = pandas.DataFrame(expected_data_frame_value_2, columns=data_frame_2_columns)

        assert_equality_of_pair_of_data_frames(expected_data_frame_1, expected_data_frame_2,
                                               sliced_data_sets[0].data_set, sliced_data_sets[1].data_set)

    def test_given_multiple_data_sets_that_one_of_them_don_t_pass_any_of_the_slicers_when_slice_data_sets_then_return_data_sets_with_one_empty(
            self):
        data_set_slicer = get_data_frame_slicer_with_country_code_cross_section_and_year_range(1900, 1940)

        data_set_info_1, data_set_info_2 = get_test_data_set_infos()

        sliced_data_sets = data_set_slicer.slice_data_sets([data_set_info_1, data_set_info_2])

        expected_data_frame_value_1 = [[1900, "JPN", 1.0], [1940, "SRB", 2.0]]
        data_frame_1_columns = ['Year', 'Country Code', 'Test']

        expected_data_frame_1 = pandas.DataFrame(expected_data_frame_value_1, columns=data_frame_1_columns)
        # empty data frame
        expected_data_frame_2 = pandas.DataFrame({'Year': pandas.Series([], dtype='int64'),
                                                  'Country Code': pandas.Series([], dtype='str'),
                                                  'Test2': pandas.Series([], dtype='float')})

        assert_equality_of_pair_of_data_frames(expected_data_frame_1, expected_data_frame_2,
                                               sliced_data_sets[0].data_set, sliced_data_sets[1].data_set)


def get_test_data_set_infos():
    data_frame_values = [[1900, "JPN", 1], [1940, "SRB", 2], [1940, "ESP", ], [2010, "JPN", ], [2020, "JPN", ],
                         [1996, "JPN", ]]
    data_frame_values2 = [[2000, "JPN", 1], [1950, "SRB", 2], [1990, "SRB", ], [2010, "GER", ], [2020, "SRB", 5],
                          [1996, "SRB", 6]]
    data_frame_1_columns = ['Year', 'Country Code', 'Test']
    data_frame_2_columns = ['Year', 'Country Code', 'Test2']
    data_set_info_1, data_set_info_2 = get_data_set_info_object("Test", data_frame_values,
                                                                data_frame_1_columns,
                                                                "Test2", data_frame_values2,
                                                                data_frame_2_columns,
                                                                ["Year", "Country Code"], ["Test"], ["Test2"])
    return data_set_info_1, data_set_info_2


def get_data_set_info_object(data_set1_name, data_set1_values, data_set_1_columns, data_set2_name,
                             data_set2_values,
                             data_set_2_columns, required_columns, data_set_1_other_columns,
                             data_set_2_other_columns):
    data_set_info1 = DataSetInfo(data_set1_name, pandas.DataFrame(data_set1_values, columns=data_set_1_columns),
                                 required_columns, data_set_1_other_columns)
    data_set_info2 = DataSetInfo(data_set2_name, pandas.DataFrame(data_set2_values, columns=data_set_2_columns),
                                 required_columns, data_set_2_other_columns)

    return data_set_info1, data_set_info2


def get_country_code_cross_section_slicer():
    slicer: DataFrameSlicer = CrossSectionDataFrameSlicer("Country Code")
    data_set_slicer = Container.data_set_slicer([slicer])
    return data_set_slicer


def get_year_column_range_data_frame_slicer(year_from, year_to):
    slicer: DataFrameSlicer = ColumnValueRangeDataFrameSlicer("Year", (year_from, year_to))
    data_set_slicer = Container.data_set_slicer([slicer])
    return data_set_slicer


def get_data_frame_slicer_with_country_code_cross_section_and_year_range(year_from, year_to):
    cross_section_slicer: DataFrameSlicer = CrossSectionDataFrameSlicer("Country Code")
    column_value_range_slicer: DataFrameSlicer = ColumnValueRangeDataFrameSlicer("Year", (year_from, year_to))
    data_set_slicer = Container.data_set_slicer([cross_section_slicer, column_value_range_slicer])
    return data_set_slicer


def assert_equality_of_pair_of_data_frames(expected_data_frame_1, expected_data_frame_2, actual_data_frame_1,
                                           actual_data_frame2):
    assert_frame_equal(expected_data_frame_1.reset_index(drop=True),
                       actual_data_frame_1.reset_index(drop=True))
    assert_frame_equal(expected_data_frame_2.reset_index(drop=True),
                       actual_data_frame2.reset_index(drop=True))
