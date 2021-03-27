from sklearn.decomposition import FactorAnalysis

from data_set_dimension_reductioner.classes.data_class.dimension_reduction_result import DimensionReductionResult
from data_set_dimension_reductioner.classes.dimension_reduction.dimension_reduction import DimensionReduction

NUMBER_OF_COMPONENTS = 2


class FactorAnalysisDimensionReduction(DimensionReduction):
    def reduce_dimensionality(self, x_data, y_data) -> DimensionReductionResult:
        factor_analysis_reduced_data_set = FactorAnalysis(n_components=NUMBER_OF_COMPONENTS).fit_transform(
            x_data.values)

        return DimensionReductionResult("Factor Analysis", factor_analysis_reduced_data_set)
