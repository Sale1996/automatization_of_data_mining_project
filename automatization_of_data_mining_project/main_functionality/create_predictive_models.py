from typing import List

from termcolor import colored

from data_set_dimension_reductioner.classes.data_class.dimension_reduction_result import DimensionReductionResult
from data_set_info_data_class.data_class.data_set_info import DataSetInfo
from main_functionality.create_predicitve_models_sub_functionality.get_data_sets_with_filled_nan_values import \
    get_data_sets_with_filled_nan_values
from main_functionality.create_predicitve_models_sub_functionality.get_dimensionality_reduced_data_sets import \
    get_dimensionality_reduced_data_sets
from main_functionality.create_predicitve_models_sub_functionality.get_joined_data_set import get_joined_data_set
from main_functionality.create_predicitve_models_sub_functionality.get_preprocessed_data_frame import \
    get_preprocessed_data_frame
from main_functionality.create_predicitve_models_sub_functionality.get_sliced_data_sets import \
    get_loaded_data_sets_in_year_range_with_filled_rows

ERROR_STRING = colored('\n@ERROR ', 'red')
ERROR_RETURN_VALUE = -1


def create_predictive_model_and_create_statistics(loaded_data_sets: List[DataSetInfo]):
    # slice data sets
    sliced_data_sets_in_year_range = get_loaded_data_sets_in_year_range_with_filled_rows(loaded_data_sets)

    if sliced_data_sets_in_year_range == ERROR_RETURN_VALUE:
        return ERROR_RETURN_VALUE

    # fill nan values
    data_sets_with_filled_nan_values = get_data_sets_with_filled_nan_values(sliced_data_sets_in_year_range)

    if data_sets_with_filled_nan_values == ERROR_RETURN_VALUE:
        return ERROR_RETURN_VALUE

    # join all data sets
    joined_data_frame = get_joined_data_set(data_sets_with_filled_nan_values)

    # preprocess joined data set
    preprocessed_joined_data_frame = get_preprocessed_data_frame(joined_data_frame)

    # generate dimension reduction models
    train_dimension_reduction_results: List[DimensionReductionResult] = None
    test_dimension_reduction_results: List[DimensionReductionResult] = None
    train_dimension_reduction_results, test_dimension_reduction_results = get_dimensionality_reduced_data_sets(preprocessed_joined_data_frame)



    print("debug")

    return ERROR_RETURN_VALUE
