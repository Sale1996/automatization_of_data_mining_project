import pandas as pd

from data_set_loader.classes.data_set_loader import DataSetLoader
from data_set_loader.exceptions.loader_exceptions import WrongPathNameFormatError, FileIsNotFoundError, \
    MissingImportantColumnsError


class PandasDataSetLoader(DataSetLoader):

    def load_data_set_and_column_names(self, pathname):
        self.__check_pathname(pathname)
        loaded_data = self.__load_data(pathname)
        self.__check_are_required_columns_inside(loaded_data, self.must_contained_columns)
        return self.__extract_data_set_and_column_names(loaded_data, self.must_contained_columns)

    def __check_pathname(self, pathname):
        if pathname is None:
            raise WrongPathNameFormatError

    def __load_data(self, pathname):
        try:
            loaded_data = self.__pandas_read(pathname)
        except FileNotFoundError:
            raise FileIsNotFoundError
        return loaded_data

    def __pandas_read(self, pathname):
        if pathname.endswith(".xlsx"):
            loaded_data = pd.read_excel(pathname)
        else:
            loaded_data = pd.read_csv(pathname, encoding='ISO-8859-1', error_bad_lines=False)
        return loaded_data

    def __check_are_required_columns_inside(self, loaded_data, must_contained_columns):
        for required_column in must_contained_columns:
            if required_column not in loaded_data.columns.tolist():
                raise MissingImportantColumnsError

    def __extract_data_set_and_column_names(self, loaded_data, must_contained_columns):
        column_names = loaded_data.columns
        data_set = loaded_data[column_names]
        other_column_names = self.__get_other_column_names(column_names, must_contained_columns)
        return data_set, must_contained_columns, other_column_names

    def __get_other_column_names(self, column_names, must_contained_columns):
        other_column_names = []
        for i in column_names.tolist():
            if i not in must_contained_columns:
                other_column_names.append(i)
        return other_column_names
