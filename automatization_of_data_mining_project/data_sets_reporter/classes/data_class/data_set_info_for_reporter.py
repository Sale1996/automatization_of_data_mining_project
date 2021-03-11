from dataclasses import dataclass
from typing import List


@dataclass
class DataSetInfoForReporter(object):
    data_set_name: str
    data_set_columns: List[str]