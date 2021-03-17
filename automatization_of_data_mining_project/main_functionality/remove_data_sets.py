from typing import List

from pip._vendor.distlib.compat import raw_input
from termcolor import colored

from data_set_info_data_class.data_class.data_set_info import DataSetInfo
from data_set_remover import Remover
from data_set_remover.classes.data_class.data_for_criteria_remove import DataForCriteriaRemove
from data_set_remover.exceptions.remover_exceptions import WrongInputFormatError, NonIterableObjectError, \
    NonExistingDataSetWithGivenNameError, ColumnArraysShouldNotBeBothEmpty, ColumnArraysShouldNotBeBothFilled, \
    WrongCriteriaNameError, MissingColumnToIncludeError, MissingPercentCriteriaValueMustBeBetween1and99, \
    UniqueImpressionCriteriaValueMustBeGreaterThan1

ERROR_STRING = colored('\n@ERROR ', 'red')
ERROR_RETURN_VALUE = -1
SUCCESS_STRING = colored('SUCCESS', 'green')


def remove_data_set(data_sets_info):
    remover_menu = ('-----------------------------------------------------\n'
                    '|               Data set remover                    |\n'
                    '|---------------------------------------------------|\n'
                    '| Choose the way you want to remove data set:       |\n'
                    '|                                                   |\n'
                    '| 1) Delete data set manually                       |\n'
                    '| 2) Delete data set columns by some criteria       |\n'
                    '|                                                   |\n'
                    '-----------------------------------------------------\n'
                    'Enter your option:')

    choice = raw_input(remover_menu)

    if choice == '1':
        return remove_manually(data_sets_info)

    elif choice == '2':
        return remove_by_criteria(data_sets_info)

    return ERROR_RETURN_VALUE


def remove_manually(data_sets_info):
    secondary_menu = ('-----------------------------------------------------\n'
                      '|     Choose data set which you want to delete      |\n'
                      '-----------------------------------------------------\n')

    index_number_to_data_set_name_map = {}
    last_data_set_index = 1
    for data_set_info in data_sets_info:
        index_number_to_data_set_name_map[last_data_set_index] = data_set_info.data_set_name
        data_set_option_string = " " + str(last_data_set_index) + ") " + data_set_info.data_set_name + "\n"
        secondary_menu += data_set_option_string
        last_data_set_index += 1

    secondary_menu += "Enter data set number to delete:"

    choice_to_delete = int(raw_input(secondary_menu))

    if choice_to_delete < 1 or choice_to_delete > last_data_set_index:
        print(ERROR_STRING, "You have entered wrong data set index value!")
        return ERROR_RETURN_VALUE

    data_set_name_to_delete = index_number_to_data_set_name_map[choice_to_delete]

    data_set_remover = Remover()
    try:
        updated_data_sets = data_set_remover.remove_manually(data_sets_info,
                                                             data_set_name_to_delete)
        print(SUCCESS_STRING, 'Data set with name "' + data_set_name_to_delete +
              '" is deleted!')
        return updated_data_sets
    except WrongInputFormatError:
        print(ERROR_STRING, "Input for data set remover module is invalid!\n")
        return ERROR_RETURN_VALUE
    except NonIterableObjectError:
        print(ERROR_STRING, "Input for data set remover module is non iterable!\n")
        return ERROR_RETURN_VALUE
    except NonExistingDataSetWithGivenNameError:
        print(ERROR_STRING, "Data set with given name doesn't exists in the given data set list!\n")
        return ERROR_RETURN_VALUE


def remove_by_criteria(data_sets_info):
    criteria_remover_menu = ('-----------------------------------------------------\n'
                             '|            Delete columns by criteria             |\n'
                             '|---------------------------------------------------|\n'
                             '| Choose by which criteria you want to delete the   |\n'
                             '| data sets columns:                                |\n'
                             '|                                                   |\n'
                             '| 1) Delete if number of unique values is less than |\n'
                             '|    criteria value                                 |\n'
                             '| 2) Delete if percent of missing data is greater   |\n'
                             '|    than criteria value                            |\n'
                             '|                                                   |\n'
                             '| (Note: If column to delete is "Year", "Country    |\n'
                             '|  Code" or "Country Name" then whole data set will |\n'
                             '|  be deleted. Also, if after deletion of column,   |\n'
                             '|  data set leaves with columns only mentioned      |\n'
                             '|  above, it will be deleted too!)                  |\n'
                             '-----------------------------------------------------\n'
                             'Enter your option:')
    chosen_criteria_number = int(raw_input(criteria_remover_menu))

    if chosen_criteria_number < 1 or chosen_criteria_number > 2:
        print(ERROR_STRING, "You have entered wrong data set index value!")
        return ERROR_RETURN_VALUE

    chosen_criteria_name, secondary_menu = get_chosen_criteria_name_and_secondary_menu_string_by_chosen_option(
        chosen_criteria_number)

    chosen_criteria_value = int(raw_input(secondary_menu))

    columns_to_include, columns_to_exclude = create_columns_to_include_and_columns_to_exclude_arrays(data_sets_info)

    if not isinstance(columns_to_include, list):
        return ERROR_RETURN_VALUE

    data_for_criteria = DataForCriteriaRemove(data_sets_info,
                                              chosen_criteria_name, chosen_criteria_value,
                                              columns_to_exclude, columns_to_include)

    try:
        data_set_remover = Remover()
        updated_data_sets_info = data_set_remover.remove_by_criteria(data_for_criteria)
        print(SUCCESS_STRING, "Data sets are filtered by chosen criteria!")
        return updated_data_sets_info
    except WrongInputFormatError:
        print(ERROR_STRING, "Input for data set remover module is invalid!\n")
        return ERROR_RETURN_VALUE
    except NonIterableObjectError:
        print(ERROR_STRING, "Input for data set remover module is non iterable!\n")
        return ERROR_RETURN_VALUE
    except ColumnArraysShouldNotBeBothEmpty:
        print(ERROR_STRING, "Columns to include and columns to exclude arrays should not be both empty!")
        return ERROR_RETURN_VALUE
    except ColumnArraysShouldNotBeBothFilled:
        print(ERROR_STRING,
              "Columns to include and columns to exclude arrays should not be both filled with values at the same time!")
        return ERROR_RETURN_VALUE
    except WrongCriteriaNameError:
        print(ERROR_STRING, "Criteria with provided name does not exist!")
        return ERROR_RETURN_VALUE
    except MissingColumnToIncludeError:
        print(ERROR_STRING, "One column from the columns to include array is missing in one of the datasets")
        return ERROR_RETURN_VALUE
    except MissingPercentCriteriaValueMustBeBetween1and99:
        print(ERROR_STRING, "Criteria value for removing columns by missing percentage must be between 1 and 99!")
        return ERROR_RETURN_VALUE
    except UniqueImpressionCriteriaValueMustBeGreaterThan1:
        print(ERROR_STRING,
              "Criteria value for removing columns which by number of unique members must be greater than 1!")
        return ERROR_RETURN_VALUE


