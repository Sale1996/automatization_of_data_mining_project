from typing import List

from data_set_dimension_reductioner.classes.data_class.dimension_reduction_result import DimensionReductionResult
from data_set_dimension_reductioner.classes.input_validator.dimension_reduction_statistics.input_validator_for_dimension_reduction_statistics import \
    InputValidatorForDimensionReductionStatistics
from data_set_dimension_reductioner.exceptions.dimension_reduction_exceptions import WrongInputFormatError, \
    NonIterableObjectError


class InputValidatorForDimensionReductionStatisticsImpl(InputValidatorForDimensionReductionStatistics):
    def validate(self, dimension_reduction_reports: List[DimensionReductionResult]):
        if dimension_reduction_reports is None:
            raise WrongInputFormatError
        if not isinstance(dimension_reduction_reports, list):
            raise NonIterableObjectError

        for data in dimension_reduction_reports:
            if not isinstance(data, DimensionReductionResult):
                raise WrongInputFormatError
