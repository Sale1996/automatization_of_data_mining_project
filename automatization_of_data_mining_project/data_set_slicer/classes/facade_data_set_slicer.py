from typing import List

from data_set_slicer.classes.data_frame_slicer.data_frame_slicer import DataFrameSlicer
from data_set_slicer.classes.data_set_slicer import DataSetSlicer
from data_set_slicer.classes.validator.data_slicer_validator import DataSlicerValidator
from data_set_slicer.exceptions.slicer_exceptions import NonExistingSlicingMethodError


class FacadeDataSetSlicer(DataSetSlicer):
    def __init__(self, data_frame_slicers: List[DataFrameSlicer], validator: DataSlicerValidator):
        super().__init__(data_frame_slicers)
        self.validator = validator

    def slice_data_sets(self, data_sets_info):
        self.validator.validate(data_sets_info)
        self.__check_is_there_any_data_frame_slicer()

        sliced_data_sets_info = data_sets_info
        for data_frame_slicer in self.data_frame_slicers:
            sliced_data_sets_info = data_frame_slicer.slice_data_sets(sliced_data_sets_info)

        return sliced_data_sets_info

    def __check_is_there_any_data_frame_slicer(self):
        if not self.data_frame_slicers:
            raise NonExistingSlicingMethodError
