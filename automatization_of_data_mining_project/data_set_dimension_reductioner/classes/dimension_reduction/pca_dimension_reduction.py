from typing import List

from sklearn.decomposition import PCA

from data_set_dimension_reductioner.classes.data_class.dimension_reduction_parameters.pca_parameters import \
    PCAParameters
from data_set_dimension_reductioner.classes.data_class.dimension_reduction_result import DimensionReductionResult
from data_set_dimension_reductioner.classes.dimension_reduction.dimension_reduction import DimensionReduction

NUMBER_OF_COMPONENTS = 2


def get_default_parameters() -> List[PCAParameters]:
    return [PCAParameters(NUMBER_OF_COMPONENTS)]


class PCADimensionReduction(DimensionReduction):
    def __init__(self, parameters: List[PCAParameters] = get_default_parameters()):
        super().__init__(parameters)

    def reduce_dimensionality(self, x_data, y_data) -> List[DimensionReductionResult]:
        reduced_data_sets = []

        for parameters_object in self.parameters:
            pca = PCA(n_components=parameters_object.number_of_components)
            pca_reduced_data_set = pca.fit_transform(x_data.values)
            number_of_columns_before = x_data.shape[1]
            number_of_columns_after = pca_reduced_data_set.shape[1]

            name = "PCA" + "| Parameters: Number of components = " + str(parameters_object.number_of_components)

            reduced_data_sets.append(DimensionReductionResult(name, pca_reduced_data_set,
                                                              number_of_columns_before, number_of_columns_after))

        return reduced_data_sets
