import unittest

from data_set_loader.data_set_loader import DataSetLoader


class DataSetLoaderTestBase(unittest.TestCase):
    pass


class DataSetLoaderTestErrorCases(DataSetLoaderTestBase):
    def setUp(self):
        self.data_set_loader = DataSetLoader()

    def test_given_None_when_load_data_set_then_return_minus_1_array(self):
        [data_set, arbitrary_column_names, other_column_names] = self.data_set_loader.get_data_set_and_column_names(
            None)

        self.assert_failed_load_data_are_returned(arbitrary_column_names, other_column_names, data_set)

    def test_given_wrong_pathname_when_load_data_set_then_return_minus_1_array(self):
        [data_set, arbitrary_column_names, other_column_names] = self.data_set_loader.get_data_set_and_column_names(
            "wrong_pathname")

        self.assert_failed_load_data_are_returned(arbitrary_column_names, other_column_names, data_set)

    def test_given_pathname_with_data_set_without_year_column_when_load_data_set_then_return_minus_1_array(self):
        [data_set, arbitrary_column_names, other_column_names] = self.data_set_loader.get_data_set_and_column_names(
            "./test_data/dummy_excel_dataset_without_year_column.xlsx")

        self.assert_failed_load_data_are_returned(arbitrary_column_names, other_column_names, data_set)

    def test_given_pathname_with_data_set_without_country_code_column_when_load_data_set_then_return_minus_1_array(
            self):
        [data_set, arbitrary_column_names, other_column_names] = self.data_set_loader.get_data_set_and_column_names(
            "./test_data/dummy_excel_dataset_without_country_columns.xlsx")

        self.assert_failed_load_data_are_returned(arbitrary_column_names, other_column_names, data_set)

    def assert_failed_load_data_are_returned(self, arbitrary_column_names, other_column_names, data_set):
        self.assertEqual(-1, data_set)
        self.assertEqual(-1, arbitrary_column_names)
        self.assertEqual(-1, other_column_names)


class DataSetLoaderTestDummyDataSets(DataSetLoaderTestBase):

    def setUp(self):
        self.data_set_loader = DataSetLoader()
        self.expected_data_set = [[1, 1, 1], [1, 1, 1]]
        self.expected_arbitrary_column_names = ['Year', 'Country Code']
        self.expected_other_column_names = ['Test']

    def test_given_correct_pathname_of_excel_data_set_when_load_data_set_then_return_data_set_and_column_names(self):
        [data_set, arbitrary_column_names, other_column_names] = self.data_set_loader.get_data_set_and_column_names(
            "./test_data/dummy_excel_dataset.xlsx")

        self.assert_expected_data_and_columns_are_returned(arbitrary_column_names, other_column_names, data_set)

    def test_given_correct_pathname_of_csv_data_set_when_load_data_set_then_return_data_set_and_column_names(self):
        [data_set, arbitrary_column_names, other_column_names] = self.data_set_loader.get_data_set_and_column_names(
            "./test_data/dummy_cvs_dataset.csv")

        self.assert_expected_data_and_columns_are_returned(arbitrary_column_names, other_column_names, data_set)

    def test_given_correct_pathname_of_data_set_with_multiple_other_columns_when_load_data_set_then_return_data_set_and_column_names(
            self):
        self.expected_data_set = [[1, 1, 1, 1, 1], [1, 1, 1, 1, 1]]
        self.expected_other_column_names = ['Test', 'Test2', 'Test3']

        [data_set, arbitrary_column_names, other_column_names] = self.data_set_loader.get_data_set_and_column_names(
            "./test_data/dummy_excel_dataset_with_multiple_y_columns.xlsx")

        self.assert_expected_data_and_columns_are_returned(arbitrary_column_names, other_column_names, data_set)

    def assert_expected_data_and_columns_are_returned(self, arbitrary_column_names, other_column_names, data_set):
        self.assertTrue((self.expected_data_set == data_set.to_numpy()).all())
        self.assertEqual(self.expected_arbitrary_column_names, arbitrary_column_names)
        self.assertEqual(self.expected_other_column_names, other_column_names)
