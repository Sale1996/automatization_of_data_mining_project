from typing import List

import numpy
from sklearn.ensemble import RandomForestRegressor

from data_set_dimension_reductioner.classes.data_class.dimension_reduction_parameters.random_forest_parameters import \
    RandomForestParameters
from data_set_dimension_reductioner.classes.data_class.dimension_reduction_result import DimensionReductionResult
from data_set_dimension_reductioner.classes.dimension_reduction.dimension_reduction import DimensionReduction

NUMBER_OF_FEATURES = 2
RANDOM_STATE = 1
MAX_DEPTH = 10


def get_default_parameters() -> List[RandomForestParameters]:
    return [RandomForestParameters(NUMBER_OF_FEATURES, RANDOM_STATE, MAX_DEPTH)]


class RandomForestDimensionReduction(DimensionReduction):
    def __init__(self, parameters: List[RandomForestParameters] = get_default_parameters()):
        super().__init__(parameters)

    def reduce_dimensionality(self, x_data, y_data) -> List[DimensionReductionResult]:
        reduced_data_sets = []

        for parameters_object in self.parameters:
            model = RandomForestRegressor(random_state=parameters_object.random_state,
                                          max_depth=parameters_object.max_depth)
            model.fit(x_data, y_data.values.ravel())
            features = x_data.columns
            importances = model.feature_importances_
            indices = numpy.argsort(importances)[-parameters_object.number_of_features:]

            reduced_columns = []
            for indice in indices:
                reduced_columns.append(features[indice])
            random_forest_reduced_data_set = x_data[reduced_columns]

            number_of_columns_before = x_data.shape[1]
            number_of_columns_after = random_forest_reduced_data_set.shape[1]

            name = "Random Forest reduction" + "| Parameters: Number of features = " + str(parameters_object.number_of_features) + "; Random state = " + str(parameters_object.random_state) + "; Max depth = " + str(parameters_object.max_depth)

            reduced_data_sets.append(
                DimensionReductionResult(name, random_forest_reduced_data_set.values,
                                         number_of_columns_before, number_of_columns_after))

        return reduced_data_sets
