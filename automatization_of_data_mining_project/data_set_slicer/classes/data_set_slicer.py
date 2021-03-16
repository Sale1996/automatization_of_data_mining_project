from typing import List
from data_set_slicer.classes.data_frame_slicer.data_frame_slicer import DataFrameSlicer


class DataSetSlicer(object):
    def __init__(self, data_frame_slicers: List[DataFrameSlicer]):
        self.data_frame_slicers = data_frame_slicers

    def slice_data_sets(self, data_sets_info):
        pass
