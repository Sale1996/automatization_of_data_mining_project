from typing import List, Tuple

from data_set_slicer.classes.data_class.data_set_info import DataSetInfo
from data_set_slicer.classes.data_frame_slicer.data_frame_slicer import DataFrameSlicer
from data_set_slicer.exceptions.slicer_exceptions import WrongRangeObjectFormatError, EmptyResultsError


class ColumnValueRangeDataFrameSlicer(DataFrameSlicer):
    def __init__(self, column_name: str, year_range: Tuple[int, int]):
        super().__init__(column_name)
        self.validate_year_range(year_range)
        self.year_range = year_range

    def slice_data_sets(self, data_sets_info: List[DataSetInfo]) -> List[DataSetInfo]:
        self.check_if_any_of_data_sets_contains_data_in_year_range(data_sets_info)

        sliced_data_set_sets_info = []
        for data_set_info in data_sets_info:
            sliced_data_set = self.slice_data_frame(data_set_info)
            sliced_data_set_info = self.create_new_data_set_info_object(data_set_info, sliced_data_set)
            sliced_data_set_sets_info.append(sliced_data_set_info)

        return sliced_data_set_sets_info

    def check_if_any_of_data_sets_contains_data_in_year_range(self, data_sets_info):
        is_there_data_in_range = False
        for data_set_info in data_sets_info:
            if data_set_info.data_set[self.column_name].between(self.year_range[0], self.year_range[1]).any():
                is_there_data_in_range = True
        if not is_there_data_in_range:
            raise EmptyResultsError

    def slice_data_frame(self, data_set_info):
        sliced_data_set = data_set_info.data_set.loc[
            data_set_info.data_set[self.column_name].between(self.year_range[0], self.year_range[1])]
        return sliced_data_set

    def create_new_data_set_info_object(self, data_set_info, sliced_data_set):
        return DataSetInfo(data_set_info.data_set_name, sliced_data_set,
                           data_set_info.must_contained_columns,
                           data_set_info.other_column_names)

    def validate_year_range(self, year_range):
        if not isinstance(year_range, tuple):
            raise WrongRangeObjectFormatError
        if len(year_range) != 2:
            raise WrongRangeObjectFormatError
        if not isinstance(year_range[0], int) or not isinstance(year_range[1], int):
            raise WrongRangeObjectFormatError
