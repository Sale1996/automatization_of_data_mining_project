from typing import List

from data_set_slicer.classes.data_class.data_set_info import DataSetInfo
from data_set_slicer.classes.data_frame_slicer.data_frame_slicer import DataFrameSlicer
from data_set_slicer.exceptions.slicer_exceptions import EmptyResultsError


class CrossSectionDataFrameSlicer(DataFrameSlicer):
    def __init__(self, column_name: str):
        super().__init__(column_name)

    def slice_data_sets(self, data_sets_info: List[DataSetInfo]) -> List[DataSetInfo]:
        intersection_values = self.get_cross_section_of_unique_values_of_column_of_data_sets(data_sets_info)

        self.check_is_there_not_cross_section(intersection_values)

        sliced_data_set_sets_info = []
        for data_set_info in data_sets_info:
            sliced_data_set = self.slice_data_frame(data_set_info, intersection_values)
            sliced_data_set_info = self.create_new_data_set_info_object(data_set_info, sliced_data_set)
            sliced_data_set_sets_info.append(sliced_data_set_info)

        return sliced_data_set_sets_info

    def get_cross_section_of_unique_values_of_column_of_data_sets(self, data_sets_info):
        unique_values_of_each_data_set = []
        for data_set_info in data_sets_info:
            column_unique_values = data_set_info.data_set[self.column_name].unique()
            unique_values_of_each_data_set.append(column_unique_values)
        intersection_values = list(set.intersection(*map(set, unique_values_of_each_data_set)))
        return intersection_values

    def check_is_there_not_cross_section(self, intersection_values):
        if not intersection_values:
            raise EmptyResultsError

    def slice_data_frame(self, data_set_info, intersection_values):
        sliced_data_set = data_set_info.data_set.loc[
            data_set_info.data_set[self.column_name].isin(intersection_values)]
        return sliced_data_set

    def create_new_data_set_info_object(self, data_set_info, sliced_data_set):
        sliced_data_set_info = DataSetInfo(data_set_info.data_set_name, sliced_data_set,
                                           data_set_info.must_contained_columns,
                                           data_set_info.other_column_names)
        return sliced_data_set_info
