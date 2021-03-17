from typing import List

from pip._vendor.distlib.compat import raw_input
from termcolor import colored

from data_set_info_data_class.data_class.data_set_info import DataSetInfo
from main_functionality.create_predictive_models import create_predictive_model_and_create_statistics
from main_functionality.create_statistics import create_data_sets_statistics_document
from main_functionality.load_data import load_data_set
from main_functionality.print_data_set_info import print_quick_info_of_loaded_data_sets
from main_functionality.remove_data_sets import remove_data_set

ERROR_STRING = colored('\n@ERROR ', 'red')
ERROR_RETURN_VALUE = -1


def menu():
    menu_string = ('-----------------------------------------\n'
                   '| AUTOMATIZATION OF DATA MINING PROJECT |\n'
                   '|---------------------------------------|\n'
                   '| 1) Load a data set to the program     |\n'
                   '| 2) List all uploaded data sets        |\n'
                   '| 3) Create data set statistics         |\n'
                   '| 4) Remove data set/sets               |\n'
                   '| 5) Create predictive models and       |\n'
                   '|    create statistics                  |\n'
                   '| 0) Exit                               |\n'
                   '-----------------------------------------\n'
                   'Enter your choice:')
    choice = raw_input(menu_string)
    return choice


def program():
    loaded_data_sets: List[DataSetInfo] = []
    data_sets_in_year_range: List[DataSetInfo] = []
    while True:
        choice = menu()
        if choice == '1':
            loaded_data_set = load_data_set()
            if isinstance(loaded_data_set, DataSetInfo):
                loaded_data_sets.append(loaded_data_set)
        elif choice == '2':
            print_quick_info_of_loaded_data_sets(loaded_data_sets)
        elif choice == '3':
            create_data_sets_statistics_document(loaded_data_sets,
                                                 "C:/Users/Sale/Desktop/MASTER_PROJEKAT/automatization_of_data_mining_project/automatization_of_data_mining_project/generated_statistics")
        elif choice == '4':
            updated_data_sets = remove_data_set(loaded_data_sets)
            if not isinstance(updated_data_sets, int):
                loaded_data_sets = updated_data_sets
        elif choice == '5':
            data_sets_in_year_range = create_predictive_model_and_create_statistics(loaded_data_sets)
        elif choice == '0':
            print("exit")
            break
        else:
            print(ERROR_STRING, "Your choice must be between 1 and 5!\n")


if __name__ == '__main__':
    program()
