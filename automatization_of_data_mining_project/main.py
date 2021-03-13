from typing import List
from termcolor import colored

from pip._vendor.distlib.compat import raw_input

from data_set_loader import Loader
from data_set_loader.exceptions.loader_exceptions import WrongPathNameFormatError, FileIsNotFoundError, \
    MissingImportantColumnsError
from data_set_remover import Remover
from data_set_remover.classes.data_class.data_for_criteria_remove import DataForCriteriaRemove
from data_set_remover.classes.data_class.data_set_info import DataSetInfo
from data_set_remover.exceptions.remover_exceptions import WrongInputFormatError, NonIterableObjectError, \
    NonExistingDataSetWithGivenNameError, ColumnArraysShouldNotBeBothEmpty, ColumnArraysShouldNotBeBothFilled, \
    WrongCriteriaNameError, MissingColumnToIncludeError, MissingPercentCriteriaValueMustBeBetween1and99, \
    UniqueImpressionCriteriaValueMustBeGreaterThan1
from data_set_statistic_reporter import StatisticReporter
from data_set_statistic_reporter.classes.data_class.statistic_reporter_data_class import StatisticReporterDataClass
from data_set_statistic_reporter.classes.statistic_generator.implementations.column_names_statistic_generator import \
    ColumnNamesStatisticGenerator
from data_set_statistic_reporter.classes.statistic_generator.implementations.missing_data_statistic_generator import \
    MissingDataStatisticGenerator
from data_set_statistic_reporter.classes.statistic_generator.implementations.range_statistic_generator import \
    RangeStatisticGenerator
from data_set_statistic_reporter.classes.statistic_generator.implementations.unique_impression_statistic_generator import \
    UniqueImpressionStatisticGenerator
from data_set_statistic_reporter.classes.statistic_generator.implementations.variance_statistic_generator import \
    VarianceStatisticGenerator
from data_set_statistic_reporter.classes.statistic_generator.statistic_generator import StatisticGenerator
from data_sets_reporter import Reporter
from data_sets_reporter.classes.data_class.data_set_info_for_reporter import DataSetInfoForReporter

ERROR_STRING = colored('\n@ERROR ', 'red')


def menu():
    menu_string = ('-----------------------------------------\n'
                   '| AUTOMATIZATION OF DATA MINING PROJECT |\n'
                   '|---------------------------------------|\n'
                   '| 1) Load a data set to the program     |\n'
                   '| 2) List all uploaded data sets        |\n'
                   '| 3) Create data set statistics         |\n'
                   '| 4) Remove data set/sets               |\n'
                   '| 5) Exit                               |\n'
                   '-----------------------------------------\n'
                   'Enter your choice:')
    choice = raw_input(menu_string)
    return int(choice)


def load_data_set():
    loader_menu = ('-----------------------------------------------------\n'
                   '|               Data set loader                     |\n'
                   '|---------------------------------------------------|\n'
                   '| There is some rules need to be told,              |\n'
                   '| before we step to loading process:                |\n'
                   '|                                                   |\n'
                   '| - Data sets must contain:                         |\n'
                   '|   (note: Column names must be exactly the same)   |\n'
                   '|   -- "Year" column with no missing values         |\n'
                   '|   -- "Country Code" or "Country Name" column      |\n'
                   '|      with no missing values                       |\n'
                   '|                                                   |\n'
                   '| - You need to be sure if data sets data is        |\n'
                   '|   semantically correct                            |\n'
                   '|                                                   |\n'
                   '| - All missing values needs to be represented      |\n'
                   '|   as empty cells, not for example as "0"          |\n'
                   '|                                                   |\n'
                   '-----------------------------------------------------\n'
                   'Enter url path to your csv/excel document:')

    document_path = raw_input(loader_menu)
    must_contained_columns = ['Year']
    pairs_of_must_contained_columns = [('Country Code', 'Country Name')]
    data_set_loader = Loader(must_contained_columns, pairs_of_must_contained_columns)

    try:
        [data_set, arbitrary_column_names, other_column_names] = data_set_loader.load_data_set_and_column_names(
            document_path)
    except WrongPathNameFormatError:
        print(ERROR_STRING, "Wrong path name please try again!\n")
        return -1
    except FileIsNotFoundError:
        print(ERROR_STRING, "There is no file at pathname location!\n")
        return -1
    except MissingImportantColumnsError:
        print(ERROR_STRING,
              "'Year' or ['Country Code'/'Country Name'] column is missing in your data set! Please check spelling of your columns\n")
        return -1

    data_set_name = raw_input("Please enter data set name:")

    data_set_info = DataSetInfo(data_set_name, data_set, arbitrary_column_names, other_column_names)

    return data_set_info


