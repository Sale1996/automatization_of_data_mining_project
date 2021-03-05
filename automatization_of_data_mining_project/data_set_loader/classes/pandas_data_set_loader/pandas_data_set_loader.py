from data_set_loader.classes.data_set_loader import DataSetLoader
from data_set_loader.classes.pandas_data_set_loader.pandas_reader.pandas_reader import PandasReader
from data_set_loader.classes.pandas_data_set_loader.pathname_checker.pathname_checker import PathNameChecker
from data_set_loader.exceptions.loader_exceptions import FileIsNotFoundError, \
    MissingImportantColumnsError


class PandasDataSetLoader(DataSetLoader):

    def __init__(self, column_names, pandas_reader: PandasReader, pathname_checker: PathNameChecker):
        super().__init__(column_names)
        self.pandas_reader = pandas_reader
        self.pathname_checker = pathname_checker

    def load_data_set_and_column_names(self, pathname):
        self.pathname_checker.check(pathname)
        loaded_data = self.__load_data(pathname)
        self.__check_are_required_columns_inside(loaded_data, self.must_contained_columns)
        return self.__extract_data_set_and_column_names(loaded_data, self.must_contained_columns)

    def __load_data(self, pathname):
        try:
            loaded_data = self.pandas_reader.read(pathname)
        except FileNotFoundError:
            raise FileIsNotFoundError
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
