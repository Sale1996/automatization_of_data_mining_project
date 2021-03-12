from data_set_remover.classes.criteria_validator.criteria_value_validator.criteria_value_validator import \
    CriteriaValueValidator
from data_set_remover.exceptions.remover_exceptions import MissingPercentCriteriaValueMustBeBetween1and99


class MissingDataPercentCriteriaValueValidator(CriteriaValueValidator):
    def __init__(self):
        super().__init__()
        self.criteria_name = "MISSING_DATA_PERCENT_CRITERIA"

    def is_valid(self, value: int):
        if value < 1 or value > 99:
            raise MissingPercentCriteriaValueMustBeBetween1and99
