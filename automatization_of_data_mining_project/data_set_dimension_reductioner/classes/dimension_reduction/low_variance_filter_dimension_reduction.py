from data_set_dimension_reductioner.classes.data_class.dimension_reduction_result import DimensionReductionResult
from data_set_dimension_reductioner.classes.dimension_reduction.dimension_reduction import DimensionReduction

VARIANCE_THRESHOLD = 1


class LowVarianceFilterDimensionReduction(DimensionReduction):
    def reduce_dimensionality(self, x_data, y_data) -> DimensionReductionResult:
        var = x_data.var()
        variables = x_data.columns
        passed_columns = []
        for i in range(0, len(var)):
            if var[i] >= VARIANCE_THRESHOLD:
                passed_columns.append(variables[i])
        low_variance_filter_reduced_data_set = x_data[passed_columns]

        return DimensionReductionResult("Low variance filter", low_variance_filter_reduced_data_set.values)
