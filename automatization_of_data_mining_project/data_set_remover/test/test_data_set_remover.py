import unittest

import pandas

from data_set_info_data_class.data_class.data_set_info import DataSetInfo
from data_set_remover.classes.data_class.data_for_criteria_remove import DataForCriteriaRemove
from data_set_remover.depedency_injector.container import Container
from data_set_remover.exceptions.remover_exceptions import WrongInputFormatError, NonIterableObjectError, \
    NonExistingDataSetWithGivenNameError, ColumnArraysShouldNotBeBothEmpty, ColumnArraysShouldNotBeBothFilled, \
    WrongCriteriaNameError, MissingColumnToIncludeError, MissingPercentCriteriaValueMustBeBetween1and99, \
    UniqueImpressionCriteriaValueMustBeGreaterThan1


class DataSetsRemoverTestBase(unittest.TestCase):
    pass


class DataSetsRemoverTestErrorCases(DataSetsRemoverTestBase):
    def setUp(self):
        self.data_set_remover = Container.data_set_remover()

    def test_given_none_when_remove_data_set_by_name_then_throw_wrong_input_format_error(self):
        with self.assertRaises(WrongInputFormatError):
            self.data_set_remover.remove_manually(None, None)

    def test_given_non_array_input_when_remove_data_sets_then_throw_non_iterable_input_error(self):
        non_iterable_input = 1
        with self.assertRaises(NonIterableObjectError):
            self.data_set_remover.remove_manually(non_iterable_input, "")

    def test_given_array_with_wrong_element_and_data_set_name_type_when_remove_data_sets_then_throw_wrong_input_format_error(
            self):
        input_with_wrong_element_type = [1, 2, 3]
        with self.assertRaises(WrongInputFormatError):
            self.data_set_remover.remove_manually(input_with_wrong_element_type, 1)

    def test_given_array_with_data_set_and_wrong_data_set_name_when_remove_data_set_then_throw_not_existing_data_set_name(
            self):
        data_set_info = DataSetInfo("Test", pandas.DataFrame([]), [], [])
        wrong_data_set_name = "TestTest"
        with self.assertRaises(NonExistingDataSetWithGivenNameError):
            self.data_set_remover.remove_manually([data_set_info], wrong_data_set_name)


