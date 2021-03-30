import csv
import os
from datetime import datetime
from typing import List

from data_set_dimension_reductioner.classes.data_class.dimension_reduction_result import DimensionReductionResult
from data_set_dimension_reductioner.classes.data_set_dimension_reductioner import DataSetDimensionReductioner
from data_set_dimension_reductioner.classes.dimension_reduction.dimension_reduction import DimensionReduction
from data_set_dimension_reductioner.classes.dimension_reduction_statistics_reporter.statistic_reporter import \
    DimensionReductionStatisticReporter
from data_set_dimension_reductioner.classes.input_validator.dimension_reduction.input_validator import InputValidator
from data_set_dimension_reductioner.classes.input_validator.dimension_reduction_statistics.input_validator_for_dimension_reduction_statistics import \
    InputValidatorForDimensionReductionStatistics


class FacadeDataSetDimensionReductioner(DataSetDimensionReductioner):
    def __init__(self, input_validator: InputValidator,
                 dimension_reductioners: List[DimensionReduction],
                 dimension_reduction_statistics_reporter: InputValidatorForDimensionReductionStatistics,
                 statistic_reporter: DimensionReductionStatisticReporter):
        self.input_validator = input_validator
        self.dimension_reductioners = dimension_reductioners
        self.dimension_reduction_statistics_reporter = dimension_reduction_statistics_reporter
        self.statistic_reporter = statistic_reporter

    def get_reduced_data_sets(self, x_data, y_data) -> List[DimensionReductionResult]:
        self.input_validator.validate(x_data, y_data)

        dimension_reduction_objects = []

        for dimension_reductioner in self.dimension_reductioners:
            dimension_reduction_objects.extend(dimension_reductioner.reduce_dimensionality(x_data, y_data))

        return dimension_reduction_objects

    def create_dimension_reduction_statistics(self, dimension_reduction_results: List[DimensionReductionResult]):
        self.dimension_reduction_statistics_reporter.validate(dimension_reduction_results)
        self.statistic_reporter.generate_report(dimension_reduction_results)
