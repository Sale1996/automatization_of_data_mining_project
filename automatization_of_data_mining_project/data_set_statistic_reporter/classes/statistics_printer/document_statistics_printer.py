from typing import List

from data_set_statistic_reporter.classes.statistics_printer.statistics_printer import StatisticsPrinter
import csv
import os
from datetime import datetime


class DocumentStatisticsPrinter(StatisticsPrinter):
    def __init__(self, document_path: str):
        self.document_path = document_path

    def print_statistics(self, statistics_as_data_set: List[List[str]]):
        current_time = datetime.now()
        current_time_string = current_time.strftime("%d_%m_%Y_%H_%M_%S")
        filename = os.path.join(
            self.document_path + "/data_sets_statistics_" + current_time_string + ".csv")
        with open(filename, "w") as f:
            writer = csv.writer(f)
            writer.writerows(statistics_as_data_set)
