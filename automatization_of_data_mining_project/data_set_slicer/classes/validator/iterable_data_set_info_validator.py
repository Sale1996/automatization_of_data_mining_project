from data_set_info_data_class.data_class.data_set_info import DataSetInfo
from data_set_slicer.classes.validator.data_slicer_validator import DataSlicerValidator
from data_set_slicer.exceptions.slicer_exceptions import WrongInputFormatError, NonIterableObjectError


class IterableDataSetInfoValidator(DataSlicerValidator):
    def validate(self, input_data):
        if input_data is None:
            raise WrongInputFormatError

        if not isinstance(input_data, list):
            raise NonIterableObjectError

        for data_set_info in input_data:
            if not isinstance(data_set_info, DataSetInfo):
                raise WrongInputFormatError
