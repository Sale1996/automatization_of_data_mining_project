import unittest

import pandas

from data_set_remover.classes.data_class.data_for_criteria_remove import DataForCriteriaRemove
from data_set_remover.classes.data_class.data_set_info import DataSetInfo
from data_set_remover.classes.data_set_remover import DataSetRemover
from data_set_remover.exceptions.remover_exceptions import WrongInputFormatError, NonIterableObjectError, \
    NonExistingDataSetWithGivenNameError, ColumnArraysShouldNotBeBothEmpty, ColumnArraysCannotBeBothFilled


class DataSetsRemoverTestBase(unittest.TestCase):
    pass


class DataSetsRemoverTestErrorCases(DataSetsRemoverTestBase):
    def setUp(self):
        self.data_set_remover = DataSetRemover()

    def test_given_none_when_remove_data_set_by_name_then_throw_wrong_input_format_error(self):
        with self.assertRaises(WrongInputFormatError):
            self.data_set_remover.remove_data_set(None, None)

    def test_given_non_array_input_when_remove_data_sets_then_throw_non_iterable_input_error(self):
        non_iterable_input = 1
        with self.assertRaises(NonIterableObjectError):
            self.data_set_remover.remove_data_set(non_iterable_input, "")

    def test_given_array_with_wrong_element_and_data_set_name_type_when_remove_data_sets_then_throw_wrong_input_format_error(
            self):
        input_with_wrong_element_type = [1, 2, 3]
        with self.assertRaises(WrongInputFormatError):
            self.data_set_remover.remove_data_set(input_with_wrong_element_type, 1)

    def test_given_array_with_data_set_and_wrong_data_set_name_when_remove_data_set_then_throw_not_existing_data_set_name(
            self):
        data_set_info = DataSetInfo("Test", pandas.DataFrame([]))
        wrong_data_set_name = "TestTest"
        with self.assertRaises(NonExistingDataSetWithGivenNameError):
            self.data_set_remover.remove_data_set([data_set_info], wrong_data_set_name)


class DataSetsRemoveByCriteriaTestErrorCases(DataSetsRemoverTestBase):
    def setUp(self):
        self.data_set_remover = DataSetRemover()
        self.data_set_info1 = DataSetInfo("Test", pandas.DataFrame([]))

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
        data_for_criteria = DataForCriteriaRemove([self.data_set_info1], 1, 1, ["Test"], [])

        with self.assertRaises(WrongInputFormatError):
            self.data_set_remover.remove_by_criteria(data_for_criteria)

    def test_given_non_int_criteria_value_when_remove_automatically_by_criteria_then_throw_wrong_format_input_error(
            self):
        data_for_criteria = DataForCriteriaRemove([self.data_set_info1], "Criteria Name", "wrong", ["Test"], [])

        with self.assertRaises(WrongInputFormatError):
            self.data_set_remover.remove_by_criteria(data_for_criteria)

    def test_given_non_array_columns_to_exclude_when_remove_automatically_by_criteria_then_throw_non_iterable_object_error(
            self):
        data_for_criteria = DataForCriteriaRemove([self.data_set_info1], "Criteria Name", 1, "Test", [])

        with self.assertRaises(NonIterableObjectError):
            self.data_set_remover.remove_by_criteria(data_for_criteria)

    def test_given_non_array_columns_to_include_when_remove_automatically_by_criteria_then_throw_non_iterable_object_error(
            self):
        data_for_criteria = DataForCriteriaRemove([self.data_set_info1], "Criteria Name", 1, ["Test"], "Test")

        with self.assertRaises(NonIterableObjectError):
            self.data_set_remover.remove_by_criteria(data_for_criteria)

    def test_given_both_empty_columns_to_include_exclude_when_remove_automatically_by_criteria_then_throw_columns_arrays_cannot_be_both_empty(
            self):
        data_for_criteria = DataForCriteriaRemove([self.data_set_info1], "Criteria Name", 1, [], [])

        with self.assertRaises(ColumnArraysShouldNotBeBothEmpty):
            self.data_set_remover.remove_by_criteria(data_for_criteria)

    def test_given_both_filled_columns_to_include_exclude_when_remove_automatically_by_criteria_then_throw_columns_arrays_cannot_be_both_filled(
            self):
        data_for_criteria = DataForCriteriaRemove([self.data_set_info1], "Criteria Name", 1, ["Test"], ["Test"])

        with self.assertRaises(ColumnArraysCannotBeBothFilled):
            self.data_set_remover.remove_by_criteria(data_for_criteria)

    def test_given_non_string_columns_to_include_when_remove_automatically_by_criteria_then_throw_wrong_input_format_error(
            self):
        data_for_criteria = DataForCriteriaRemove([self.data_set_info1], "Criteria Name", 1, [], [1])

        with self.assertRaises(WrongInputFormatError):
            self.data_set_remover.remove_by_criteria(data_for_criteria)

    def test_given_non_string_columns_to_exclude_when_remove_automatically_by_criteria_then_throw_wrong_input_format_error(
            self):
        data_for_criteria = DataForCriteriaRemove([self.data_set_info1], "Criteria Name", 1, [1], [])

        with self.assertRaises(WrongInputFormatError):
            self.data_set_remover.remove_by_criteria(data_for_criteria)


class DataSetRemoverDummyCasesTest(DataSetsRemoverTestBase):
    def setUp(self):
        self.data_set_remover = DataSetRemover()
        self.data_set_info1 = DataSetInfo("Test", pandas.DataFrame([]))

    def test_given_array_with_data_set_and_correct_data_set_name_when_remove_data_set_then_return_empty_array(self):
        data_set_name = "Test"
        self.assertEqual([], self.data_set_remover.remove_data_set([self.data_set_info1], data_set_name))

    def test_given_array_with_multiple_data_sets_and_correct_data_set_name_when_remove_data_set_then_return_array_without_that_data_set(
            self):
        data_set_info2 = DataSetInfo("Test2", pandas.DataFrame([]))
        data_set_info3 = DataSetInfo("Test3", pandas.DataFrame([]))
        data_set_name = "Test2"

        self.assertEqual([self.data_set_info1, data_set_info3],
                         self.data_set_remover.remove_data_set([self.data_set_info1, data_set_info2, data_set_info3],
                                                               data_set_name))
