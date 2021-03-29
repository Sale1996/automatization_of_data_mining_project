from typing import List

from data_set_dimension_reductioner.classes.data_class.dimension_reduction_parameters.dimension_reduction_parameters import \
    DimensionReductionParameters


class DimensionReduction(object):
    def __init__(self, parameters: List[DimensionReductionParameters]):
        self.parameters = parameters

    def reduce_dimensionality(self, x_data, y_data):
        pass
