import pandas as pd

FAILED_LOAD = [-1, -1, -1]
MUST_CONTAINED_TRAIN_COLUMNS = ['Year', 'Country Code']


class DataSetLoader(object):
    def get_data_set_and_column_names(self, pathname):
        if pathname is None:
            return FAILED_LOAD

        try:
            loaded_data = self.pandas_read(pathname)
        except FileNotFoundError:
            return FAILED_LOAD

        for required_column in MUST_CONTAINED_TRAIN_COLUMNS:
            if required_column not in loaded_data.columns.array:
                return FAILED_LOAD

        return self.extract_data_set_and_column_names(loaded_data)

    def pandas_read(self, pathname):
        if pathname.endswith(".xlsx"):
            loaded_data = pd.read_excel(pathname)
        else:
            loaded_data = pd.read_csv(pathname, encoding='ISO-8859-1', error_bad_lines=False)
        return loaded_data

    def extract_data_set_and_column_names(self, loaded_data):
        column_names = loaded_data.columns
        data_set = loaded_data[column_names]

        other_column_names = self.get_other_column_names(column_names)

        return data_set, MUST_CONTAINED_TRAIN_COLUMNS, other_column_names

    def get_other_column_names(self, column_names):
        other_column_names = []
        for i in column_names.tolist():
            if i not in MUST_CONTAINED_TRAIN_COLUMNS:
                other_column_names.append(i)
        return other_column_names
