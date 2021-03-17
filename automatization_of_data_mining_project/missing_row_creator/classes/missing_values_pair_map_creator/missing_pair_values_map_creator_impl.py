from missing_row_creator.classes.missing_values_pair_map_creator.missing_values_pair_map_creator import \
    MissingPairValuesMapCreator


class MissingPairValuesMapCreatorImpl(MissingPairValuesMapCreator):
    def create_map(self, data_set, first_column_pair_name,
                   second_column_pair_name, second_column_values_to_match):

        first_column_index, second_column_index = self.get_columns_indexes(data_set, first_column_pair_name,
                                                                           second_column_pair_name)
        missing_pair_values_map = {}

        for row in data_set.values:
            if row[first_column_index] in missing_pair_values_map:
                missing_pair_values_map = self.remove_second_column_value_if_it_is_contained_in_dataset(
                    row[first_column_index],
                    row[second_column_index],
                    missing_pair_values_map)
            else:
                missing_pair_values_map = self.create_first_column_instance_in_map(row[first_column_index],
                                                                                   missing_pair_values_map,
                                                                                   second_column_values_to_match)
                missing_pair_values_map = self.remove_second_column_value_if_it_is_contained_in_dataset(
                    row[first_column_index],
                    row[second_column_index],
                    missing_pair_values_map)

        return missing_pair_values_map

    def create_first_column_instance_in_map(self, first_column_value, missing_pair_values_map,
                                            second_column_values_to_match):
        updated_missing_pair_values_map = missing_pair_values_map.copy()
        updated_missing_pair_values_map[first_column_value] = second_column_values_to_match[:]
        return updated_missing_pair_values_map

    def remove_second_column_value_if_it_is_contained_in_dataset(self, first_column_value, second_column_value,
                                                                 missing_pair_values_map):
        updated_missing_pair_values_map = missing_pair_values_map.copy()
        if second_column_value in updated_missing_pair_values_map[first_column_value]:
            updated_missing_pair_values_map[first_column_value].remove(second_column_value)
        return updated_missing_pair_values_map

    def get_columns_indexes(self, data_set, first_column_pair_name, second_column_pair_name):
        second_column_index = data_set.columns.get_loc(second_column_pair_name)
        first_column_index = data_set.columns.get_loc(first_column_pair_name)
        return first_column_index, second_column_index
