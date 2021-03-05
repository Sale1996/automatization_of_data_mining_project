from data_set_loader.classes.pandas_data_set_loader.loader.data_loader import DataLoader
from data_set_loader.classes.pandas_data_set_loader.loader.pandas_reader.pandas_reader import PandasReader
from data_set_loader.exceptions.loader_exceptions import FileIsNotFoundError


class DataFrameWithColumnsArrayLoader(DataLoader):
    def __init__(self, pandas_reader: PandasReader):
        self.pandas_reader = pandas_reader

    def load_data(self, pathname):
        try:
            loaded_data = self.pandas_reader.read(pathname)
        except FileNotFoundError:
            raise FileIsNotFoundError
        return loaded_data

    def extract_data(self, loaded_data, must_contained_columns):
        return self.__extract_data_set_and_column_names(loaded_data, must_contained_columns)

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
