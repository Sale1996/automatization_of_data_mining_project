from typing import List

from nan_value_filler.classes.nan_filler.nan_filler import NanFiller
from nan_value_filler.classes.nan_value_filler import NanValueFiller
from nan_value_filler.classes.input_validator.input_validator import InputValidator


class FacadeNanValueFiller(NanValueFiller):
    def __init__(self, input_validator: InputValidator, nan_fillers: List[NanFiller]):
        self.input_validator = input_validator
        self.nan_fillers = nan_fillers

    def fill_nan_values(self, data_set_info, filling_method, filling_column_name):
        self.input_validator.validate(data_set_info, filling_method, filling_column_name)

        for nan_filler in self.nan_fillers:
            if nan_filler.name == filling_method:
                return nan_filler.fill_nan_values(data_set_info, filling_column_name)