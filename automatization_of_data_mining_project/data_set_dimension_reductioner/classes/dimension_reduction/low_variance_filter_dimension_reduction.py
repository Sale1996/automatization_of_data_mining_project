from typing import List

from data_set_dimension_reductioner.classes.data_class.dimension_reduction_parameters.factor_analysis_parameters import \
    FactorAnalysisParameters
from data_set_dimension_reductioner.classes.data_class.dimension_reduction_parameters.low_variance_filter_parameters import \
    LowVarianceFilterParameters
from data_set_dimension_reductioner.classes.data_class.dimension_reduction_result import DimensionReductionResult
from data_set_dimension_reductioner.classes.dimension_reduction.dimension_reduction import DimensionReduction

VARIANCE_THRESHOLD = 1


def get_default_parameters() -> List[LowVarianceFilterParameters]:
    return [LowVarianceFilterParameters(VARIANCE_THRESHOLD)]


class LowVarianceFilterDimensionReduction(DimensionReduction):
    def __init__(self, parameters: List[LowVarianceFilterParameters] = get_default_parameters()):
        super().__init__(parameters)

    def reduce_dimensionality(self, x_data, y_data) -> List[DimensionReductionResult]:
        reduced_data_sets = []

        for parameters_object in self.parameters:
            var = x_data.var()
            variables = x_data.columns
            passed_columns = []
            for i in range(0, len(var)):
                if var[i] >= parameters_object.variance_threshold:
                    passed_columns.append(variables[i])
            low_variance_filter_reduced_data_set = x_data[passed_columns]

            reduced_data_sets.append(
                DimensionReductionResult("Low variance filter", low_variance_filter_reduced_data_set.values))

        return reduced_data_sets