class DataSetsRemoveByCriteriaTestErrorCases(DataSetsRemoverTestBase):
    def setUp(self):
        self.data_set_remover = Container.data_set_remover()
        self.data_set_info = DataSetInfo("Test", pandas.DataFrame([[1]], columns=["Test"]), [], [])

    def test_given_none_when_remove_automatically_by_criteria_then_throw_wrong_input_format_error(self):
        with self.assertRaises(WrongInputFormatError):
            self.data_set_remover.remove_by_criteria(None)

    def test_given_non_array_data_set_input_when_remove_automatically_by_criteria_then_throw_non_iterable_input_error(
            self):
        data_for_criteria = DataForCriteriaRemove(1, 'Criteria', 1, ["Test"], [])

        with self.assertRaises(NonIterableObjectError):
            self.data_set_remover.remove_by_criteria(data_for_criteria)

    def test_given_non_string_criteria_name_when_remove_automatically_by_criteria_then_throw_wrong_format_input_error(
            self):
        data_for_criteria = DataForCriteriaRemove([self.data_set_info], 1, 1, ["Test"], [])

        with self.assertRaises(WrongInputFormatError):
            self.data_set_remover.remove_by_criteria(data_for_criteria)

    def test_given_non_int_criteria_value_when_remove_automatically_by_criteria_then_throw_wrong_format_input_error(
            self):
        data_for_criteria = DataForCriteriaRemove([self.data_set_info], "Criteria Name", "wrong", ["Test"], [])

        with self.assertRaises(WrongInputFormatError):
            self.data_set_remover.remove_by_criteria(data_for_criteria)

    def test_given_non_array_columns_to_exclude_when_remove_automatically_by_criteria_then_throw_non_iterable_object_error(
            self):
        data_for_criteria = DataForCriteriaRemove([self.data_set_info], "Criteria Name", 1, "Test", [])

        with self.assertRaises(NonIterableObjectError):
            self.data_set_remover.remove_by_criteria(data_for_criteria)

    def test_given_non_array_columns_to_include_when_remove_automatically_by_criteria_then_throw_non_iterable_object_error(
            self):
        data_for_criteria = DataForCriteriaRemove([self.data_set_info], "Criteria Name", 1, ["Test"], "Test")

        with self.assertRaises(NonIterableObjectError):
            self.data_set_remover.remove_by_criteria(data_for_criteria)

    def test_given_both_empty_columns_to_include_exclude_when_remove_automatically_by_criteria_then_throw_columns_arrays_cannot_be_both_empty(
            self):
        data_for_criteria = DataForCriteriaRemove([self.data_set_info], "Criteria Name", 1, [], [])

        with self.assertRaises(ColumnArraysShouldNotBeBothEmpty):
            self.data_set_remover.remove_by_criteria(data_for_criteria)

    def test_given_both_filled_columns_to_include_exclude_when_remove_automatically_by_criteria_then_throw_columns_arrays_cannot_be_both_filled(
            self):
        data_for_criteria = DataForCriteriaRemove([self.data_set_info], "Criteria Name", 1, ["Test"], ["Test"])

        with self.assertRaises(ColumnArraysShouldNotBeBothFilled):
            self.data_set_remover.remove_by_criteria(data_for_criteria)

    def test_given_non_string_columns_to_include_when_remove_automatically_by_criteria_then_throw_wrong_input_format_error(
            self):
        data_for_criteria = DataForCriteriaRemove([self.data_set_info], "Criteria Name", 1, [], [1])

        with self.assertRaises(WrongInputFormatError):
            self.data_set_remover.remove_by_criteria(data_for_criteria)

    def test_given_non_string_columns_to_exclude_when_remove_automatically_by_criteria_then_throw_wrong_input_format_error(
            self):
        data_for_criteria = DataForCriteriaRemove([self.data_set_info], "Criteria Name", 1, [1], [])

        with self.assertRaises(WrongInputFormatError):
            self.data_set_remover.remove_by_criteria(data_for_criteria)

    def test_given_non_existing_criteria_name_when_remove_automatically_by_criteria_then_throw_criteria_with_given_name_not_exists(
            self):
        data_for_criteria = DataForCriteriaRemove([self.data_set_info], "Wrong criteria name", 1, ["Test"], [])

        with self.assertRaises(WrongCriteriaNameError):
            self.data_set_remover.remove_by_criteria(data_for_criteria)

    def test_given_data_sets_who_have_missing_one_of_columns_to_include_when_remove_automatically_by_criteria_then_throw_missing_columns_to_include_error(
            self):
        data_for_criteria = DataForCriteriaRemove([self.data_set_info], "MISSING_DATA_PERCENT_CRITERIA", 1, [],
                                                  ["Test2"])

        with self.assertRaises(MissingColumnToIncludeError):
            self.data_set_remover.remove_by_criteria(data_for_criteria)

    def test_given_missing_criteria_criteria_data_with_wrong_criteria_value_when_remove_automatically_by_criteria_then_throw_criteria_value_must_be_between_1_and_99(
            self):
        data_for_criteria = DataForCriteriaRemove([self.data_set_info], "MISSING_DATA_PERCENT_CRITERIA", 111, [],
                                                  ["Test"])

        with self.assertRaises(MissingPercentCriteriaValueMustBeBetween1and99):
            self.data_set_remover.remove_by_criteria(data_for_criteria)

    def test_given_unique_impression_criteria_datA_with_wrong_criteria_value_when_remove_automatically_by_criteria_then_throw_criteria_value_must_be_greater_than_1(
            self):
        data_for_criteria = DataForCriteriaRemove([self.data_set_info], "NUMBER_OF_UNIQUE_IMPRESSIONS_CRITERIA", -10,
                                                  [], ["Test"])

        with self.assertRaises(UniqueImpressionCriteriaValueMustBeGreaterThan1):
            self.data_set_remover.remove_by_criteria(data_for_criteria)


