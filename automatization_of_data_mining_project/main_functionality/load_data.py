from pip._vendor.distlib.compat import raw_input
from termcolor import colored

from data_set_info_data_class.data_class.data_set_info import DataSetInfo
from data_set_loader import Loader
from data_set_loader.exceptions.loader_exceptions import WrongPathNameFormatError, FileIsNotFoundError, \
    MissingImportantColumnsError

ERROR_STRING = colored('\n@ERROR ', 'red')
ERROR_RETURN_VALUE = -1
SUCCESS_STRING = colored('SUCCESS', 'green')


def load_data_set():
    loader_menu = get_loader_starting_menu()
    document_path = raw_input(loader_menu)
    data_set_loader = initialize_loader()

    try:
        [data_set, arbitrary_column_names, other_column_names] = data_set_loader.load_data_set_and_column_names(
            document_path)
    except WrongPathNameFormatError:
        print(ERROR_STRING, "Wrong path name please try again!\n")
        return ERROR_RETURN_VALUE
    except FileIsNotFoundError:
        print(ERROR_STRING, "There is no file at pathname location!\n")
        return ERROR_RETURN_VALUE
    except MissingImportantColumnsError:
        print(ERROR_STRING,
              "'Year' or ['Country Code'/'Country Name'] column is missing in your data set! Please check spelling of your columns\n")
        return ERROR_RETURN_VALUE

    data_set_name = get_data_set_name()

    data_set_info = DataSetInfo(data_set_name, data_set, arbitrary_column_names, other_column_names)

    print(SUCCESS_STRING, "Data set with name " + data_set_name + " is loaded!")

    return data_set_info


def get_loader_starting_menu():
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
    return loader_menu


def initialize_loader():
    must_contained_columns = ['Year']
    pairs_of_must_contained_columns = [('Country Code', 'Country Name')]
    data_set_loader = Loader(must_contained_columns, pairs_of_must_contained_columns)
    return data_set_loader


def get_data_set_name():
    data_set_name = raw_input("Please enter data set name:")
    return data_set_name
