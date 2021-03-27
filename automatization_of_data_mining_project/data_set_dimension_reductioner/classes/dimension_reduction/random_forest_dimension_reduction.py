import numpy
from sklearn.ensemble import RandomForestRegressor

from data_set_dimension_reductioner.classes.data_class.dimension_reduction_result import DimensionReductionResult
from data_set_dimension_reductioner.classes.dimension_reduction.dimension_reduction import DimensionReduction

NUMBER_OF_FEATURES = 2
RANDOM_STATE = 1
MAX_DEPTH = 10


class RandomForestDimensionReduction(DimensionReduction):
    def reduce_dimensionality(self, x_data, y_data) -> DimensionReductionResult:
        model = RandomForestRegressor(random_state=RANDOM_STATE, max_depth=MAX_DEPTH)
        model.fit(x_data, y_data)
        features = x_data.columns
        importances = model.feature_importances_
        indices = numpy.argsort(importances)[-NUMBER_OF_FEATURES:]

        reduced_columns = []
        for indice in indices:
            reduced_columns.append(features[indice])
        random_forest_reduced_data_set = x_data[reduced_columns]
        return DimensionReductionResult("Random Forest reduction", random_forest_reduced_data_set.values)
