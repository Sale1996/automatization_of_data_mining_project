import pandas

from data_set_loader.classes.pandas_data_set_loader.loader.data_loader import DataLoader
from data_set_loader.classes.pandas_data_set_loader.processor.converter.column_pair_converter import ColumnPairConverter


class DocumentColumnPairConverter(ColumnPairConverter):

    def __init__(self, loader: DataLoader):
        self.loader = loader

    def convert_values_of_changeable_column_to_match_important_column(
            self, loaded_data: pandas.DataFrame,
            pair_important_column: str,
            pair_changeable_column: str) -> pandas.DataFrame:

        converter_data_set = self.__load_converter_data_set(pair_important_column, pair_changeable_column)
        changeable_column_to_important_column_map = self.__get_changeable_column_to_important_column_map(
            converter_data_set)
        updated_data_frame = self.__change_changeable_column_to_important_column_in_data_set(
            changeable_column_to_important_column_map, loaded_data, pair_important_column, pair_changeable_column)

        return updated_data_frame

    def __change_changeable_column_to_important_column_in_data_set(self, changeable_column_to_important_column_map,
                                                                 loaded_data, important_column,
                                                                 changeable_column):

        changeable_column_index = loaded_data.columns.get_loc(changeable_column)
        new_columns = self.__change_changeable_column_name_to_important_column_name(
            changeable_column_index, loaded_data, important_column)
        updated_data_set = self.__convert_values_of_changeable_column_into_corresponding_values_of_important_column(
            changeable_column_index, changeable_column_to_important_column_map, loaded_data)
        updated_data_frame = pandas.DataFrame(updated_data_set, columns=new_columns)

        return updated_data_frame

    def __convert_values_of_changeable_column_into_corresponding_values_of_important_column(
            self, changeable_column_index, changeable_column_to_important_column_map, loaded_data):

        # Add it only if map contains important column value for changeable column key value
        updated_data_set = []
        for row in loaded_data.values:
            if row[changeable_column_index] in changeable_column_to_important_column_map:
                new_row = row
                new_row[changeable_column_index] = changeable_column_to_important_column_map[row[changeable_column_index]]
                updated_data_set.append(new_row)

        return updated_data_set

    def __change_changeable_column_name_to_important_column_name(
            self, changeable_column_index, loaded_data, pair_important_column):

        new_columns = loaded_data.columns.tolist()[:]
        new_columns[changeable_column_index] = pair_important_column

        return new_columns

    def __get_changeable_column_to_important_column_map(self, converter_data_set):
        changeable_column_to_important_column_map = {}
        for converter_value in converter_data_set:
            changeable_column_to_important_column_map[converter_value[1]] = converter_value[0]
        return changeable_column_to_important_column_map

    def __load_converter_data_set(self, pair_important_column, pair_changeable_column):
        document_name = pair_important_column + '_' + pair_changeable_column
        document_name = document_name.replace(' ', '_')
        loaded_converter_data = self.loader.load_data(
            'C:/Users/Sale/Desktop/MASTER_PROJEKAT/automatization_of_data_mining_project/automatization_of_data_mining_project/data_set_loader/classes/pandas_data_set_loader/processor/converter/document_converter/data/' + document_name + '.xlsx')
        converter_data_set = loaded_converter_data[[pair_important_column, pair_changeable_column]].values
        return converter_data_set