def print_quick_info_of_loaded_data_sets(loaded_data_sets: List[DataSetInfo]):
    from data_sets_reporter.exceptions.register_exeptions import WrongInputFormatError, NonIterableObjectError

    print('\n')
    data_sets_reporter = Reporter()

    data_sets_informations_for_reporter: List[DataSetInfoForReporter] = []

    for data_set_info in loaded_data_sets:
        data_set_columns = data_set_info.must_contained_columns[:]
        data_set_columns.extend(data_set_info.other_column_names)
        data_set_information_for_reporter = DataSetInfoForReporter(data_set_info.data_set_name,
                                                                   data_set_columns)

        data_sets_informations_for_reporter.append(data_set_information_for_reporter)

    try:
        report = data_sets_reporter.get_report_listing_of_data_sets(data_sets_informations_for_reporter)
        print(report)
    except WrongInputFormatError:
        print(ERROR_STRING, "Input for data set reporter is invalid!\n")
        return
    except NonIterableObjectError:
        print(ERROR_STRING, "Input for data set reporter is not iterable!\n")
        return


def create_data_sets_statistics_document(loaded_data_sets: List[DataSetInfo]):
    from data_set_statistic_reporter.exceptions.reporter_exceptions import WrongInputFormatError, NonIterableObjectError

    statistic_reporter = StatisticReporter()
    data_sets_as_statistic_reporter_data: List[StatisticReporterDataClass] = []

    columns_statistic_generator = ColumnNamesStatisticGenerator([])
    range_statistic_generator = RangeStatisticGenerator(['Year'])
    unique_impression_statistic_generator = UniqueImpressionStatisticGenerator(['Country Code'])
    variance_statistic_generator = VarianceStatisticGenerator(["Year"])
    shared_statistic_generators: List[StatisticGenerator] = [columns_statistic_generator,
                                                             range_statistic_generator,
                                                             unique_impression_statistic_generator,
                                                             variance_statistic_generator]

    for data_set_info in loaded_data_sets:
        missing_data_statistic_generator: StatisticGenerator = MissingDataStatisticGenerator(
            data_set_info.other_column_names)
        data_set_statistic_generators = shared_statistic_generators[:]
        data_set_statistic_generators.append(missing_data_statistic_generator)

        data_set_as_statistic_reporter_data = StatisticReporterDataClass(data_set_info.data_set_name,
                                                                         data_set_info.data_set,
                                                                         data_set_statistic_generators)
        data_sets_as_statistic_reporter_data.append(data_set_as_statistic_reporter_data)

    try:
        statistic_reporter.print_statistic(data_sets_as_statistic_reporter_data)
        print(
            "\n Statistics are successfully created! They are located on 'data_set_statistic_reporter/generated_statistics'\n")
    except WrongInputFormatError:
        print(ERROR_STRING, "Input for statistics data set reporter is invalid!\n")
        return
    except NonIterableObjectError:
        print(ERROR_STRING, "Input for statistics data set reporter is not iterable!\n")
        return


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
        print("\nChoose data set which you want to delete:\n")
        index_number_to_data_set_name_map = {}
        starting_index = 1
        for data_set_info in data_sets_info:
            index_number_to_data_set_name_map[starting_index] = data_set_info.data_set_name
            print(str(starting_index) + ") " + data_set_info.data_set_name)
            starting_index += 1

        choice_to_delete = int(raw_input("Enter data set number to delete:"))
        if choice_to_delete < 1 or choice_to_delete > starting_index:
            print(ERROR_STRING, "You have entered wrong data set index value!")
            return -1
        data_set_remover = Remover()
        try:
            updated_data_sets = data_set_remover.remove_manually(data_sets_info,
                                                                 index_number_to_data_set_name_map[choice_to_delete])
            print('\nData set with name "', index_number_to_data_set_name_map[choice_to_delete],
                  '" is successfully deleted!')
            return updated_data_sets
        except WrongInputFormatError:
            print(ERROR_STRING, "Input for data set remover module is invalid!\n")
            return -1
        except NonIterableObjectError:
            print(ERROR_STRING, "Input for data set remover module is non iterable!\n")
            return -1
        except NonExistingDataSetWithGivenNameError:
            print(ERROR_STRING, "Data set with given name doesn't exists in the given data set list!\n")
            return -1

    elif choice == '2':
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
            return -1

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

        chosen_criteria_value = int(raw_input(secondary_menu))

        fill_columns_menu = ('------------------------------------------------------\n'
                             '|          Choose which columns to check             |\n'
                             '|----------------------------------------------------|\n'
                             '|                                                    |\n'
                             '| 1)Columns to include                               |\n'
                             '| 2)Columns to exclude                               |\n'
                             '| (Note: Only one array can be filled! Either colum- |\n'
                             '| ns to include or columns to exclude!               |\n'
                             '|                                                    |\n'
                             '------------------------------------------------------\n'
                             'Enter your choice:')

        columns_to_check_user_choice = int(raw_input(fill_columns_menu))
        if columns_to_check_user_choice < 1 or columns_to_check_user_choice > 2:
            print(ERROR_STRING, "You have entered wrong value!")
            return -1

        if columns_to_check_user_choice == 1:
            columns_to_exclude = []
            columns_to_include = get_chosen_column_names(data_sets_info)
        else:
            columns_to_include = []
            columns_to_exclude = get_chosen_column_names(data_sets_info)

        data_for_criteria = DataForCriteriaRemove(data_sets_info,
                                                  chosen_criteria_name, chosen_criteria_value,
                                                  columns_to_exclude, columns_to_include)

        try:
            data_set_remover = Remover()
            updated_data_sets_info = data_set_remover.remove_by_criteria(data_for_criteria)
            print("\n Data sets are filtered by chosen criteria!\n")
            return updated_data_sets_info
        except WrongInputFormatError:
            print(ERROR_STRING, "Input for data set remover module is invalid!\n")
            return -1
        except NonIterableObjectError:
            print(ERROR_STRING, "Input for data set remover module is non iterable!\n")
            return -1
        except ColumnArraysShouldNotBeBothEmpty:
            print(ERROR_STRING, "Columns to include and columns to exclude arrays should not be both empty!")
            return -1
        except ColumnArraysShouldNotBeBothFilled:
            print(ERROR_STRING, "Columns to include and columns to exclude arrays should not be both filled with values at the same time!")
            return -1
        except WrongCriteriaNameError:
            print(ERROR_STRING, "Criteria with provided name does not exist!")
            return -1
        except MissingColumnToIncludeError:
            print(ERROR_STRING, "One column from the columns to include array is missing in one of the datasets")
            return -1
        except MissingPercentCriteriaValueMustBeBetween1and99:
            print(ERROR_STRING, "Criteria value for removing columns by missing percentage must be between 1 and 99!")
            return -1
        except UniqueImpressionCriteriaValueMustBeGreaterThan1:
            print(ERROR_STRING, "Criteria value for removing columns which by number of unique members must be greater than 1!")
            return -1

    return -1


