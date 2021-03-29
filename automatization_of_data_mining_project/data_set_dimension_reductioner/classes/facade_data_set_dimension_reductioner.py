from typing import List

from data_set_dimension_reductioner.classes.data_set_dimension_reductioner import DataSetDimensionReductioner
from data_set_dimension_reductioner.classes.dimension_reduction.dimension_reduction import DimensionReduction
from data_set_dimension_reductioner.classes.input_validator.input_validator import InputValidator


class FacadeDataSetDimensionReductioner(DataSetDimensionReductioner):
    def __init__(self, input_validator: InputValidator,
                 dimension_reductioners: List[DimensionReduction]):
        self.input_validator = input_validator
        self.dimension_reductioners = dimension_reductioners

    def get_reduced_data_sets(self, x_data, y_data):
        self.input_validator.validate(x_data, y_data)

        dimension_reduction_objects = []

        for dimension_reductioner in self.dimension_reductioners:
            dimension_reduction_objects.extend(dimension_reductioner.reduce_dimensionality(x_data, y_data))

        return dimension_reduction_objects

