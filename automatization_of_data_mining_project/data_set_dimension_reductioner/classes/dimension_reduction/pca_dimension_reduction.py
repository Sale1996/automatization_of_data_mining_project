from sklearn.decomposition import PCA

from data_set_dimension_reductioner.classes.data_class.dimension_reduction_result import DimensionReductionResult
from data_set_dimension_reductioner.classes.dimension_reduction.dimension_reduction import DimensionReduction

NUMBER_OF_COMPONENTS = 2


class PCADimensionReduction(DimensionReduction):
    def reduce_dimensionality(self, x_data, y_data) -> DimensionReductionResult:
        pca = PCA(n_components=NUMBER_OF_COMPONENTS)
        pca_reduced_data_set = pca.fit_transform(x_data.values)
        return DimensionReductionResult("PCA", pca_reduced_data_set)
