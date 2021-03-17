import pandas

from data_set_info_data_class.data_class.data_set_info import DataSetInfo
from missing_row_creator.classes.missing_row_creator import MissingRowCreator
from missing_row_creator.classes.missing_row_validator.missing_row_validator import MissingRowValidator
from missing_row_creator.classes.missing_values_pair_map_creator.missing_values_pair_map_creator import \
    MissingPairValuesMapCreator
from missing_row_creator.classes.row_creator.row_creator import RowCreator


class FacadeMissingRowCreator(MissingRowCreator):
    def __init__(self, validator: MissingRowValidator, missing_pair_values_map_creator: MissingPairValuesMapCreator,
                 row_creator: RowCreator):
        self.validator = validator
        self.missing_pair_values_map_creator = missing_pair_values_map_creator
        self.row_creator = row_creator

    def create_missing_rows(self, data_sets_info, first_column_pair_name,
                            second_column_pair_name, second_column_values_to_match):
        self.validator.validate(data_sets_info, first_column_pair_name,
                                second_column_pair_name, second_column_values_to_match)

        filled_data_sets = []
        for data_set_info in data_sets_info:
            country_years_map = self.missing_pair_values_map_creator.create_map(data_set_info.data_set,
                                                                                first_column_pair_name,
                                                                                second_column_pair_name,
                                                                                second_column_values_to_match)
            data_with_added_rows = self.row_creator.add_rows(data_set_info.data_set,
                                                             first_column_pair_name,
                                                             second_column_pair_name,
                                                             country_years_map)

            updated_data_set_info = self.create_new_data_set_info_object(data_set_info, data_with_added_rows)
            filled_data_sets.append(updated_data_set_info)

        return filled_data_sets

    def create_new_data_set_info_object(self, data_set_info, filled_data_set):
        updated_data_frame = pandas.DataFrame(filled_data_set, columns=data_set_info.data_set.columns.tolist())
        return DataSetInfo(data_set_info.data_set_name, updated_data_frame,
                           data_set_info.must_contained_columns,
                           data_set_info.other_column_names)
