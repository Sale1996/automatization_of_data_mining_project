import unittest

from data_set_loader.classes.data_set_loader import DataSetLoader
from data_set_loader.depedency_injector.container import Container
from data_set_loader.exceptions.loader_exceptions import WrongPathNameFormatError, FileIsNotFoundError, \
    MissingImportantColumnsError


class DataSetLoaderTestBase(unittest.TestCase):
    pass


class DataSetLoaderTestErrorCases(DataSetLoaderTestBase):
    def setUp(self):
        must_contained_columns_in_data_set = ['Year', 'Country Code']
        self.data_set_loader: DataSetLoader = Container.DataSetLoader(must_contained_columns_in_data_set)

    def test_given_None_when_load_data_set_then_return_minus_1_array(self):
        with self.assertRaises(WrongPathNameFormatError):
            self.data_set_loader.load_data_set_and_column_names(None)

    def test_given_wrong_pathname_when_load_data_set_then_return_minus_1_array(self):
        with self.assertRaises(FileIsNotFoundError):
            self.data_set_loader.load_data_set_and_column_names("wrong_pathname")

    def test_given_pathname_with_data_set_without_year_column_when_load_data_set_then_return_minus_1_array(self):
        with self.assertRaises(MissingImportantColumnsError):
            self.data_set_loader.load_data_set_and_column_names(
                "./test_data/dummy_excel_dataset_without_year_column.xlsx")

    def test_given_pathname_with_data_set_without_country_code_column_when_load_data_set_then_return_minus_1_array(
            self):
        with self.assertRaises(MissingImportantColumnsError):
            self.data_set_loader.load_data_set_and_column_names(
                "./test_data/dummy_excel_dataset_without_country_columns.xlsx")


class DataSetLoaderTestDummyDataSets(DataSetLoaderTestBase):

    def setUp(self):
        self.expected_arbitrary_column_names = ['Year', 'Country Code']
        self.expected_other_column_names = ['Test']
        self.data_set_loader: DataSetLoader = Container.DataSetLoader(self.expected_arbitrary_column_names)
        self.expected_data_set = [[1, 1, 1], [1, 1, 1]]

    def test_given_correct_pathname_of_excel_data_set_when_load_data_set_then_return_data_set_and_column_names(self):
        [data_set, arbitrary_column_names, other_column_names] = self.data_set_loader.load_data_set_and_column_names(
            "./test_data/dummy_excel_dataset.xlsx")

        self.assert_expected_data_and_columns_are_returned(arbitrary_column_names, other_column_names, data_set)

    def test_given_correct_pathname_of_csv_data_set_when_load_data_set_then_return_data_set_and_column_names(self):
        [data_set, arbitrary_column_names, other_column_names] = self.data_set_loader.load_data_set_and_column_names(
            "./test_data/dummy_cvs_dataset.csv")

        self.assert_expected_data_and_columns_are_returned(arbitrary_column_names, other_column_names, data_set)

    def test_given_correct_pathname_of_data_set_with_multiple_other_columns_when_load_data_set_then_return_data_set_and_column_names(
            self):
        self.expected_data_set = [[1, 1, 1, 1, 1], [1, 1, 1, 1, 1]]
        self.expected_other_column_names = ['Test', 'Test2', 'Test3']

        [data_set, arbitrary_column_names, other_column_names] = self.data_set_loader.load_data_set_and_column_names(
            "./test_data/dummy_excel_dataset_with_multiple_y_columns.xlsx")

        self.assert_expected_data_and_columns_are_returned(arbitrary_column_names, other_column_names, data_set)

    def assert_expected_data_and_columns_are_returned(self, arbitrary_column_names, other_column_names, data_set):
        self.assertTrue((self.expected_data_set == data_set.to_numpy()).all())
        self.assertEqual(self.expected_arbitrary_column_names, arbitrary_column_names)
        self.assertEqual(self.expected_other_column_names, other_column_names)
