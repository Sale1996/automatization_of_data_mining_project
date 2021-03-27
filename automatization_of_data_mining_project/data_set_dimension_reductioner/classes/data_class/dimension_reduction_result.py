from dataclasses import dataclass
from numpy.core.multiarray import ndarray


@dataclass
class DimensionReductionResult(object):
    reduction_name: str
    reduced_data_set: ndarray
