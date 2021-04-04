from typing import List

from termcolor import colored

from data_set_info_data_class.data_class.data_set_info import DataSetInfo
from pip._vendor.distlib.compat import raw_input

from nan_value_filler import NaNFiller

ERROR_STRING = colored('\n@ERROR ', 'red')
ERROR_RETURN_VALUE = -1


def get_data_sets_with_filled_nan_values(sliced_data_sets: List[DataSetInfo]):
    map_index_to_array_data_set_info_column_name_chosen_filling_method = {}
    while True:
        filling_step_main_menu = ('----------------------------------------------------------\n'
                                  '|            Fill NaN values for each column             |\n'
                                  '|--------------------------------------------------------|\n'
                                  '| Fill missing values with one of the following methods: |\n'
                                  '| - Fill with zeros                                      |\n'
                                  '| - Fill with minimum column value                       |\n'
                                  '| - Fill with maximum column value                       |\n'
                                  '| - Fill with mean column value                          |\n'
                                  '| - Fill with "missing value" string                     |\n'
                                  '| - Fill with multiple linear regression                 |\n'
                                  '| - Fill with logistic regression                        |\n'
                                  '|                                                        |\n'
                                  '----------------------------------------------------------\n'
                                  '                                                         \n'
                                  ' 1) Continue process                                     \n'
                                  ' 2) Fill all columns by same filling method              \n')

        filling_step_main_menu = add_column_names_to_menu_and_initialize_map(filling_step_main_menu,
                                                                             map_index_to_array_data_set_info_column_name_chosen_filling_method,
                                                                             sliced_data_sets)

        # get user choice
        user_choice = raw_input(filling_step_main_menu)

        if user_choice == '0':
            # back to main menu
            return ERROR_RETURN_VALUE
        elif user_choice == '1':
            # exit filling menu and continue to fill missing data
            if are_all_filling_methods_chosen_for_each_column(
                    map_index_to_array_data_set_info_column_name_chosen_filling_method):
                print(ERROR_STRING, "Filling method is not chosen for every column")
                continue
            else:
                # leave while loop
                break
        elif user_choice == '2':
            column_filing_method_menu_header = '\n All columns                            \n'
            filling_options = get_filing_options_string()
            column_filling_method_menu = column_filing_method_menu_header + filling_options

            user_filing_method_choice = raw_input(column_filling_method_menu)

            if user_filing_method_choice == '1':
                choose_filling_method_for_all_columns(
                    map_index_to_array_data_set_info_column_name_chosen_filling_method, 'fill_with_zero')
            elif user_filing_method_choice == '2':
                choose_filling_method_for_all_columns(
                    map_index_to_array_data_set_info_column_name_chosen_filling_method, 'fill_with_min_value')
            elif user_filing_method_choice == '3':
                choose_filling_method_for_all_columns(
                    map_index_to_array_data_set_info_column_name_chosen_filling_method, 'fill_with_max_value')
            elif user_filing_method_choice == '4':
                choose_filling_method_for_all_columns(
                    map_index_to_array_data_set_info_column_name_chosen_filling_method, 'fill_with_mean_value')
            elif user_filing_method_choice == '5':
                choose_filling_method_for_all_columns(
                    map_index_to_array_data_set_info_column_name_chosen_filling_method,
                    'fill_with_missing_value_category')
            elif user_filing_method_choice == '6':
                choose_filling_method_for_all_columns(
                    map_index_to_array_data_set_info_column_name_chosen_filling_method,
                    'fill_with_multiple_linear_regression')
            elif user_filing_method_choice == '7':
                choose_filling_method_for_all_columns(
                    map_index_to_array_data_set_info_column_name_chosen_filling_method, 'fill_with_logistic_regression')
            else:
                print(ERROR_STRING, "Wrong input, please type a number between 1 and 7.")
                continue
        else:
            if user_choice not in map_index_to_array_data_set_info_column_name_chosen_filling_method:
                print(ERROR_STRING, "Wrong input choice!")
                continue

            item_info = map_index_to_array_data_set_info_column_name_chosen_filling_method.get(user_choice)

            column_filing_method_menu_header = '\n Column name: ' + colored(item_info[1], 'magenta') + '\n'
            filling_options = get_filing_options_string()
            column_filling_method_menu = column_filing_method_menu_header + filling_options

            user_filing_method_choice = raw_input(column_filling_method_menu)

            if user_filing_method_choice == '1':
                item_info[2] = 'fill_with_zero'
            elif user_filing_method_choice == '2':
                item_info[2] = 'fill_with_min_value'
            elif user_filing_method_choice == '3':
                item_info[2] = 'fill_with_max_value'
            elif user_filing_method_choice == '4':
                item_info[2] = 'fill_with_mean_value'
            elif user_filing_method_choice == '5':
                item_info[2] = 'fill_with_missing_value_category'
            elif user_filing_method_choice == '6':
                item_info[2] = 'fill_with_multiple_linear_regression'
            elif user_filing_method_choice == '7':
                item_info[2] = 'fill_with_logistic_regression'
            else:
                print(ERROR_STRING, "Wrong input, please type a number between 1 and 7.")

            continue

    nan_value_filler = NaNFiller()
    updated_data_sets = {}
    for data_info in map_index_to_array_data_set_info_column_name_chosen_filling_method.values():
        if data_info[0].data_set_name in updated_data_sets:
            data_set_info_to_fill = updated_data_sets[data_info[0].data_set_name]
        else:
            data_set_info_to_fill = data_info[0]

        # if there is any missing data for specific column, then use filler to fill the data
        if data_set_info_to_fill.data_set[data_info[1]].isnull().values.any():
            updated_data_set_info: DataSetInfo = nan_value_filler.fill_nan_values(data_set_info_to_fill, data_info[2],
                                                                                  data_info[1])
            updated_data_sets[updated_data_set_info.data_set_name] = updated_data_set_info
        else:
            updated_data_sets[data_set_info_to_fill.data_set_name] = data_set_info_to_fill

    filled_data_sets_info = list(updated_data_sets.values())

    return filled_data_sets_info


