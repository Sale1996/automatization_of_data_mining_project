import csv
import os
from datetime import datetime
from typing import List

from data_set_dimension_reductioner.classes.data_class.dimension_reduction_result import DimensionReductionResult
from data_set_dimension_reductioner.classes.data_set_dimension_reductioner import DataSetDimensionReductioner
from data_set_dimension_reductioner.classes.dimension_reduction.dimension_reduction import DimensionReduction
from data_set_dimension_reductioner.classes.input_validator.input_validator import InputValidator
from data_set_dimension_reductioner.exceptions.dimension_reduction_exceptions import WrongInputFormatError, \
    NonIterableObjectError


class FacadeDataSetDimensionReductioner(DataSetDimensionReductioner):
    def __init__(self, input_validator: InputValidator,
                 dimension_reductioners: List[DimensionReduction]):
        self.input_validator = input_validator
        self.dimension_reductioners = dimension_reductioners

    def get_reduced_data_sets(self, x_data, y_data) -> List[DimensionReductionResult]:
        self.input_validator.validate(x_data, y_data)

        dimension_reduction_objects = []

        for dimension_reductioner in self.dimension_reductioners:
            dimension_reduction_objects.extend(dimension_reductioner.reduce_dimensionality(x_data, y_data))

        return dimension_reduction_objects

    def get_report_data(self, reduced_data: List[DimensionReductionResult], document_path):
        if reduced_data is None:
            raise WrongInputFormatError
        if not isinstance(reduced_data, list):
            raise NonIterableObjectError

        for data in reduced_data:
            if not isinstance(data, DimensionReductionResult):
                raise WrongInputFormatError

        data_sets_report = []

        for data in reduced_data:
            data_sets_report.append([data.reduction_name])
            data_sets_report.append(["Number of columns before", "Number of columns after"])
            data_sets_report.append([data.number_of_columns_before, data.number_of_columns_after])

        current_time = datetime.now()
        current_time_string = current_time.strftime("%d_%m_%Y_%H_%M_%S")
        filename = os.path.join(
            document_path + "/dimension_reduction_statistics_" + current_time_string + ".csv")
        with open(filename, "w") as f:
            writer = csv.writer(f)
            writer.writerows(data_sets_report)