class DataSetRemoverDummyCasesTest(DataSetsRemoverTestBase):
    def setUp(self):
        self.data_set_remover = Container.data_set_remover()
        self.data_set_info = DataSetInfo("Test", pandas.DataFrame([]), [], [])

    def test_given_array_with_data_set_and_correct_data_set_name_when_remove_data_set_then_return_empty_array(self):
        data_set_name = "Test"
        self.assertEqual([], self.data_set_remover.remove_manually([self.data_set_info], data_set_name))

    def test_given_array_with_multiple_data_sets_and_correct_data_set_name_when_remove_data_set_then_return_array_without_that_data_set(
            self):
        data_set_info2 = DataSetInfo("Test2", pandas.DataFrame([]), [], [])
        data_set_info3 = DataSetInfo("Test3", pandas.DataFrame([]), [], [])
        data_set_name = "Test2"

        self.assertEqual([self.data_set_info, data_set_info3],
                         self.data_set_remover.remove_manually([self.data_set_info, data_set_info2, data_set_info3],
                                                               data_set_name))


class DataSetRemoverByCriteriaDummyCasesTest(DataSetsRemoverTestBase):
    def setUp(self) -> None:
        self.data_set_remover = Container.data_set_remover()
        self.MISSING_DATA_PERCENT_CRITERIA_NAME = "MISSING_DATA_PERCENT_CRITERIA"
        self.NUMBER_OF_UNIQUE_IMPRESSIONS_NAME = "NUMBER_OF_UNIQUE_IMPRESSIONS_CRITERIA"

    def test_given_missing_percent_criteria_with_important_column_and_all_elements_that_pass_criteria_when_remove_datasets_by_criteria_return_same_data_sets_info_list(
            self):
        data_frame_columns, data_frame_values, data_frame_values2 = self.get_data_frame_values_and_columns_with_3_columns()

        data_set_info1, data_set_info2 = self.get_data_set_info_object("Test", data_frame_values, "Test2",
                                                                       data_frame_values2, data_frame_columns,
                                                                       ["Year, Country Code"], ["Test"])

        data_for_criteria = DataForCriteriaRemove([data_set_info1, data_set_info2],
                                                  self.MISSING_DATA_PERCENT_CRITERIA_NAME, 99,
                                                  [], ["Test"])

        self.assertEqual([data_set_info1, data_set_info2], self.data_set_remover.remove_by_criteria(data_for_criteria))

    def test_given_missing_percent_criteria_with_must_contained_important_column_and_one_element_who_dont_pass_criteria_when_remove_datasets_by_criteria_return_data_sets_without_the_one(
            self):
        data_frame_columns, data_frame_values, data_frame_values2 = self.get_data_frame_values_and_columns_with_3_columns()

        data_set_info1, data_set_info2 = self.get_data_set_info_object("Test", data_frame_values, "Test2",
                                                                       data_frame_values2, data_frame_columns,
                                                                       ["Year", "Country Code", "Test"], [])

        data_for_criteria = DataForCriteriaRemove([data_set_info1, data_set_info2],
                                                  self.MISSING_DATA_PERCENT_CRITERIA_NAME, 50,
                                                  [], ["Test"])

        self.assertEqual([data_set_info2], self.data_set_remover.remove_by_criteria(data_for_criteria))

    def test_given_missing_percent_criteria_with_only_one_other_column_and_one_element_who_dont_pass_criteria_when_remove_datasets_by_criteria_return_data_sets_without_the_one(
            self):
        data_frame_columns, data_frame_values, data_frame_values2 = self.get_data_frame_values_and_columns_with_3_columns()

        data_set_info1, data_set_info2 = self.get_data_set_info_object("Test", data_frame_values, "Test2",
                                                                       data_frame_values2, data_frame_columns,
                                                                       ["Year", "Country Code"], ["Test"])

        data_for_criteria = DataForCriteriaRemove([data_set_info1, data_set_info2],
                                                  self.MISSING_DATA_PERCENT_CRITERIA_NAME, 50,
                                                  [], ["Test"])

        self.assertEqual([data_set_info2], self.data_set_remover.remove_by_criteria(data_for_criteria))

    def test_given_missing_percent_criteria_with_only_one_other_column_of_multiple_other_columns_who_dont_pass_criteria_when_remove_datasets_by_criteria_return_data_sets_without_that_column(
            self):
        data_frame_columns, data_frame_values, data_frame_values2 = self.get_data_frame_values_and_columns_with_4_columns()

        data_set_info1, data_set_info2 = self.get_data_set_info_object("Test", data_frame_values, "Test2",
                                                                       data_frame_values2, data_frame_columns,
                                                                       ["Year", "Country Code"], ["Test", "Test2"])

        data_for_criteria = DataForCriteriaRemove([data_set_info1, data_set_info2],
                                                  self.MISSING_DATA_PERCENT_CRITERIA_NAME, 50,
                                                  ["Year", "Country Code"], [])

        self.act_and_assert_criteria_method(data_frame_columns, data_for_criteria)

    def test_given_number_of_unique_impression_criteria_with_only_one_other_column_of_multiple_other_columns_who_don_t_pass_criteria_when_remove_datasets_by_criteria_return_data_sets_without_that_column(
            self):
        data_frame_columns, data_frame_values, data_frame_values2 = self.get_data_frame_values_and_columns_with_4_columns()

        data_set_info1, data_set_info2 = self.get_data_set_info_object("Test", data_frame_values, "Test2",
                                                                       data_frame_values2, data_frame_columns,
                                                                       ["Year", "Country Code"], ["Test", "Test2"])

        data_for_criteria = DataForCriteriaRemove([data_set_info1, data_set_info2],
                                                  self.NUMBER_OF_UNIQUE_IMPRESSIONS_NAME, 3,
                                                  ["Year", "Country Code"], [])

        self.act_and_assert_criteria_method(data_frame_columns, data_for_criteria)

    def act_and_assert_criteria_method(self, data_frame_columns, data_for_criteria):
        expected_data_frame_columns = ['Year', 'Country Code', 'Test']

        action_return_value = self.data_set_remover.remove_by_criteria(data_for_criteria)

        self.assertEqual(expected_data_frame_columns, action_return_value[0].data_set.columns.tolist())
        self.assertEqual(data_frame_columns, action_return_value[1].data_set.columns.tolist())

    def get_data_frame_values_and_columns_with_3_columns(self):
        data_frame_values = [
            [1900, "SRB", 1], [1950, "JPN", 2], [1990, "RUS", ], [2010, "SRB", ], [2020, "ESP", ], [1996, "JPN", ]]
        data_frame_values2 = [
            [1900, "SRB", 1], [1950, "JPN", 2], [1990, "RUS", ], [2010, "SRB", ], [2020, "ESP", 5], [1996, "JPN", 6]]
        data_frame_columns = ['Year', 'Country Code', 'Test']

        return data_frame_columns, data_frame_values, data_frame_values2

    def get_data_frame_values_and_columns_with_4_columns(self):
        data_frame_values = [
            [1900, "SRB", 2, 2], [1950, "JPN", 7, 2], [1990, "RUS", 4, ], [2010, "SRB", 7, ], [2020, "ESP", 9, ],
            [1996, "JPN", 4, ]]
        data_frame_values2 = [
            [1900, "SRB", 1, 4], [1950, "JPN", 5, 7], [1990, "RUS", 8, ], [2010, "SRB", 9, ], [2020, "ESP", 5, 8],
            [1996, "JPN", 2, 3]]
        data_frame_columns = ['Year', 'Country Code', 'Test', 'Test2']
        return data_frame_columns, data_frame_values, data_frame_values2

    def get_data_set_info_object(self, data_set1_name, data_set1_values, data_set2_name, data_set2_values,
                                 data_frame_columns, required_columns, other_columns):
        data_set_info1 = DataSetInfo(data_set1_name, pandas.DataFrame(data_set1_values, columns=data_frame_columns),
                                     required_columns, other_columns)
        data_set_info2 = DataSetInfo(data_set2_name, pandas.DataFrame(data_set2_values, columns=data_frame_columns),
                                     required_columns, other_columns)

        return data_set_info1, data_set_info2


class DataSetRemoverGetInformationTest(DataSetsRemoverTestBase):
    def test_given_criteria_validators_for_missing_percent_and_number_of_unique_impressions_when_get_criteria_validators_names_then_give_correct_list_of_names(
            self):
        data_set_remover = Container.data_set_remover()

        criteria_names = data_set_remover.get_criteria_validator_names()

        self.assertEqual(["MISSING_DATA_PERCENT_CRITERIA", "NUMBER_OF_UNIQUE_IMPRESSIONS_CRITERIA"], criteria_names)
