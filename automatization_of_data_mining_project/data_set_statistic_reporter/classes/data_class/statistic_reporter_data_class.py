from dataclasses import dataclass
from typing import List

import pandas as pd

from data_set_statistic_reporter.classes.statistic_generator.statistic_generator import StatisticGenerator


@dataclass
class StatisticReporterDataClass(object):
    data_set_name: str
    data_set: pd.DataFrame
    statistic_generators: List[StatisticGenerator]
