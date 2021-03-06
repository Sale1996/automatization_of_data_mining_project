from typing import List, Tuple

import pandas

from data_set_loader.classes.pandas_data_set_loader.processor.converter.column_pair_converter import ColumnPairConverter
from data_set_loader.classes.pandas_data_set_loader.processor.data_processor import DataProcessor

'''
  Column which needs to be transformed into other pair 'pair_important_column'
  for example 'Country Name' is changeable column and 'Country Code' is important column
'''


class DataProcessorForPairOfMustContainedColumns(DataProcessor):

    def __init__(self, column_pair_converter: ColumnPairConverter):
        self.column_pair_converter = column_pair_converter

    def update_data_set_and_must_contained_columns(self, loaded_data: pandas.DataFrame,
                                                   must_contained_columns: List[str],
                                                   pairs_of_must_contained_columns: List[Tuple[str, str]])\
            -> (pandas.DataFrame, List[str]):

        updated_data_set = loaded_data
        updated_must_contained_columns = must_contained_columns

        for pair_of_must_contained_columns in pairs_of_must_contained_columns:
            pair_important_column = pair_of_must_contained_columns[0]
            pair_changeable_column = pair_of_must_contained_columns[1]

            updated_must_contained_columns = self.__add_important_column_to_must_contained_columns_array(
                updated_must_contained_columns, pair_important_column)

            if not self.__is_contained_in_data(updated_data_set, pair_changeable_column):
                continue

            if self.__is_contained_in_data(updated_data_set, pair_important_column):
                updated_data_set = self.__remove_changeable_column_from_data_set(updated_data_set, pair_changeable_column)
                continue

            updated_data_set = self.column_pair_converter.convert_values_of_changeable_column_to_match_important_column \
                (updated_data_set, pair_important_column, pair_changeable_column)

        return updated_data_set, updated_must_contained_columns

    def __add_important_column_to_must_contained_columns_array(self, must_contained_columns, additional_important_column):
        updated_must_contained_columns = must_contained_columns[:]
        updated_must_contained_columns.append(additional_important_column)

        return updated_must_contained_columns

    def __is_contained_in_data(self, loaded_data, column_name):
        return column_name in loaded_data.columns.tolist()

    def __remove_changeable_column_from_data_set(self, loaded_data, pair_changeable_column):
        columns_without_changeable_column = loaded_data.columns.tolist()[:]
        columns_without_changeable_column.remove(pair_changeable_column)
        data_set_without_changeable_column = loaded_data[columns_without_changeable_column]
        return data_set_without_changeable_column
