import unittest

from data_set_loader.classes.data_set_loader import DataSetLoader
from data_set_loader.depedency_injector.container import Container
from data_set_loader.exceptions.loader_exceptions import WrongPathNameFormatError, FileIsNotFoundError, \
    MissingImportantColumnsError


class DataSetLoaderTestBase(unittest.TestCase):
    pass


class DataSetLoaderTestErrorCases(DataSetLoaderTestBase):
    def setUp(self):
        must_contained_columns = ['Year']
        pairs_of_must_contained_columns = [('Country Code', 'Country Name')]
        self.data_set_loader: DataSetLoader = Container.data_set_loader(must_contained_columns,
                                                                        pairs_of_must_contained_columns)

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

    def test_given_pathname_with_data_set_without_country_code_and_country_name_column_when_load_data_set_then_return_minus_1_array(
            self):
        with self.assertRaises(MissingImportantColumnsError):
            self.data_set_loader.load_data_set_and_column_names(
                "./test_data/dummy_excel_dataset_without_country_columns.xlsx")


class DataSetLoaderTestDummyDataSets(DataSetLoaderTestBase):

    def setUp(self):
        must_contained_columns = ['Year']
        pairs_of_must_contained_columns = [('Country Code', 'Country Name')]
        self.expected_arbitrary_column_names = ['Year', 'Country Code']
        self.expected_other_column_names = ['Test']
        self.data_set_loader: DataSetLoader = Container.data_set_loader(must_contained_columns,
                                                                        pairs_of_must_contained_columns)

    def test_given_correct_pathname_of_excel_data_set_when_load_data_set_then_return_data_set_and_column_names(self):
        expected_data_set = [[1, 1, 1], [1, 1, 1]]
        [data_set, arbitrary_column_names, other_column_names] = self.data_set_loader.load_data_set_and_column_names(
            "./test_data/dummy_excel_dataset.xlsx")

        self.assert_expected_data_and_columns_are_returned(expected_data_set, arbitrary_column_names,
                                                           other_column_names, data_set)

    def test_given_correct_pathname_of_csv_data_set_when_load_data_set_then_return_data_set_and_column_names(self):
        expected_data_set = [[1, 1, 1], [1, 1, 1]]
        [data_set, arbitrary_column_names, other_column_names] = self.data_set_loader.load_data_set_and_column_names(
            "./test_data/dummy_cvs_dataset.csv")

        self.assert_expected_data_and_columns_are_returned(expected_data_set, arbitrary_column_names,
                                                           other_column_names, data_set)

    def test_given_correct_pathname_of_data_set_with_multiple_other_columns_when_load_data_set_then_return_data_set_and_column_names(
            self):
        expected_data_set = [[1, 1, 1, 1, 1], [1, 1, 1, 1, 1]]
        self.expected_other_column_names = ['Test', 'Test2', 'Test3']

        [data_set, arbitrary_column_names, other_column_names] = self.data_set_loader.load_data_set_and_column_names(
            "./test_data/dummy_excel_dataset_with_multiple_y_columns.xlsx")

        self.assert_expected_data_and_columns_are_returned(expected_data_set, arbitrary_column_names,
                                                           other_column_names, data_set)

    def assert_expected_data_and_columns_are_returned(self, expected_data_set, arbitrary_column_names,
                                                      other_column_names, data_set):
        self.assertTrue((expected_data_set == data_set.values).all())
        self.__assert_column_names_are_correct(arbitrary_column_names, other_column_names)

    def test_given_pathname_with_data_set_without_country_code_and_with_country_name_column_when_load_data_set_then_return_data_set(
            self):
        expected_data_set = [[2021, 'SRB', 1], [2020, 'SRB', 2]]
        [data_set, arbitrary_column_names, other_column_names] = self.data_set_loader.load_data_set_and_column_names(
            "./test_data/dummy_dataset_with_country_name_only.xlsx")

        self.assertion_for_country_datasets(data_set, expected_data_set, arbitrary_column_names, other_column_names)

    def test_given_pathname_with_data_set_with_country_code_and_country_name_when_load_data_set_then_return_data_set_without_country_name(
            self):
        expected_data_set = [[2021, 'SRB', 1], [2020, 'SRB', 2]]
        [data_set, arbitrary_column_names, other_column_names] = self.data_set_loader.load_data_set_and_column_names(
            "./test_data/dummy_dataset_with_country_code_and_country_name_columns.xlsx")

        self.assertion_for_country_datasets(data_set, expected_data_set, arbitrary_column_names, other_column_names)

    def test_given_pathname_with_data_set_with_non_existing_country_name_when_load_data_set_then_return_data_set(self):
        expected_data_set = [[2021, 'SRB', 1], [2020, 'SRB', 2]]
        [data_set, arbitrary_column_names, other_column_names] = self.data_set_loader.load_data_set_and_column_names(
            "./test_data/dummy_dataset_with_non_existing_country_name.xlsx")

        self.assertion_for_country_datasets(data_set, expected_data_set, arbitrary_column_names, other_column_names)

    def assertion_for_country_datasets(self, data_set, expected_data_set, arbitrary_column_names, other_column_names):
        self.assertTrue(self.__compare_data_sets(data_set, expected_data_set))
        self.__assert_column_names_are_correct(arbitrary_column_names, other_column_names)

    def __compare_data_sets(self, data_set, expected_data_set):
        data_frame_as_array = data_set.values
        data_set_size = len(data_frame_as_array)
        for index in range(0, data_set_size):
            if data_frame_as_array[index][0] != expected_data_set[index][0]:
                return False

            if data_frame_as_array[index][1] != expected_data_set[index][1]:
                return False

            if data_frame_as_array[index][2] != expected_data_set[index][2]:
                return False

        return True

    def __assert_column_names_are_correct(self, arbitrary_column_names, other_column_names):
        self.assertEqual(self.expected_arbitrary_column_names, arbitrary_column_names)
        self.assertEqual(self.expected_other_column_names, other_column_names)
