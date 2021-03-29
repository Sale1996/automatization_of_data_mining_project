from dataclasses import dataclass

from data_set_dimension_reductioner.classes.data_class.dimension_reduction_parameters.dimension_reduction_parameters import \
    DimensionReductionParameters


@dataclass
class RandomForestParameters(DimensionReductionParameters):
    number_of_features: int
    random_state: int
    max_depth: int
