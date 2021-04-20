from typing import List

from pip._vendor.distlib.compat import raw_input
from termcolor import colored

from data_set_info_data_class.data_class.data_set_info import DataSetInfo
from main_functionality.create_predictive_models import create_predictive_model_and_create_statistics
from main_functionality.create_statistics import create_data_sets_statistics_document
from main_functionality.load_data import load_data_set, initialize_loader
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

    '''
        TEST CASES
    '''
    data_set_loader = initialize_loader()
    [data_set, arbitrary_column_names, other_column_names] = data_set_loader.load_data_set_and_column_names(
        'C:/Users/Sale/Desktop/MASTER_PROJEKAT/test_tabele/agricultural_methane_emission.xlsx')
    data_set_info = DataSetInfo('Agricultural methane emission', data_set, arbitrary_column_names, other_column_names)
    loaded_data_sets.append(data_set_info)
    [data_set, arbitrary_column_names, other_column_names] = data_set_loader.load_data_set_and_column_names(
        'C:/Users/Sale/Desktop/MASTER_PROJEKAT/test_tabele/co-emissions-per-capita.csv')
    data_set_info = DataSetInfo('CO emissions', data_set, arbitrary_column_names, other_column_names)
    loaded_data_sets.append(data_set_info)
    [data_set, arbitrary_column_names, other_column_names] = data_set_loader.load_data_set_and_column_names(
        'C:/Users/Sale/Desktop/MASTER_PROJEKAT/test_tabele/CoruptionPerceptionIndex_filtered.xlsx')
    data_set_info = DataSetInfo('Coruption Perception Index', data_set, arbitrary_column_names, other_column_names)
    loaded_data_sets.append(data_set_info)
    [data_set, arbitrary_column_names, other_column_names] = data_set_loader.load_data_set_and_column_names(
        'C:/Users/Sale/Desktop/MASTER_PROJEKAT/test_tabele/daily-per-capita-supply-of-calories.csv')
    data_set_info = DataSetInfo('Daily per capita supply of calories', data_set, arbitrary_column_names, other_column_names)
    loaded_data_sets.append(data_set_info)
    [data_set, arbitrary_column_names, other_column_names] = data_set_loader.load_data_set_and_column_names(
        'C:/Users/Sale/Desktop/MASTER_PROJEKAT/test_tabele/death_rate.xlsx')
    data_set_info = DataSetInfo('Death rate', data_set, arbitrary_column_names, other_column_names)
    loaded_data_sets.append(data_set_info)
    [data_set, arbitrary_column_names, other_column_names] = data_set_loader.load_data_set_and_column_names(
        'C:/Users/Sale/Desktop/MASTER_PROJEKAT/test_tabele/electricity.xlsx')
    data_set_info = DataSetInfo('Electricity', data_set, arbitrary_column_names, other_column_names)
    loaded_data_sets.append(data_set_info)
    [data_set, arbitrary_column_names, other_column_names] = data_set_loader.load_data_set_and_column_names(
        'C:/Users/Sale/Desktop/MASTER_PROJEKAT/test_tabele/employers_percentage.xlsx')
    data_set_info = DataSetInfo('Employers percentage', data_set, arbitrary_column_names, other_column_names)
    loaded_data_sets.append(data_set_info)
    [data_set, arbitrary_column_names, other_column_names] = data_set_loader.load_data_set_and_column_names(
        'C:/Users/Sale/Desktop/MASTER_PROJEKAT/test_tabele/fertility_rate_births_per_women.xlsx')
    data_set_info = DataSetInfo('Fertility rate', data_set, arbitrary_column_names, other_column_names)
    loaded_data_sets.append(data_set_info)
    [data_set, arbitrary_column_names, other_column_names] = data_set_loader.load_data_set_and_column_names(
        'C:/Users/Sale/Desktop/MASTER_PROJEKAT/test_tabele/Freedom_of_the_Press_Data.xlsx')
    data_set_info = DataSetInfo('Freedom of the press data', data_set, arbitrary_column_names, other_column_names)
    loaded_data_sets.append(data_set_info)
    [data_set, arbitrary_column_names, other_column_names] = data_set_loader.load_data_set_and_column_names(
        'C:/Users/Sale/Desktop/MASTER_PROJEKAT/test_tabele/Global_Media_Freedom_Dataset.xlsx')
    data_set_info = DataSetInfo('Global media freedom', data_set, arbitrary_column_names, other_column_names)
    loaded_data_sets.append(data_set_info)
    [data_set, arbitrary_column_names, other_column_names] = data_set_loader.load_data_set_and_column_names(
        'C:/Users/Sale/Desktop/MASTER_PROJEKAT/test_tabele/human-rights-scores.csv')
    data_set_info = DataSetInfo('Human rights scores', data_set, arbitrary_column_names, other_column_names)
    loaded_data_sets.append(data_set_info)
    [data_set, arbitrary_column_names, other_column_names] = data_set_loader.load_data_set_and_column_names(
        'C:/Users/Sale/Desktop/MASTER_PROJEKAT/test_tabele/inflation.xlsx')
    data_set_info = DataSetInfo('inflation', data_set, arbitrary_column_names, other_column_names)
    loaded_data_sets.append(data_set_info)
    [data_set, arbitrary_column_names, other_column_names] = data_set_loader.load_data_set_and_column_names(
        'C:/Users/Sale/Desktop/MASTER_PROJEKAT/test_tabele/internet_users_filtered.xlsx')
    data_set_info = DataSetInfo('internet users', data_set, arbitrary_column_names, other_column_names)
    loaded_data_sets.append(data_set_info)
    [data_set, arbitrary_column_names, other_column_names] = data_set_loader.load_data_set_and_column_names(
        'C:/Users/Sale/Desktop/MASTER_PROJEKAT/test_tabele/military_expenditure_formated.xlsx')
    data_set_info = DataSetInfo('military expenditure', data_set, arbitrary_column_names, other_column_names)
    loaded_data_sets.append(data_set_info)
    [data_set, arbitrary_column_names, other_column_names] = data_set_loader.load_data_set_and_column_names(
        'C:/Users/Sale/Desktop/MASTER_PROJEKAT/test_tabele/population_density.xlsx')
    data_set_info = DataSetInfo('population density', data_set, arbitrary_column_names, other_column_names)
    loaded_data_sets.append(data_set_info)
    [data_set, arbitrary_column_names, other_column_names] = data_set_loader.load_data_set_and_column_names(
        'C:/Users/Sale/Desktop/MASTER_PROJEKAT/test_tabele/PTS-2019.xlsx')
    data_set_info = DataSetInfo('PTS', data_set, arbitrary_column_names, other_column_names)
    loaded_data_sets.append(data_set_info)
    [data_set, arbitrary_column_names, other_column_names] = data_set_loader.load_data_set_and_column_names(
        'C:/Users/Sale/Desktop/MASTER_PROJEKAT/test_tabele/shares_of_suicides.xlsx')
    data_set_info = DataSetInfo('shares of suicides', data_set, arbitrary_column_names, other_column_names)
    loaded_data_sets.append(data_set_info)
    [data_set, arbitrary_column_names, other_column_names] = data_set_loader.load_data_set_and_column_names(
        'C:/Users/Sale/Desktop/MASTER_PROJEKAT/test_tabele/share-with-alcohol-or-drug-use-disorders.csv')
    data_set_info = DataSetInfo('Alcohol or drug use disorders', data_set, arbitrary_column_names, other_column_names)
    loaded_data_sets.append(data_set_info)
    [data_set, arbitrary_column_names, other_column_names] = data_set_loader.load_data_set_and_column_names(
        'C:/Users/Sale/Desktop/MASTER_PROJEKAT/test_tabele/share-with-an-eating-disorder.csv')
    data_set_info = DataSetInfo('Eating disorder', data_set, arbitrary_column_names, other_column_names)
    loaded_data_sets.append(data_set_info)
    [data_set, arbitrary_column_names, other_column_names] = data_set_loader.load_data_set_and_column_names(
        'C:/Users/Sale/Desktop/MASTER_PROJEKAT/test_tabele/share-with-depression.csv')
    data_set_info = DataSetInfo('Depression', data_set, arbitrary_column_names, other_column_names)
    loaded_data_sets.append(data_set_info)
    [data_set, arbitrary_column_names, other_column_names] = data_set_loader.load_data_set_and_column_names(
        'C:/Users/Sale/Desktop/MASTER_PROJEKAT/test_tabele/share-with-mental-and-substance-disorders.csv')
    data_set_info = DataSetInfo('Mental or substance disorders', data_set, arbitrary_column_names, other_column_names)
    loaded_data_sets.append(data_set_info)
    [data_set, arbitrary_column_names, other_column_names] = data_set_loader.load_data_set_and_column_names(
        'C:/Users/Sale/Desktop/MASTER_PROJEKAT/test_tabele/unemployment.xlsx')
    data_set_info = DataSetInfo('unemployment', data_set, arbitrary_column_names, other_column_names)
    loaded_data_sets.append(data_set_info)
    [data_set, arbitrary_column_names, other_column_names] = data_set_loader.load_data_set_and_column_names(
        'C:/Users/Sale/Desktop/MASTER_PROJEKAT/test_tabele/urban_population_growth_sredjeno.xlsx')
    data_set_info = DataSetInfo('urban population growth', data_set, arbitrary_column_names, other_column_names)
    loaded_data_sets.append(data_set_info)

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
