from typing import List

from pip._vendor.distlib.compat import raw_input
from termcolor import colored

from data_set_info_data_class.data_class.data_set_info import DataSetInfo
from data_set_remover import Remover
from data_set_remover.classes.data_class.data_for_criteria_remove import DataForCriteriaRemove
from data_set_slicer import Slicer
from data_set_slicer.classes.data_frame_slicer.column_value_range_data_frame_slicer import \
    ColumnValueRangeDataFrameSlicer
from data_set_slicer.classes.data_frame_slicer.cross_section_data_frame_slicer import CrossSectionDataFrameSlicer
from data_set_slicer.classes.data_frame_slicer.data_frame_slicer import DataFrameSlicer
from main_functionality.create_statistics import create_data_sets_statistics_document
from missing_row_creator import MissingRowCreator

ERROR_STRING = colored('\n@ERROR ', 'red')
ERROR_RETURN_VALUE = -1


def get_loaded_data_sets_in_year_range_with_filled_rows(loaded_data_sets: List[DataSetInfo]):
    while True:
        year_from, year_to = get_year_extremes_from_user()

        if year_from == ERROR_RETURN_VALUE:
            continue

        sliced_data_sets_info = slide_data_sets_in_year_range(loaded_data_sets, year_from, year_to)

        data_sets_info_with_missing_rows = fill_missing_rows_in_year_range_for_every_country_code(sliced_data_sets_info,
                                                                                                  year_from, year_to)

        create_data_sets_statistics_document(data_sets_info_with_missing_rows,
                                             "C:/Users/Sale/Desktop/MASTER_PROJEKAT/automatization_of_data_mining_project/automatization_of_data_mining_project/generated_statistics/predicting_model_generation/filled_data_sets/")

        after_slicing_menu = ('----------------------------------------------------------\n'
                              '|          Creation of predictive models                 |\n'
                              '|--------------------------------------------------------|\n'
                              '| Data sets are sliced and filled to match year          |\n'
                              '| range.                                                 |\n'
                              '| Check the newly generated statistics about % of        |\n'
                              '| the missing data in included year range and enter the  |\n'
                              '| percentage of maximum allowed missing data which       |\n'
                              '| will be filled with one of the filling methods         |\n'
                              '| or                                                     |\n'
                              '| go back and choose another year range                  |\n'
                              '|                                                        |\n'
                              '| Choose:                                                |\n'
                              '|                                                        |\n'
                              '| 1) Enter maximum percentage of missing data            |\n'
                              '| 2) Choose different year range                         |\n'
                              '| 3) Go back to main menu                                |\n'
                              '|                                                        |\n'
                              '----------------------------------------------------------\n'
                              'Choose option: ')

        user_option = raw_input(after_slicing_menu)

        if user_option != '1' and user_option != '2' and user_option != '3':
            print(ERROR_STRING, "You have entered wrong value!")
            continue

        if user_option == '3':
            return ERROR_RETURN_VALUE
        if user_option == '2':
            continue
        if user_option == '1':
            refreshed_data_sets_info = get_percentage_and_remove_columns_with_greater_percentage_of_missing_data(
                data_sets_info_with_missing_rows)

            return refreshed_data_sets_info


def get_year_extremes_from_user():
    starter_menu = ('-----------------------------------------------------\n'
                    '|          Creation of predictive models            |\n'
                    '|---------------------------------------------------|\n'
                    '| For creation of predictive models all data sets   |\n'
                    '| will be sliced to the chosen year range and all   |\n'
                    '| data sets will contain shared Country Code values |\n'
                    '|                                                   |\n'
                    '-----------------------------------------------------\n'
                    'Choose year from: ')
    year_from_string = raw_input(starter_menu)
    if not year_from_string.isdigit():
        print(ERROR_STRING, 'Year from value should be numeric!')
        return ERROR_RETURN_VALUE, ERROR_RETURN_VALUE

    year_to_string = raw_input('Choose year to: ')
    if not year_to_string.isdigit():
        print(ERROR_STRING, 'Year to value should be numeric!')
        return ERROR_RETURN_VALUE, ERROR_RETURN_VALUE

    year_from = int(year_from_string)
    year_to = int(year_to_string)
    if year_to < year_from:
        print(ERROR_STRING, 'Year to should be higher that Year from value!')
        return ERROR_RETURN_VALUE, ERROR_RETURN_VALUE

    return year_from, year_to


def slide_data_sets_in_year_range(loaded_data_sets, year_from, year_to):
    cross_section_slicer: DataFrameSlicer = CrossSectionDataFrameSlicer("Country Code")
    column_value_range_slicer: DataFrameSlicer = ColumnValueRangeDataFrameSlicer("Year", (year_from, year_to))
    data_set_slicer = Slicer([cross_section_slicer, column_value_range_slicer])
    sliced_data_sets_info = data_set_slicer.slice_data_sets(loaded_data_sets)
    return sliced_data_sets_info


def fill_missing_rows_in_year_range_for_every_country_code(sliced_data_sets_info, year_from, year_to):
    year_range_array = list(range(year_from, year_to + 1))
    missing_row_creator = MissingRowCreator()
    data_sets_info_with_missing_rows = missing_row_creator.create_missing_rows(sliced_data_sets_info,
                                                                               "Country Code", "Year",
                                                                               year_range_array)
    return data_sets_info_with_missing_rows


def get_percentage_and_remove_columns_with_greater_percentage_of_missing_data(data_sets_info_with_missing_rows):
    while True:
        maximum_missing_data_percentage = raw_input("Enter maximum percentage of missing data:")
        if maximum_missing_data_percentage.isdigit():
            break
        print(ERROR_STRING, 'Percentage value should be numeric!')

    data_for_criteria = DataForCriteriaRemove(data_sets_info_with_missing_rows,
                                              "MISSING_DATA_PERCENT_CRITERIA",
                                              int(maximum_missing_data_percentage),
                                              ["Year", "Country Code"], [])
    data_set_remover = Remover()
    refreshed_data_sets_info = data_set_remover.remove_by_criteria(data_for_criteria)
    return refreshed_data_sets_info
