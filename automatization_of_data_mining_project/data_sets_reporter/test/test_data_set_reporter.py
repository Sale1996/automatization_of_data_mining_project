import unittest

from data_sets_reporter.classes.data_class.data_set_info_for_reporter import DataSetInfoForReporter
from data_sets_reporter.depedency_injector.container import Container
from data_sets_reporter.exceptions.register_exeptions import WrongInputFormatError, NonIterableObjectError


class DataSetsListingTestBase(unittest.TestCase):
    pass


class DataSetsListingTestErrorCases(DataSetsListingTestBase):
    def setUp(self):
        self.data_set_reporter = Container.data_set_reporter()

    def test_given_None_when_listing_data_sets_then_throw_input_format_exception(self):
        with self.assertRaises(WrongInputFormatError):
            self.data_set_reporter.get_report_listing_of_data_sets(None)

    def test_given_non_array_element_when_listing_data_sets_then_throw_non_iterable_exception(self):
        non_iterable_object = 1

        with self.assertRaises(NonIterableObjectError):
            self.data_set_reporter.get_report_listing_of_data_sets(non_iterable_object)

    def test_given_array_with_one_element_tuple_when_listing_data_sets_then_throw_input_format_exception(self):
        array_with_one_element_tuple = ["Test"]

        with self.assertRaises(WrongInputFormatError):
            self.data_set_reporter.get_report_listing_of_data_sets(array_with_one_element_tuple)

    def test_given_array_with_wrong_first_tuple_element_when_listing_data_sets_then_throw_input_format_exception(self):
        array_with_wrong_first_tuple_element = [(1, ["Test"])]

        with self.assertRaises(WrongInputFormatError):
            self.data_set_reporter.get_report_listing_of_data_sets(array_with_wrong_first_tuple_element)

    def test_given_array_with_wrong_format_on_second_tuple_element_when_listing_data_sets_then_throw_input_format_ex(
            self):
        array_with_wrong_format_on_second_tuple_element = [("Test", "Test2")]

        with self.assertRaises(WrongInputFormatError):
            self.data_set_reporter.get_report_listing_of_data_sets(array_with_wrong_format_on_second_tuple_element)

    def test_given_array_with_wrong_elements_on_second_tuple_element_when_listing_data_sets_then_throw_input_format_ex(
            self):
        array_with_wrong_elements_on_second_tuple_element = [("Test", [1, "Test"])]

        with self.assertRaises(WrongInputFormatError):
            self.data_set_reporter.get_report_listing_of_data_sets(array_with_wrong_elements_on_second_tuple_element)


class DataSetsListingOnDummyDataSetLists(DataSetsListingTestBase):
    def setUp(self):
        self.data_set_reporter = Container.data_set_reporter()

    def test_given_empty_data_sets_list_when_listing_data_sets_then_return_string_listing_for_empty_case(self):
        expected_string_report = "THERE IS NO DATA SET TO LIST\n\n\n"

        string_report = self.data_set_reporter.get_report_listing_of_data_sets([])

        self.assertEqual(expected_string_report, string_report)

    def test_given_array_with_one_data_set_when_listing_data_sets_then_return_string_listing_for_one_data_set(self):
        expected_string_report = "\nDummy data set name\n\nColumns:\n\nTest || Test2 || Test3\n\n\n==========\n"

        data_set_info = DataSetInfoForReporter("Dummy data set name", ["Test", "Test2", "Test3"])

        string_report = self.data_set_reporter.get_report_listing_of_data_sets([data_set_info])

        self.assertEqual(expected_string_report, string_report)

    def test_given_array_with_multiple_data_sets_when_listing_data_sets_then_return_correct_string_report(
            self):
        expected_string_report = "\nDummy data set name\n\nColumns:\n\nTest || Test2 || Test3\n\n\n==========\n"
        expected_string_report += "\nDummy data set 2 name\n\nColumns:\n\nTest3 || Test4 || Test5\n\n\n==========\n"

        data_set_info1 = DataSetInfoForReporter("Dummy data set name", ["Test", "Test2", "Test3"])
        data_set_info2 = DataSetInfoForReporter("Dummy data set 2 name", ["Test3", "Test4", "Test5"])

        string_report = self.data_set_reporter.get_report_listing_of_data_sets(
            [data_set_info1, data_set_info2])

        self.assertEqual(expected_string_report, string_report)