def choose_filling_method_for_all_columns(map_index_to_array_data_set_info_column_name_chosen_filling_method,
                                          filling_method):
    for item_info in map_index_to_array_data_set_info_column_name_chosen_filling_method.values():
        item_info[2] = filling_method


def get_filing_options_string():
    filling_options = (' Filling options:                                         \n'
                       '                                                          \n'
                       ' 1) Fill with zeros                                       \n'
                       ' 2) Fill with minimum column value                        \n'
                       ' 3) Fill with maximum column value                        \n'
                       ' 4) Fill with mean column value                           \n'
                       ' 5) Fill with "missing value" string                      \n'
                       ' 6) Fill with multiple linear regression                  \n'
                       ' 7) Fill with logistic regression                         \n'
                       '\n'
                       ' Chose: ')
    return filling_options


def are_all_filling_methods_chosen_for_each_column(map_index_to_array_data_set_info_column_name_chosen_filling_method):
    is_there_non_chosen_filling_method = False
    for item_info in map_index_to_array_data_set_info_column_name_chosen_filling_method.values():
        if item_info[2] == '':
            is_there_non_chosen_filling_method = True
    return is_there_non_chosen_filling_method


def add_column_names_to_menu_and_initialize_map(filling_step_main_menu,
                                                map_index_to_array_data_set_info_column_name_chosen_filling_method,
                                                sliced_data_sets):
    starting_index = 3
    for sliced_data_set in sliced_data_sets:
        data_set_columns = sliced_data_set.other_column_names
        for data_set_column_name in data_set_columns:
            if str(starting_index) not in map_index_to_array_data_set_info_column_name_chosen_filling_method:
                map_index_to_array_data_set_info_column_name_chosen_filling_method[str(starting_index)] = [
                    sliced_data_set,
                    data_set_column_name,
                    '']

            filling_step_main_menu += ' ' + str(starting_index) + ') ' + data_set_column_name + ' ' + colored(
                map_index_to_array_data_set_info_column_name_chosen_filling_method[str(starting_index)][2],
                'magenta') + '\n'
            starting_index += 1
    filling_step_main_menu += ' 0) Return to main menu \n Choose:'
    return filling_step_main_menu
