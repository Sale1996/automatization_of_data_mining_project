from typing import List

from termcolor import colored

from data_set_info_data_class.data_class.data_set_info import DataSetInfo
from main_functionality.create_predicitve_models_sub_functionality.get_data_sets_with_filled_nan_values import \
    get_data_sets_with_filled_nan_values
from main_functionality.create_predicitve_models_sub_functionality.get_sliced_data_sets import \
    get_loaded_data_sets_in_year_range_with_filled_rows


ERROR_STRING = colored('\n@ERROR ', 'red')
ERROR_RETURN_VALUE = -1


def create_predictive_model_and_create_statistics(loaded_data_sets: List[DataSetInfo]):
    sliced_data_sets_in_year_range = get_loaded_data_sets_in_year_range_with_filled_rows(loaded_data_sets)

    if sliced_data_sets_in_year_range == ERROR_RETURN_VALUE:
        return ERROR_RETURN_VALUE

    data_sets_with_filled_nan_values = get_data_sets_with_filled_nan_values(sliced_data_sets_in_year_range)

    return ERROR_RETURN_VALUE
