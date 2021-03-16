from missing_row_creator.classes.missing_row_creator import MissingRowCreator
from missing_row_creator.classes.missing_row_validator.missing_row_validator import MissingRowValidator


class FacadeMissingRowCreator(MissingRowCreator):
    def __init__(self, validator: MissingRowValidator):
        self.validator = validator

    def create_missing_rows(self, data_sets_info, year_range):
        self.validator.validate(data_sets_info, year_range)