import csv
import os
from datetime import datetime
from typing import List

from data_set_dimension_reductioner.classes.data_class.dimension_reduction_result import DimensionReductionResult
from data_set_dimension_reductioner.classes.dimension_reduction_statistics_reporter.statistic_reporter import \
    DimensionReductionStatisticReporter


class DimensionReductionDocumentStatisticReporter(DimensionReductionStatisticReporter):
    def __init__(self, document_path: str):
        self.document_path = document_path

    def generate_report(self, dimension_reduction_results: List[DimensionReductionResult]):
        data_sets_report = []

        for data in dimension_reduction_results:
            data_sets_report.append([data.reduction_name])
            data_sets_report.append(["Number of columns before", "Number of columns after"])
            data_sets_report.append([data.number_of_columns_before, data.number_of_columns_after])

        current_time = datetime.now()
        current_time_string = current_time.strftime("%d_%m_%Y_%H_%M_%S")
        filename = os.path.join(
            self.document_path + "/dimension_reduction_statistics_" + current_time_string + ".csv")
        with open(filename, "w") as f:
            writer = csv.writer(f)
            writer.writerows(data_sets_report)
