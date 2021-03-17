from dataclasses import dataclass
from typing import List

import pandas


@dataclass
class DataSetInfo(object):
    data_set_name: str
    data_set: pandas.DataFrame
    must_contained_columns: List[str]
    other_column_names: List[str]
