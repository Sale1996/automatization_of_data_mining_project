from typing import List

from data_set_info_data_class.data_class.data_set_info import DataSetInfo


class DataFrameSlicer(object):
    def __init__(self, column_name: str):
        self.column_name = column_name

    def slice_data_sets(self, data_sets_info: List[DataSetInfo]) -> List[DataSetInfo]:
        pass