def get_chosen_column_names(data_sets_info: List[DataSetInfo]):
    chosen_column_names = []

    while True:
        index_to_column_name_map = {}
        choose_columns_menu = ('------------------------------------------------------\n'
                               '|          Choose which columns to check             |\n'
                               '|----------------------------------------------------|\n'
                               )

        index = 1
        for arbitrary_column in data_sets_info[0].must_contained_columns:
            already_selected_text = colored(' * already selected', 'magenta') if (arbitrary_column in chosen_column_names) else ""
            column_menu_item = ' ' + str(index) + ') ' + arbitrary_column + already_selected_text + '\n'
            choose_columns_menu += column_menu_item
            index_to_column_name_map[index] = arbitrary_column
            index += 1

        for data_set_info in data_sets_info:
            for other_column in data_set_info.other_column_names:
                column_menu_item = ' ' + str(index) + ') ' + other_column + '\n'
                choose_columns_menu += column_menu_item
                index_to_column_name_map[index] = other_column
                index += 1

        choose_columns_menu += ' 0) Finish adding columns\nChoose your option:'

        chosen_option = int(raw_input(choose_columns_menu))
        if chosen_option < 0 or chosen_option > index - 1:
            print(ERROR_STRING, "You have entered wrong value!")
            return -1

        if chosen_option == 0:
            return chosen_column_names

        if index_to_column_name_map[chosen_option] not in chosen_column_names:
            chosen_column_names.append(index_to_column_name_map[chosen_option])


def program():
    loaded_data_sets: List[DataSetInfo] = []
    while True:
        choice = menu()
        if choice == 1:
            loaded_data_set = load_data_set()
            if isinstance(loaded_data_set, DataSetInfo):
                loaded_data_sets.append(loaded_data_set)
        elif choice == 2:
            print_quick_info_of_loaded_data_sets(loaded_data_sets)
        elif choice == 3:
            create_data_sets_statistics_document(loaded_data_sets)
        elif choice == 4:
            updated_data_sets = remove_data_set(loaded_data_sets)
            if not isinstance(updated_data_sets, int):
                loaded_data_sets = updated_data_sets
        elif choice == 5:
            print("exit")
            break


if __name__ == '__main__':
    program()
