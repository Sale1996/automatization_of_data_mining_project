from dataclasses import dataclass
from typing import List

from data_set_info_data_class.data_class.data_set_info import DataSetInfo

'''
    Note: 
        Columns to include/exclude should never be non empty or empty at the same time!
        So if there is some elements in "columns_to_exclude", then other one should be empty!
'''


@dataclass
class DataForCriteriaRemove(object):
    data_sets_info: List[DataSetInfo]
    criteria_name: str
    criteria_value: int
    columns_to_exclude: List[str]
    columns_to_include: List[str]


