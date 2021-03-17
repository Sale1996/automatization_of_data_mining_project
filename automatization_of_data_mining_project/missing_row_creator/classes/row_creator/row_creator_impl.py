from missing_row_creator.classes.row_creator.row_creator import RowCreator


class RowCreatorImpl(RowCreator):
    def add_rows(self, data_set, first_column_pair_name,
                 second_column_pair_name, missing_pair_values_map):
        first_column_pair_index, second_column_pair_index = self.get_column_indexes(data_set, first_column_pair_name,
                                                                                    second_column_pair_name)
        number_of_columns = len(data_set.columns.tolist())

        data_set_values = self.add_existing_data_to_updated_data_set(data_set)

        data_set_values = self.add_missing_rows(data_set_values, first_column_pair_index, missing_pair_values_map,
                                                number_of_columns,
                                                second_column_pair_index)

        return data_set_values

    def get_column_indexes(self, data_set, first_column_pair_name, second_column_pair_name):
        second_column_pair_index = data_set.columns.get_loc(second_column_pair_name)
        first_column_pair_index = data_set.columns.get_loc(first_column_pair_name)
        return first_column_pair_index, second_column_pair_index

    def add_existing_data_to_updated_data_set(self, data_set):
        data_set_values = []
        for data in data_set.values:
            data_set_values.append(data)
        return data_set_values

    def add_missing_rows(self, data_set_values, first_column_pair_index, missing_pair_values_map, number_of_columns,
                         second_column_pair_index):
        updated_data_set_values = data_set_values

        for first_column_pair_value in missing_pair_values_map:
            list_of_second_column_missing_second_pair_values = missing_pair_values_map[first_column_pair_value]
            for missing_second_pair_value in list_of_second_column_missing_second_pair_values:
                new_row = self.create_new_row_with_column_pair_values_and_nan_on_other_columns(first_column_pair_index,
                                                                                               first_column_pair_value,
                                                                                               missing_second_pair_value,
                                                                                               number_of_columns,
                                                                                               second_column_pair_index)
                updated_data_set_values.append(new_row)

        return updated_data_set_values

    def create_new_row_with_column_pair_values_and_nan_on_other_columns(self, first_column_pair_index,
                                                                        first_column_pair_value,
                                                                        missing_second_pair_value, number_of_columns,
                                                                        second_column_pair_index):
        new_row = [float('nan') for x in range(number_of_columns)]
        new_row[second_column_pair_index] = missing_second_pair_value
        new_row[first_column_pair_index] = first_column_pair_value
        return new_row