def get_chosen_criteria_name_and_secondary_menu_string_by_chosen_option(chosen_criteria_number):
    if chosen_criteria_number == 1:
        chosen_criteria_name = "NUMBER_OF_UNIQUE_IMPRESSIONS_CRITERIA"
        secondary_menu = ('-----------------------------------------------------\n'
                          '|          Number of unique column values           |\n'
                          '-----------------------------------------------------\n'
                          'Enter minimum number of unique column data (minimum is 1):')
    else:
        chosen_criteria_name = "MISSING_DATA_PERCENT_CRITERIA"
        secondary_menu = ('-----------------------------------------------------\n'
                          '|          Percent of missing data criteria         |\n'
                          '-----------------------------------------------------\n'
                          'Enter maximum percentage of missing data (1-99):')
    return chosen_criteria_name, secondary_menu


def create_columns_to_include_and_columns_to_exclude_arrays(data_sets_info):
    fill_columns_menu = ('------------------------------------------------------\n'
                         '|          Choose which columns to check             |\n'
                         '|----------------------------------------------------|\n'
                         '|                                                    |\n'
                         '| 1)Columns to include                               |\n'
                         '| 2)Columns to exclude                               |\n'
                         '| (Note: Only one array can be filled! Either        |\n'
                         '|  columns to include or columns to exclude!         |\n'
                         '|                                                    |\n'
                         '------------------------------------------------------\n'
                         'Enter your choice:')
    columns_to_check_user_choice = int(raw_input(fill_columns_menu))
    if columns_to_check_user_choice < 1 or columns_to_check_user_choice > 2:
        print(ERROR_STRING, "You have entered wrong value!")
        return ERROR_RETURN_VALUE, ERROR_RETURN_VALUE
    if columns_to_check_user_choice == 1:
        columns_to_exclude = []
        columns_to_include = get_chosen_column_names(data_sets_info)
    else:
        columns_to_include = []
        columns_to_exclude = get_chosen_column_names(data_sets_info)
    return columns_to_include, columns_to_exclude


def get_chosen_column_names(data_sets_info: List[DataSetInfo]):
    chosen_column_names = []

    while True:
        index_to_column_name_map = {}
        choose_columns_menu = ('------------------------------------------------------\n'
                               '|          Choose which columns to check             |\n'
                               '|----------------------------------------------------|\n'
                               )

        index = 1
        # FIRST PRINT ALL ARBITRARY COLUMNS ("Year", "Country Code" in our case)
        for arbitrary_column in data_sets_info[0].must_contained_columns:
            already_selected_text = colored(' * already selected', 'magenta') if (
                    arbitrary_column in chosen_column_names) else ""
            column_menu_item = ' ' + str(index) + ') ' + arbitrary_column + already_selected_text + '\n'
            choose_columns_menu += column_menu_item
            index_to_column_name_map[index] = arbitrary_column
            index += 1

        # THEN PRINT ALL OTHER COLUMNS THAT DATA SETS CONTAIN
        for data_set_info in data_sets_info:
            for other_column in data_set_info.other_column_names:
                already_selected_text = colored(' * already selected', 'magenta') if (
                        other_column in chosen_column_names) else ""
                column_menu_item = ' ' + str(index) + ') ' + other_column + already_selected_text + '\n'
                choose_columns_menu += column_menu_item
                index_to_column_name_map[index] = other_column
                index += 1

        choose_columns_menu += ' 0) Finish adding columns\nChoose your option:'

        chosen_option = int(raw_input(choose_columns_menu))

        if chosen_option < 0 or chosen_option > index - 1:
            print(ERROR_STRING, "You have entered wrong value!")
            return ERROR_RETURN_VALUE

        is_exit_option = chosen_option == 0
        if is_exit_option:
            return chosen_column_names

        if index_to_column_name_map[chosen_option] not in chosen_column_names:
            chosen_column_names.append(index_to_column_name_map[chosen_option])
