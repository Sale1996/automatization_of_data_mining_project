from dataclasses import dataclass
from typing import List

import pandas as pd


@dataclass
class StatisticReporterDataClass(object):
    data_set_name: str
    data_set: pd.DataFrame
    columns_for_range_report: List[str]
    columns_for_unique_impression_report: List[str]
    columns_for_variation_report: List[str]
    columns_for_missing_data_statistic_report: List[str]