from typing import List

from data_set_statistic_reporter.classes.statistics_printer.statistics_printer import StatisticsPrinter
import csv
import os
from datetime import datetime


class DocumentStatisticsPrinter(StatisticsPrinter):
    def print_statistics(self, statistics_as_data_set: List[List[str]]):
        current_time = datetime.now()
        current_time_string = current_time.strftime("%d_%m_%Y_%H_%M_%S")
        filename = os.path.join(
            "C:/Users/Sale/Desktop/MASTER_PROJEKAT/automatization_of_data_mining_project/automatization_of_data_mining_project/data_set_statistic_reporter/generated_statistics/data_sets_statistics_" + current_time_string + ".csv")
        with open(filename, "w") as f:
            writer = csv.writer(f)
            writer.writerows(statistics_as_data_set)
