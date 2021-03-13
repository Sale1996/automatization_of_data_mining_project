import pandas

from data_set_remover.classes.criteria_validator.criteria_value_validator.criteria_value_validator import \
    CriteriaValueValidator


class CriteriaColumnValidator(object):
    def __init__(self, criteria_value_validator: CriteriaValueValidator):
        self.criteria_name = None
        self.criteria_value_validator = criteria_value_validator

    def is_valid(self, data_set: pandas.DataFrame, column: str, criteria_value: int):
        pass

    def is_criteria_value_valid(self, criteria_value: int):
        self.criteria_value_validator.is_valid(criteria_value)
