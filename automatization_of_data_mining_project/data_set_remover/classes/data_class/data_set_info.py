from dataclasses import dataclass

import pandas


@dataclass
class DataSetInfo(object):
    data_set_name: str
    data_set: pandas.DataFrame
